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

"""Python dictionary.py or dict/sets"""

# I won't make this a class for this.  I will just show the dict example.
# dict is an object that contains a list of two data sets.  The first item
# is always unique.  The second item contains data that relates to the first item.

# I had to build redirects for mlb teams based on devision.
#Here is an example of a dictionary 

from collections import OrderedDict

print "109-dictionary.py started."

teams = {'angels': '2013-alds',
         'astros': '2013-nlds',
         'athletics': '2013-alds',
         'blue-jays': '2013-alds',
         'braves':'2013-nlds',
         'brewers':'2013-nlds',
         'cardinals':'2013-nlds',
         'cubs':'2013-nlds',
         'diamondbacks':'2013-nlds',
         'dodgers':'2013-nlds',
         'giants':'2013-nlds',
         'indians':'2013-alds',
         'mariners':'2013-alds',
         'marlins':'2013-nlds',
         'mets':'2013-nlds',
         'nationals':'2013-nlds',
         'orioles':'2013-alds',
         'padres':'2013-nlds',
         'phillies':'2013-nlds',
         'pirates':'2013-nlds',
         'rangers':'2013-alds',
         'rays':'2013-alds',
         'red-sox':'2013-alds',
         'reds':'2013-nlds',
         'rockies':'2013-nlds',
         'royals':'2013-alds',
         'tigers': '2013-alds',
         'twins':'2013-alds',
         'white-sox': '2013-alds',
         'yankees': '2013-alds'}

#sorts the dictionary.  Only exists in python 2.7.x and newer
sortedTeams = OrderedDict(sorted(teams.items(), key=lambda x: x[0]))

for teamName, division in sortedTeams.items():
    print "The team: " + teamName + " belongs to " + division + " divsion."

print "109-dictionary.py Completed."
