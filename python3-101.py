#!/usr/bin/en python3
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

#this is going to my best attemtpt get your feet wet with python3.x
#This is how comments are written.  
#These statemenets do not run but provide explanation

#These import statements are part of the python language
#they always exist at the top of any python script.
import sys
import os

os.system("clear") # clears the screen 
print ('This program will attempt to teach you python.  Created by Dan Sheffner.') #tells you who I am
print ('email me at dsheffner @ gmail dot com') #my email

input("press enter to continue.") #waits for you to hit enter
os.system("clear")

print ("I recommendation you print this on a color printer with line numbers.")
print ("A good windows text editor is notepad++ http://notepad-plus-plus.org/")
input("press enter to continue.")
os.system("clear")

print ("I don't know you but so many people had said show me the code so... Here it is:")
print ("Good luck, take your take your time, and offer recommendations.")
input("press enter to continue.")
os.system("clear")

print ("Every person should be able to print hello world to the screen in the program language they are using.")
input("press enter to continue.")
os.system("clear")

print ('all print statements are wrapped in print("string") No exceptions.')
print ('example print ("Hello world")')
print ('')
print ('Example running in code')
print ("hello world")
print ("hello world","today")
input("press enter to continue.")
os.system("clear")

print ("Are you following along in a python command prompt testing print?")
print ("The only way to learn python is doing it youself.")
print ("If you need more help installing python3 please visit python.org. or http://github.com/thesheff17/smtc/")
input("press enter to continue.")
os.system("clear")

print ("A couple things you should know before you start to program in python.")
print ("Are you ready to read for about 5 min but maybe think for 30 min?")
input("press enter to continue.")
os.system("clear")

print ('python does not care about empty lines.  Use as many as you would like.')
input("press enter to continue.")
os.system("clear")

print ("python heavily relies on the tab key INSTEAD of using any brackets/parathethese()/{} like other programming languages.")
print ("If this is your first programming language then don't worry.  Keep reading.")
input("press enter to continue.")
os.system("clear")

print ("tabs will define logic on what code runs.")
print ("an if statement example:")
print ("if 10 > 5:")
print ('    print ("10 of course is greater then 5 and so this line runs.")')


if 10 > 5: # 10 will always be greater then 5
    print ("10 of course is greater then 5 and so this line runs.")
    print ("this line runs because its tabbed over.")
else:
    print ("This line will never run because 10 will never be greater then 5.")

print ("This line is not tabbed over and will always run.")
input("press enter to continue.")
os.system("clear")

print ("Your about 100 lines in of the code. Need a break?")
print ("ok some harder stuff.")
input("press enter to continue.")
os.system("clear")

print ("lets learn about functions.  Functions are code we can call more then once.")
print ("so we don't have to keep copying/pasting code all the time.")
input("press enter to continue.")
os.system("clear")

print ("From this point forward examples will only exist in the code.")
print ("Don't worry just keep reading the script and you will do fine.")
input("press enter to continue.")
os.system("clear")

#FUNCTION

#as you can see there is a number of lines that are already duplicated.
#for example line 104 is the same as 109 and 105 is the same as 110.
#lets fix that with a function:
def screenClear():
    input("press enter to continue.")
    os.system("clear")
    
#You should see python 3.x here.  if you don't change your editor to this version
#or just run it from the command line with python3 python3.py
print ('printing the variable sys.version will tell you the version of python you are using.')
print ("don't worry about the GCC version")
print ('')
print(sys.version)
screenClear()  #are first example of calling our new function! Sweet no more copy paste.

#This should produce "first name middle name last name"  
#If you see ('first name','mdiddle name','last name') 
#you are still using python 2.x
print ("adding string together with the print statement")
print  ('example: print ("cat", "went to the house to see the", "dog")')
print ('\n')
print("first name", "middle name", "last name")
screenClear()

#from this point forward I'm not going to provide print examples.
#The examples of what it describes in represented in the code.

#string to int, int to string
print ('Many times you will have to convert data types to other data types.')
print ('The most common example is string to integer and integer to string')
print ('age is a string and we convert it to an int to get newAage')
age = "45"
newAge = int(age) + 5
print (str(newAge))
screenClear()

#all of python is simply refrence of an object = value
#basic examples
print ('All objects in python are object = value')
print ('you can always check the python type with type()')
firstName = "Dan"
lastName = "Sheffner"
age = 30
print (firstName, lastName, "is",age,"years old!")
print ('The data type of firstName is:',type(firstName))
print ('The data type of lastName is:', type(lastName))
print ('The data type of age is:', type(age))
screenClear()

#I feel this section is too obstract fo a new user so  I removed it for now
###refrence object to refrence object
##print ('in python objects can have the same pointer to a value.')
##a = 3
##b = a
##
##print ("a value is:",a)
##print ("b value is:",b)
##a = a - 1
##print ("a value is:",a)
##print ("b value is:",b)
##screenClear()


# more data types

#tuples are immutable so once they are created they cannot be changed
#list are mutable so they can be changed
#use tuples are faster then lists

print ('tuples are a data types that cannot be changed(immutable) and use parentheses ()')
print ("tuples should be used if you don't need to change the data")
print ('also feel free to know when your loops start finish with a print statements below')
#tuple
animals = ('dog', 'cat', 'bird')
print ("for loop started\n")
for pet in animals:
    print (pet)
print ("for loop finished\n")
#len
print ("length of animal tuple is:",len(animals))
#class
print ("the class of animals is:",type(animals))
screenClear()

#lists data types
print ('lists are a data types that can be changed(mutable) and use brackets []')
print ("lists should when you need to change the  data")
animals2 = ['dog', 'cat', 'bird']
print ('animals2 list:')
for pet in animals2:
    print (pet)
    
list.append(animals2,"fish")

print ('animals2 list with fish appended:')
for pet in animals2:
    print (pet)
    
print ("length of animal2 list is:", len(animals2))
print ("the class of animals2 is:", type(animals2))
screenClear()


#mutiple datatypes in a list
print ('tuples and list can support multiple data types.')
newList = []
list.append(newList, 45)
list.append(newList,"String")

for dataType in newList:
    print ("data type is:", type(dataType))
screenClear()


#I feel this section is too obstract fo a new user so  I removed it for now      
###does a data type refrence another data type in memory
##a = 5
##b = a
##
##if a == b:
##    print ("True both a & b point at the same memory slot")
##else:
##    print ("False both a & b do not point at the same memory slot")
##    
##a = 5
##b = a - 1
##
##if a == b:
##    print ("True both a & b point at the same memory slot")
##else:
##    print ("False both a & b do not point at the same memory slot")

    
#basic comparison operators
#<=, !=, >=, >, <, ==
print ('basic comparison operations <=, !=, >=, >, <, ==')
age = 30
if age >= 30:
    print ('You are old')
screenClear()   

    
print ('the in command inside an if statement')
animals2 = ['dog', 'cat', 'bird']
if 'dog' in animals2:
    print ('found dog in the list')
screenClear()
    
# "not" in if statement
print ('the not command inside an if statement and then we add it')
print ('then I show you the list')
if not 'fish' in animals2:
    print ("fish is not in the list.  Adding fish to the list...")
    list.append(animals2,"fish")

for each in animals2:
    print (each)
screenClear()

print ('logical operators and, or, not and another example of a function')
age = 30
numOfYearsFriends = 5
if age >= 30 and numOfYearsFriends > 3:
    print ("You have been friends a long time")
    
#if, elif, else, function
def checkValue(x):
    if x == 5:
        print ("1st case")
        print ("x is:", x)
    elif x == 4:
        print ("2nd case")
        print ("x is:", x)
    else:
        print ("3rd case")
        print ("x is:", x)
    
checkValue(5)
checkValue(4)
checkValue(10)
screenClear()

#while statements, break, usually coninue isn't need since break is in an
#if statement.
print ('while statements')
x = 1
while True:
    x += 1
    if x == 10:
        print ("x reached 10 quiting...")
        break
    else:
        continue

screenClear()   
    
#exception handling.  When python errors out and we want to continue
print ('basic input from the console.')
print ('also shows you how to do a try except to bypass errors in python')
s = input("Please enter your age: ")
try:
    i = int(s)
except ValueError as err:
    print (err)
screenClear() 

# of course basic math works
print ('basic math')
x = 25/5
print (str(x))
print ("x data type is:", type(x))

print (str(10+10))
screenClear() 

#special addition syntax
print ('special addition syntax for integers')
print ("while loop started")
x = 1
while (x is not 50):
    x += 1
print ("while loop finished")
screenClear() 

#special addition syntax with lists
print ('special addition synatx for lists')
pets = []
pets += ['dog']
print ("The pets list now has an entry on it:",pets)
pets += ['cat']
print ("Then we added another:",pets)
screenClear()

#getting params from the command line
print ("I will just use an example here so this script doesn't fail")
print ('example: input1 = sys.argv[1]')
screenClear()

#output all the classes/methods of a module
print ('we can print out the class methods')
print (dir(sys.argv))
screenClear()

