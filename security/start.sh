#!/bin/bash

cd "$(dirname "$0")"

./motion -c ./motion-mmalcam.conf
python ./scripts/check_cmds.py &
