#!/bin/bash
cd $(dirname $0)
rm -rf test/*
rm -rf aoc/day*
rm -rf res/day*
./addDaySkeletons.sh