#!/usr/bin/python

"""Logic for tracing repo interactions.
Activated via `repo --trace ...` or `REPO_TRACE=1 repo ...`.
"""

from __future__ import print_function

import os
import sys

# Env var to implicitly turn on tracing.
REPO_TRACE = "REPO_TRACE"

_TRACE = os.environ.get(REPO_TRACE) == "1"


def IsTrace():
    return _TRACE


def SetTrace():
    global _TRACE
    _TRACE = True


def Trace(fmt, *args):
    if IsTrace():
        print(fmt % args, file=sys.stderr)
