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

pytest ${tests[@]}