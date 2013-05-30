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

"""My atttempt to teach you python 2.x"""

# This is a comment line.  These lines do not run but provide information.

#These import statements are part of the python language
#These should be at the top of all python programs.
import sys
import os

os.system("clear") # clears the screen
print 'This program will attempt to teach you python 2.x.  Created by Dan Sheffner.' #tells you who I am, and also allow in line comments.
print 'email me at dan @ sheffner dot com' #my email

raw_input("press enter to continue") #waits for you to hit enter
os.system("clear")

print "You shold print this file on a color printer with line numbers."
print "A good windows text editor is notepad++ http://notepad-plus-plus.org/"
raw_input("press enter to continue.")
os.system("clear")

print "Programmers say show me the code. So here it is..."
print "Some things to remember while programming in python."
print "1) Take your time."
print "2) Google search is your friend."
print "3) Offer recommendations to this program."
print "4) Good luck"

raw_input("press enter to continue.")
os.system("clear")

print "Every person should be able to print hello world to the screen in the program language they are using."
raw_input("press enter to continue.")
os.system("clear")

print "All print statements are wrapped in double quotes."
print "hello world"
os.system("clear")

print "A couple things you should know before you start to program in python."
raw_input("press enter to continue.")
os.system("clear")

print 'python does not care about empty lines.  Use as many as you would like.'
raw_input("press enter to continue.")
os.system("clear")

print "Python relies on the tab key instead of using any brackets{} like other programming languages."
print "If this is your first programming language then don't worry.  Keep reading."
raw_input("press enter to continue.")
os.system("clear")

print "tabs will define logic on what code runs."
print "An if & else statement example:"
print "if 10 > 5:"
print '    print "10 of course is greater then 5 and so this line runs."'

raw_input("Now for it run in the code. press enter to continue.")
os.system("clear")
if 10 > 5: # 10 will always be greater then 5
    print "10 of course is greater then 5 and so this line runs."
    print "this line runs because its tabbed over and is line with the previous statement."
else:      # else part
    print "This line will never run because 10 will never be greater then 5."
raw_input("press enter to continue.")
os.system("clear")

print "This line is not tabbed over and will always run."
raw_input("press enter to continue.")
os.system("clear")

print "Your around 100 lines of code so far. Need a break?"
print "o.k. Now for some harder code."
raw_input("press enter to continue.")
os.system("clear")

print "From this point forward examples will only exist in the code."
print "Don't worry just keep reading the script and you will do fine."
raw_input("press enter to continue.")
os.system("clear")

#variables, if statement, and using a boolean variable (True/False)
#True/False are special key words just like print that provide logic
doYouUnderstandPython = True

if doYouUnderstandPython == True: #is the variable True?
    print "Good to hear."
else:
    print "hmm...maybe you should review the code again."

raw_input("press enter to continue")
os.system("clear")

# FUNCTIONS

#as you can see there is a number of lines that are already duplicated.
#for example line 95 is the same as 100 and 96 is the same as 101.
#lets fix that with a function:
def screenClear():
    raw_input("press enter to continue.")
    os.system("clear")


#now instead of calling two lines we can just call one to run lines 126 & 127
print "now to call our new function"
screenClear()

print "You can call it as many times as you want"
print "once:"
screenClear()
print "twice:"
screenClear()
print "and so on"
screenClear()

#FUNCTIONS with parameters passed (params)
def sayHello(name):
    print "Hello " + name + " How are you doing?"

sayHello("Laura")
sayHello("Dan")
sayHello("Chris")
screenClear()

#IF, ELIF, ELSE statements.
#Many programming laungages call this a case statement
def privateMessage(name):
    if name == "Laura":
        print name + " do you want to go shopping?"
    elif name == "Chris":
        print name + " do you want to play some basketball?"
    else:
        print name + " do I know you?"

privateMessage("Laura")
privateMessage("Chris")
privateMessage("Dan")
screenClear()

#everything in ptyhon is an object.  You can see what the object is by using the below code:
myNewString = "Dan Sheffner"
print "The type of myNewString variable is: " + str(type(myNewString)) + "."
screenClear()

myNewInteger = 5
print "The type of myNewInteger variable is: " + str(type(myNewInteger)) + "."
screenClear()

myNewBoolean = True
print "The type of myNewBoolean variable is: " + str(type(myNewBoolean)) + "."
screenClear()

print "Continue on with python2/102-string.py tutorial."
print "python2-101.py completed."
