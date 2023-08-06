# -*- coding: utf-8 -*-

import collections
import io
import os
from importlib import import_module

import pytest
from line_profiler import LineProfiler


def get_stats(lp: LineProfiler) -> str:
    s = io.StringIO()
    lp.print_stats(stream=s)
    return s.getvalue()


def import_string(dotted_path):
    """
    Import a dotted module path and return the object if is callable
    """
    if not isinstance(dotted_path, str):
        return dotted_path
    try:
        module_path, callable_name = dotted_path.rsplit(".", 1)
        module = import_module(module_path)
        callable_object = getattr(module, callable_name)
        assert callable(callable_object)
        return callable_object
    except (ModuleNotFoundError, ValueError, AttributeError, AssertionError):
        raise pytest.UsageError(f"{dotted_path} not found or is not callable")


def pytest_addoption(parser):
    group = parser.getgroup("line-profile")
    group.addoption(
        "--line-profile",
        action="store",
        nargs="*",
        help="Register a function to profile while executed tests.",
    )
    group._addoption(
        "--line-profile-to-dir",
        action="store",
        metavar="path",
        default="prof/",
        help="Save to line profiles to directory",
    )
    group._addoption(
        "--line-profile-no-print",
        dest="line_profile_print",
        action="store_false",
        default=True,
        help="Print line profiles to terminal",
    )
    group._addoption(
        "--line-profile-no-rst",
        dest="line_profile_rst",
        action="store_false",
        default=True,
        help="Also save an index.rst file in the line profile directory",
    )


def pytest_load_initial_conftests(early_config, parser, args):
    early_config.addinivalue_line(
        "markers",
        "line_profile: Line profile this test.",
    )


def pytest_runtest_call(item):
    instrumented = []
    if item.get_closest_marker("line_profile"):
        instrumented += [
            import_string(s) for s in item.get_closest_marker("line_profile").args
        ]
    if item.config.getvalue("line_profile"):
        instrumented += [import_string(s) for s in item.config.getvalue("line_profile")]

    if instrumented:
        lp = LineProfiler(*instrumented)
        item_runtest = item.runtest

        def runtest():
            # we must call run_test twice here because the second call with the line profiler does not track coverage
            item_runtest()
            lp.runcall(item_runtest)
            item.config._line_profile = getattr(item.config, "_line_profile", {})
            item.config._line_profile[item.nodeid] = get_stats(lp)

        item.runtest = runtest
    pass


def pytest_terminal_summary(
    terminalreporter: "TerminalReporter",
    exitstatus: "ExitCode",
    config: "Config",
) -> None:
    reports = getattr(config, "_line_profile", {})
    cur_file = ""
    for k, v in sorted(reports.items()):
        if config.option.line_profile_print:
            terminalreporter.write_sep("=", f"Line Profile result for {k}")
            terminalreporter.write(v)
        if config.option.line_profile_to_dir:
            os.makedirs(
                os.path.dirname(config.option.line_profile_to_dir + k + ".txt"),
                exist_ok=True,
            )
            with open(config.option.line_profile_to_dir + k + ".txt", "w") as f:
                f.write(v)
        if config.option.line_profile_rst:
            os.makedirs(
                os.path.dirname(config.option.line_profile_to_dir + "index.txt"),
                exist_ok=True,
            )
            if cur_file == "":
                open(config.option.line_profile_to_dir + "index.rst", "w").close()
            with open(config.option.line_profile_to_dir + "index.rst", "a") as f:
                file, meth = k.split("::")
                if cur_file != file:
                    f.write(file + "\n")
                    f.write("--------------------\n")
                    cur_file = file
                f.write(meth + "\n")
                f.write("^^^^^^^^^^^^^^^^^^^^\n")
                f.write(":: \n\n")
                f.write("\t" + "\n\t".join(v.split("\n")) + "\n\n")


@pytest.fixture
def line_profiler(request):
    lp = LineProfiler()
    yield lp
    request.addfinalizer(lp.print_stats)
