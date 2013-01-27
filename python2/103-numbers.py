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

"""How to use numbers in python"""

import os

def screenClear():
    raw_input("press enter to continue.")
    os.system("clear")
    
os.system("clear") # clears the screen 
print '102-strings.py created by Dan Sheffner.' #tells you who I am, and also allow in line comments.
print 'email me at dan @ sheffner dot com' #my email

#integers are numbers that don't have a decimal point.
addition = 5 + 5

#You should only print out string types. So lets convert an integer to string with str()
#I know that print addition works without str().  Don't worry about this write now.
print str(addition)
screenClear()

#DOUBLES and covert doubles to STRING with str(variable)

#doubles contain decimal points
addMyMoney = 10 + 5.52

print "You have $" + str(addMyMoney) + " dollars."
screenClear()

#converting STRINGS TO INTEGERS with int(variable)
myString = "10"

howOldIsSheFiveYearsFromNow = int(myString) + 5
print "She is " + str(howOldIsSheFiveYearsFromNow) + " years old."
screenClear()

print "Continue on with python2/104-lists.py tutorial."
print "103-numbers.py completed."