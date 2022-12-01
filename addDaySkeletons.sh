#!/bin/bash
DAYTEMPLATE="res/DayXX.py.template"
TESTTEMPLATE="res/test_DayXX.py.template"

RESFOLDER="res"
SRCFOLDER="aoc"
TESTFOLDER="test"

mkdir -p $RESFOLDER $SRCFOLDER $TESTFOLDER
touch "$SRCFOLDER/__init__.py"
touch "$TESTFOLDER/__init__.py"


for DAY in {01..25}; do
  SRCDIR="$SRCFOLDER/day$DAY"
  TESTDIR="$TESTFOLDER"
  RESDIR="$RESFOLDER/day$DAY"

  mkdir -p $SRCDIR $TESTDIR $RESDIR

  if ! [ -f "$SRCDIR/Day$DAY.py" ] ; then
    cat $DAYTEMPLATE | sed -e "s/XX/$DAY/g" | sed -e "s/(0/(/g" > "$SRCDIR/Day$DAY.py"
  fi
  if ! [ -f "$TESTDIR/test_Day""$DAY"".py" ] ; then
    cat $TESTTEMPLATE | sed -e "s/XX/$DAY/g" > "$TESTDIR/test_Day""$DAY"".py"
  fi
  if ! [ -f "$RESDIR/input.txt" ] ; then
    touch "$RESDIR/input.txt"
  fi
  if ! [ -f "$RESDIR/dummy.txt" ] ; then
    touch "$RESDIR/dummy.txt"
  fi
done