#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# Copyright (c) Digital Imaging Software Solutions, INC
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

"""how to use the sys module and try/except error handling"""

#the sys module allows for passing arguments on the command line.
#this is why we also want to learn about try/except error handling.
#instead of python complaining about a user not passing it something
#lets help the script along and tell the user what to pass

import os
import sys

os.system("clear")

def screenClear():
    raw_input("press enter to continue.")
    os.system("clear")

try:
    
    #option now contains the first argument the user passed in
    option1 = sys.argv[1]
    
    if option1 == "runBackupScript":
        print "running the backup script for the new server."
        
    if option1 == "deploySoftware":
        print "deploying software to the new server."
        
    screenClear()
    
    print "You can also use as many sys.argv[x] as you need to read in any values to check."
    print "Always try to help the user out on what your script does."
    screenClear()
    
#catch the error and tell the user to pass it something.
except IndexError:
    print "You have to pass it one of two options."
    print "runBackupScript - runs the backup script"
    print "deploySoftware  - deployes the software"
    
print "Continue on with python2/107-loggingModule.py tutorial."
print "106-sysTryModule.py completed."