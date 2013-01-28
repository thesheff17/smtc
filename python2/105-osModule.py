#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Copyright (c) Digital Imaging Softawre Solutions, INC 
# Dan Sheffner Dan@Sheffner.org
# All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish, dis-
# tribute, sublicense, and/or sell copies of the Software, and to permit
# persons to whom the Software is furnished to do so, subject to the fol-
# lowing conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
# OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABIL-
# ITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
# SHALL THE AUTHOR BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

"""how to use the os & commands module"""

# os module is a little old but can still be used.
import os # Miscellaneous operating system interfaces http://docs.python.org/2/library/os.html
import commands

os.system("clear")

#we have been using it all a long here.  This is actually calling the 
#linux prompt with clear.  
def screenClear():
    raw_input("press enter to continue.")
    os.system("clear")
    
#you can even go one step further to get a string of the output
#this ls the /home/ directory
print "what files are located in /usr/local/ using the linux command ls"
files = commands.getoutput("ls /usr/local/")
print files
screenClear()
    
#os can do other things like check if files exist
#this will of course only work on linux machines
if os.path.isfile("/etc/passwd"):
    print "You have a password file"
else:
    print "You don't have a pasword file"
screenClear()
    
#check if a directory exists
if os.path.isdir("/home/"):
    print "you have a home directory"
else:
    print "you don't have a home directory"
screenClear()

print "Continue on with python2/106-sysModule.py tutorial."
print "105-osModule.py completed."