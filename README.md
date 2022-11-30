#Key Logger

#Purpose of this Key Logger

This key logger is created for a project from Cyber Project with unintentional malicious use.

#To Create the Project

- import pynput.keyboard (Class to monitor the keyboard)
https://pynput.readthedocs.io/en/latest/

- import threading 
https://docs.python.org/3/library/threading.html

- import smtplib (Class to send email)
https://docs.python.org/3/library/smtplib.html

#Feature

- Store log locally (Local keyloggers)
- Report logs to email or remote server (remote keyloggers)
- Log screenshots
- Start with system startup

#How to create email to use for sending report

- Use an email that is not use for personal stuff (recommended)
- Using email password in the code is not recommend
- Use password from "App Password" in your email account
- From your gmail account -> go to "Security" -> enable 2-factor authentication -> Choose "App password"
- Generate App Password by selecting "Select App" and choose "Custom"

#How Does the Project Work

- Activate the python file
- The program record the key that is pressed
- Send a report through email in a custom time

#Limitation

- Kali Linux is supported
- MAC/Window got blocked
- MAC/Window Virtual Machine (unknown)
