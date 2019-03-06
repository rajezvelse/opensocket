#!/usr/bin/env python

import os
import sys

if __name__ == "__main__":
    try:
        from core.management import execute_from_command_line
    except ImportError:
        raise
    execute_from_command_line(sys.argv)
