#!/usr/bin/expect -f

spawn sdkmanager --licenses

# Expect the prompt for accepting the licenses and send "y" for each one
expect {
    "Accept? (y/N)" {
        send "y\r"
        exp_continue
    }
    eof
}

exit
