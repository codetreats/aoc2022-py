#!/bin/bash
cd $(dirname $0)

if [[ $# -eq 1 ]] ; then
  FILE=test/test_Day$1.py
fi
python -m unittest $FILE