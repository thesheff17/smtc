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

"""How to use strings in python"""

import os

def screenClear():
    raw_input("press enter to continue.")
    os.system("clear")
    
os.system("clear") # clears the screen 
print '102-strings.py created by Dan Sheffner.' #tells you who I am, and also allow in line comments.
print 'email me at dan @ sheffner dot com' #my email


#anything wrapped in quote marks are called strings.
#many times you will have two strings and you want to print it in a sentance.
#a plus symbol + is used to do this
firstName = "Dan"
lastName = "Sheffner"

print "My Name is " + firstName + " " + lastName 
screenClear()

#check the length of any string
print "The length of string firsName is: " + str(len(firstName))
screenClear()

#many times strings will cotain white spaces you don't want."
spacedString = "         Hello World.               "
print "To remove spaces from a string use strip: " + spacedString.strip()
print "Without the spaces removed: " + spacedString
screenClear()

#uppercase letters
print "uppercase letters with .uppercase()."
print firstName.upper()
screenClear()

#lowercase letters
print "lowercase letters with .lowercase()"
print firstName.lower()
screenClear()

#printing a subset of a string.  Strings start with a 0 index.
print "Use stringName[start:end] to print substrings: " +  lastName[0:5]

#printing a subset of a string going backwards.
print "Use stringName[-Number] to print substrings: " +  lastName[-3]
screenClear()

#find a string in a string with string.find() 
#find will return -1 if it doesn't find it.
#otherwise it will return the position it found it at.
if lastName.find('Sheff') >= 0: # 
    print "Sheff is a substring of " + lastName + " and found at position: " + str(lastName.find('Sheff'))
    

if lastName.find("ner") >= 0:
    print "ner is a substring of " + lastName + " and found at position: " + str(lastName.find("ner"))
screenClear()

#replace strings
print "replace all e's with capital A's in a string: " + lastName.replace("e","A")
screenClear()

# line breaks in strings
print "This will print on the first line.\nThis will be on the second line."
screenClear()

#if statement using a string:
if firstName == "Dan":
    print "firstName variable is Dan"
screenClear()

#another way to use an if statement
if "Sheff" in lastName:
    print "Sheff contained in " + lastName
screenClear()

if "bla" not in lastName:
    print "bla is not in " + lastName
screenClear()

#string can span multiple lines by using triple quotes
myBook = """The quick brown fox jumps
over the lazy dog.
"""

print myBook
screenClear() 

#raw_input wil always return a string
print "How old are you?"
age = raw_input("enter your age\n")

print "Your age is " + age + "."
screenClear()

print "Continue on with python2/103-numbers.py tutorial."
print "102-strings.py completed."