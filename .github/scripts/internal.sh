#!/bin/bash

user_data_path="/data/data/com.linkedin.audiencenetwork.testapp/"
app_path=$(adb shell pm path com.linkedin.audiencenetwork.testapp | sed 's/package://' | sed 's/base\.apk$//')

user_data=$(adb shell "run-as com.linkedin.audiencenetwork.testapp du $user_data_path" | grep -w $user_data_path | awk '{print $1}')

app_data=$(adb shell "run-as com.example.breach du $app_path" | grep -w "$app_path" | awk '{print $1}')

echo "User data = $user_data"
echo "App data = $app_data"
total_app_usage=$((user_data + app_data))

echo "total app usage = $(( total_app_usage/1024 )) MB"
