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

"""How to use loops & Lists in python"""

import os
import time

os.system("clear")

def screenClear():
    raw_input("press enter to continue.")
    os.system("clear")
    

#my friends list
friends = ["Chris","Dan","Laura"]

#you can also append values to a list
friends.append("Becky")

#for loop
for each in friends:
    print each 
screenClear()

# if we want to know the index during for loop    
for index, each in enumerate(friends):
    print "index is: " + str(index) + " name is:" + each
screenClear()

#go through a range of numbers
for number in range(0,25):
    print str(number)
screenClear()

#sometimes you need an endless loop that does something
#you should always build in sleep time in seconds at the end.
#if you don't add time.sleep(3) the script will consume 100% of 1 CPU.
x = 0
y = 3

while 1==1:
    x += 1
    if x > y:
        print "x reached 3 breaking loop out."
        break
    
    print "sleep for 3 seconds"
    time.sleep(3)
    
screenClear()

#list can be different types (string and integers mixed)
list1 = ["Dan", 5, "Laura", 10]

for each in list1:
    if isinstance(each, int):  #This line checks to see if it is an integer.
        print str(each + 5)
    else:                      #otherwise just print the name which is a string
        print each
        
print "Continue on with python2/105-osModule.py tutorial."
print "104-listLoops.py completed."