#!/bin/bash

app_path="$(adb shell pm path com.linkedin.audiencenetwork.testapp | sed 's/package://' | sed 's/base\.apk$//')"

user_data="$(adb shell "run-as com.example.breach du /data/data/com.example.breach" | awk '{$1=$1}1' | grep -w /data/data/com.example.breach | awk '{print $1}')"

app_data="$(adb shell "run-as com.example.breach du $app_path" | grep -w "$app_path" | awk '{print $1}' )"

total_app_usage=$(( user_data + app_data ))

echo "total app usage = $(( total_app_usage/1024 )) KB"
