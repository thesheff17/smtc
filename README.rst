####
smtc - show me the code
####

************
Introduction
************

This will attempt to teach you how to program in python.

************
Installation
************

* git clone git://github.com/thesheff17/smtc.git

os -
    * it doesn't matter what operating system you use but I would recommend http://ubuntu.com/ linux. 
    
linux/ubuntu -
    * python 2.x should be already on your system. You can check by typing python at the prompt. ctrl-D exits the python prompt.
    * install some extra packages at the command line: sudo apt-get install git-core gitk python-mysqldb spe

mac -
    * I don't use a mac.  Feel free to change this section.
    * python 2.7.x should be installed. http://www.python.org/getit/mac/
    * git http://git-scm.com/download/mac
    
windows -
    * I recommend either installing ubuntu on a virtual machine with virtualbox or use
    * http://ideone.com/ in the browser. Hello world example: http://ideone.com/52PbNB
    
windows pre configured cygwin download -
    * download https://s3.amazonaws.com/smtc/smtcCygwin.zip
    * extract smtcCygwin.zip and run cygwin.exe
    * update the git reporitory: cd smtc
    * git pull
    
windows emulating linux w/ cygwin -
    * download setup.exe from cygwin http://www.cygwin.com/
    * install Devel/git: Fast version control system - core files
    * install Python/python: Python language interpreter 
    * install Editors/vim: Vi Improved: echanced vi editor
    * install Net/openssh: The openSSH server and client programs
    * install Net/rsync: fast remote file transfer program (can use existing data to minimize transfer)
    * install Utils/Ncurses: Utilities for terminal handling
    
* python 2.x
    * python2-101.py                - first example of how to program in python 2.x
    * python2/102-strings.py        - more info on strings.
    * python2/103-numbers.py        - how to us numbers.
    * python2/104-listsLoops.py     - how to use list & loops
    * python2/105-osModule.py       - how to use the os module
    * python2/106-sysTryModule.py   - how to use the sys module & try/except Error handling
    * python2/107-loggingModule.py  - how to use the logging module
    * python2/108-classes.py        - how to use classes.
    
* TO DO:
    * python2/109-botoModule.py     - how to use the boto module https://github.com/boto/boto
    * tutorial on how to submit changes in git
    
* Wish list:
    * python2/datetimeModule.py     - how to use the datetime module
    * python2/dictionaries          - http://docs.python.org/2/tutorial/datastructures.html
    * python2/django                - web framework
    * python2/pypy implimenation    - http://pypy.org/
    * python2/sqlachemy             - http://www.sqlalchemy.org/
    
    * I tried to get cygwin working with easy_tools installing MySQL-python.  This failed for a number
      of reasons.  I tried installing some MySQL libraries as well gcc-core but still failed.
    
* python 3.x 
    * python3-101.py                - first example of how to program in python 3.x
