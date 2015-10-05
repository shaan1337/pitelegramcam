#!/bin/bash

cd "$(dirname "$0")"

killall motion
kill -9 `pgrep -f check_cmds.py`
