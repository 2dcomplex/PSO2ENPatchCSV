#!/bin/bash
find . -name "*.csv" -print0|xargs -0 python3 check.py&>/dev/null||find . -name "*.csv" -print0|xargs -0 -n 1 python3 check.py
