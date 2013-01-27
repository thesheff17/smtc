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

#this is going to my best attemtpt get your feet wet with python 2.x
#This is how comments are written.  
#These statemenets do not run but provide explanation

#These import statements are part of the python language
#they always exist at the top of any python script.
import sys
import os

os.system("clear") # clears the screen 
print 'This program will attempt to teach you python.  Created by Dan Sheffner.' #tells you who I am, and also allow in line comments.
print 'email me at dsheffner @ gmail dot com' #my email

raw_input("press enter to continue") #waits for you to hit enter
os.system("clear")  

print "I recommendation you print this on a color printer with line numbers."
print "A good windows text editor is notepad++ http://notepad-plus-plus.org/"
raw_input("press enter to continue.")
os.system("clear")

print "I don't know you but so many people had said show me the code... So here it is:"
print "Good luck, take your take your time, and offer recommendations."
raw_input("press enter to continue.")
os.system("clear")

print "Every person should be able to print hello world to the screen in the program language they are using."
raw_input("press enter to continue.")
os.system("clear")

print "all print statements are wrapped in double quotes."
print ("")
print "hello world"
os.system("clear")

print "Are you following along in a python command prompt testing print?"
print "The only way to learn python is doing it youself."
print "If you need more help installing python3 please visit python.org. or http://github.com/thesheff17/smtc/"
raw_input("press enter to continue.")
os.system("clear")

print "A couple things you should know before you start to program in python."
print "Are you ready to read for about 5 min but maybe think for 30 min?"
raw_input("press enter to continue.")
os.system("clear")

print 'python does not care about empty lines.  Use as many as you would like.'
raw_input("press enter to continue.")
os.system("clear")

print "python heavily relies on the tab key INSTEAD of using any brackets/parathethese()/{} like other programming languages."
print "If this is your first programming language then don't worry.  Keep reading."
raw_input("press enter to continue.")
os.system("clear")

print "tabs will define logic on what code runs."
print "an if else statement example:"
print "if 10 > 5:"
print '    print "10 of course is greater then 5 and so this line runs."'

raw_input("Now for it run in the code. press enter to continue.")
os.system("clear")
if 10 > 5: # 10 will always be greater then 5
    print "10 of course is greater then 5 and so this line runs."
    print "this line runs because its tabbed over and is line with the previous statement."
else:
    print "This line will never run because 10 will never be greater then 5."
    
print "This line is not tabbed over and will always run."
raw_input("press enter to continue.")
os.system("clear")

print "Your about 100 lines in of the code. Need a break?"
print "ok some harder stuff."
raw_input("press enter to continue.")
os.system("clear")



print "lets learn about functions.  Functions are code we can call more then once."
print "so we don't have to keep copying/pasting code all the time."
raw_input("press enter to continue.")
os.system("clear")

print "From this point forward examples will only exist in the code."
print "Don't worry just keep reading the script and you will do fine."
raw_input("press enter to continue.")
os.system("clear")

#VARIABLES and another example of an if statement
doYouUnderstandPython = True

if doYouUnderstandPython == True:
    print "Good to hear."
else:
    print "hmm...maybe you should review the code again"
    
raw_input("press enter to continue")
os.system("clear")

# FUNCTIONS

#as you can see there is a number of lines that are already duplicated.
#for example line 95 is the same as 100 and 96 is the same as 101.
#lets fix that with a function:
def screenClear():
    raw_input("press enter to continue.")
    os.system("clear")
    
    
#now instead of calling two lines we can just call one to run lines 118 & 119
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

# STRINGS

#anything wrapped in quote marks are called strings.
#many times you will have two strings and you want to print it in a sentance.
#a plus symbol + is used to do this
firstName = "Dan"
lastName = "Sheffner"

print "My Name is " + firstName + " " + lastName 
screenClear()

#INTEGERS and convert INTEGERS to STRING with str(variable)

#integers are numbers that don't have a decimal point.
addition = 5 + 5

#You should only print out string type. So lets convert an integer to string with str()
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

#Checking the TYPE of the variables you use type(variable)
myNewString = "Dan Sheffner"
print "The type of myNewString variable is: " + str(type(myNewString)) + "."
screenClear()

myNewInteger = 5
print "The type of myNewInteger variable is: " + str(type(myNewInteger)) + "."
screenClear()


print "