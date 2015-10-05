#!/bin/python
import os

#Set your bot token here
token = '123456789:ABCDe-11111111111111111111111111111'

#Set the user or group chat id here
chat_id = 123456789

#cd to the script's directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
