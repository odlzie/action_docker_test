#!/bin/sh -l

echo "Hellow $1"
time=$(date)
ech "time=$time" >> $GITHUB_OUTPUT