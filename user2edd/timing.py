"""
module: timing.py
source: http://stackoverflow.com/a/1557906/6009280
"""
# Stdlib imports
import atexit
from datetime import timedelta
from time import localtime, strftime, time

# Third-party app imports
# Imports from my apps


def _secondsToStr(elapsed=None):
    if elapsed is None:
        return strftime("%Y-%m-%d %H:%M:%S", localtime())
    else:
        return str(timedelta(seconds=elapsed))


def log(s, elapsed=None):
    line = "-" * 40
    print(line)
    print(f"{_secondsToStr()} - {s}")
    if elapsed:
        print(f"Elapsed time: {elapsed}")
    print(line)


def endlog():
    end = time()
    elapsed = end - start
    log("End Program", _secondsToStr(elapsed))


# ----------------------------------------------
start = time()
atexit.register(endlog)
log(f"Start Program")
