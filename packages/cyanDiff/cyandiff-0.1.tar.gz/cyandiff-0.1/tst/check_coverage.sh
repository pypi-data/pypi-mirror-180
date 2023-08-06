#!/usr/bin/env bash
set -e

tests=(
    cyanDiff/test_ad_helpers.py
    cyanDiff/test_ad_overloads.py
    cyanDiff/test_ad_types.py
    cyanDiff/test_critical_points.py
    cyanDiff/test_newton_raphson.py
    cyanDiff/test_reverse_mode.py
)

export PYTHONPATH="$(pwd -P)/../src":${PYTHONPATH}

coverage run -m pytest ${tests[@]}

# usage of the .coveragerc file means we don't need the --cov option
percent_str="$(coverage report -m| tail -1 | awk '{print $NF}')"

percent_num=${percent_str::-1}

echo "Code coverage percentage: $percent_num"

if [ $percent_num -ge 90 ]; then
    exit 0
else
    exit 1
fi