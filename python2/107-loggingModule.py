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

"""how to use the logging module"""

#you should know what you programs are doing at all times.
#use the linux command: tail -f log.log to watch as your programs works.

import logging
import time

#a bunch of stuff you don't really need to worry about except log.log
#log.log is the name of the file this information is going to be going to
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler('log.log')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(filename)s - %(funcName)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

#now just start logging where need
event = True
if event == True:
    logger.info("The event was True")
    
logger.info("Ran this line outside the loop")

x = 0
while x < 5:
    logger.info("The value of x is: " + str(x))
    x += 1

#figuring out when stuff start/stops
logger.info("started process x")
print "run run run"
time.sleep(3)
print "run run run"
time.sleep(3)
logger.info("completed process x")

#logging errors
if event <> False:
    logger.error("event does not equal False.  Logging error")

print "Continue on with python2/108-classes.pytorial."
print "106-sysTryModule.py completed."
