#!/bin/bash

adb shell df -h
a=$(adb shell df -h)
echo $a
