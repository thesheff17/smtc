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

"""Python classes"""

#this will attempt to teach you how classes work.  Every developer 
#has their own idea what a class does or an explination of what it is.
#My take on a class is a collection of code snippets that relates to each other.

#I will try to explain things as I write the class code. 
#ALL your programs should be classes from this point forward.
#if you are not writing your code in a class you are being lazy. Regardless of
#programming language.

import sys
import os

os.system("clear")

def screenClear():
    raw_input("press enter to continue.")
    os.system("clear")

#lets create a class to store my pet names.
#all classes begin with an uppercase letter
#the only reason I'm using a number in the class name is to seperate out each class examples.
class Pets1:
    
    #all classes start with a constructor
    #a constructor contains variables that need to be accessed by all methods
    
    def __init__(self):        
        #lets make a list to store our pets.  
        #You use self before the variable name in classes
        self.cats = ['Jabba', 'Egon']
        self.dogs = ['Comet', 'Roo', 'Felix']
        
    #now lets write our first method
    # method to print our pets
    def printPets(self):
        #variables that start with self. will be available in all methed
    
        print "I have " + str(len(self.cats)) + " cats."
        print "The names are:"
        for each in self.cats:
            print each
        
        print ""
        
        print "I have " + str(len(self.dogs)) + " dogs."
        print "The names are:"
        for each in self.dogs:
            print each
            
#now that we have our basic first class lets make it add/delete pets:
class Pets2:
    
    #all classes start with a constructor
    #a constructor contains variables that need to be accessed by all methods
    
    def __init__(self):
        
        #lets make a list to store our games.  
        #You use self before the variable name in classes
        self.cats = ['Jabba', 'Egon']
        self.dogs = ['Comet', 'Roo', 'Felix']
        
    def printPets(self):
        
        print "I have " + str(len(self.cats)) + " cats."
        print "The names are:"
        for each in self.cats:
            print each
        
        print ""
        
        print "I have " + str(len(self.dogs)) + " dogs."
        print "The names are:"
        for each in self.dogs:
            print each
            
    def addDog(self, name):
        self.dogs.append(name)
        print "dog name " + name + " added to list"
        
    def removeDog(self, name):
        self.dogs.remove(name)
        print "dog name " + name + " removed to list"
        
    def addCat(self, name):
        self.cats.append(name)
        print "cat name " + name + " added to list"
        
    def removeCat(self, name):
        self.cats.remove(name)
        print "cat name " + name + " removed to list"
        
        
#You can also pass items into the constructor
class Pets3:
    
    #all classes start with a constructor
    #a constructor contains variables that need to be accessed by all methods
    def __init__(self, dogName):
        
        #lets make a list to store our games.  
        #You use self before the variable name in classes
        self.cats = ['Jabba', 'Egon']
        self.dogs = ['Comet', 'Roo', 'Felix']
        self.dogName = dogName
        
        #add it to the list
        self.dogs.append(self.dogName)
        
    def printPets(self):
        
        print "I have " + str(len(self.cats)) + " cats."
        print "The names are:"
        for each in self.cats:
            print each
        
        print ""
        
        print "I have " + str(len(self.dogs)) + " dogs."
        print "The names are:"
        for each in self.dogs:
            print each
            
            
#You can also pass items into the constructor
class Pets4:
    
    #all classes start with a constructor
    #a constructor contains variables that need to be accessed by all methods
    def __init__(self):
        
        #lets make a list to store our games.  
        #You use self before the variable name in classes
        self.cats = ['Jabba', 'Egon']
        self.dogs = ['Comet', 'Roo', 'Felix']
        
    def printPets(self):
        
        print "I have " + str(len(self.cats)) + " cats."
        print "The names are:"
        for each in self.cats:
            print each
        
        print ""
        
        print "I have " + str(len(self.dogs)) + " dogs."
        print "The names are:"
        for each in self.dogs:
            print each
            
    #this will deault to the dogName Buddy otherwise pass your own name
    def addDog(self, dogName = 'Buddy'):
        self.dogs.append(dogName)
            
            
#This is a special if statement that says:
#are you calling this script directly if so run this code.
#I can't explain this anymore.  If you want to read more about this visit
#http://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == "__main__":
    
    #I print out when I star/end my scripts.
    print "108-classes.py started."
    
    #pets1 example:
    #first thing you want to do is create a variable point at your new class
    print "Example 1 of class Pets1"
    myPets1 = Pets1()
    
    #now lets print out my pets
    myPets1.printPets()
    screenClear()
    
    #pets2 example:
    myPets2 = Pets2()
    
    #print out pets
    print "Example 2 of class Pets2"
    myPets2.printPets()
    screenClear()
    
    #now lets add/remove some
    myPets2.addDog("Buddy")
    myPets2.removeDog("Roo")
    myPets2.addCat("Ozzy")
    myPets2.addCat("Paws")
    screenClear()
    
    #print out pets
    myPets2.printPets()
    screenClear()
    
    #you can easily have two variables using the same class
    myPets2a = Pets2()
    myPets2b = Pets2()
    
    myPets2a.removeDog("Roo")
    myPets2b.addDog("Buddy")
    screenClear()
    
    #print out myPets2a
    print "printing out myPets2a pets"
    myPets2a.printPets()
    screenClear()
    
    #print out myPets2b
    print "printing out myPets2b pets"
    myPets2b.printPets()
    screenClear()
    
    #pet3 example
    myPets3 = Pets3("Buddy")
    print "printing out myPets3 pets"
    myPets3.printPets()
    screenClear()
    
    #pet4 example
    myPets4 = Pets4()
    myPets4.addDog()
    myPets4.addDog("Sparky")
    print "printing out myPets4 pets"
    myPets4.printPets()
    screenClear()
    
    #print the script is done.
    print "108-classes.py completed."