from .pseudo_traceback import _build_pseudo_trace_str

should_use_color = False
COLOR_RED = "\x1b[31m"
COLOR_RESET = "\x1b[0m"
_failures = []


def clear_failures():
    global _failures
    _failures = []


def any_failures() -> bool:
    return bool(get_failures())


def get_failures():
    return _failures


def log_failure(msg=""):
    __tracebackhide__ = True
    msg = str(msg).strip()
    pseudo_trace_str = _build_pseudo_trace_str()
    msg_plus_trace = f"{msg}\n{pseudo_trace_str}"
    if should_use_color:
        msg_plus_trace = f"{COLOR_RED}{msg_plus_trace}{COLOR_RESET}"
    entry = f"FAILURE: {msg_plus_trace}"
    _failures.append(entry)
