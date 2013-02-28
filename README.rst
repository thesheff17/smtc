####
smtc - show me the code
####

************
Introduction
************
This will teach you how to program in python.

*****************
python 2.7.x vs 3.x
*****************
Most of my time is spent in the 2.7.x code base due the modules I need.  Eventually
everything will be python 3.x compatible and I will use that.  Until then I use
2.7.x and higher.

************
Installation
************
    *Git is a piece of software you should store your code in.  If you have git installed on your machine you can do:
    * git clone git://github.com/thesheff17/smtc.git

operating system -
    * it doesn't matter what operating system you use but I would recommend http://ubuntu.com/ linux. 
    
linux/ubuntu -
    * python 2.7.x should be already on your system. You can check by typing python at the prompt. ctrl-D exits the python prompt.
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
    * extract smtcCygwin.zip to your C:\\ drive and run cygwin.bat
    * a black box should pop up. Switch to my home directory: cd /home/thesheff17/smtc/
    * update the git repository: git pull
    
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
    * python2/109-dictionary.py     - how to use dictionary/sets/hashes
    
* TO DO:
    * tutorial on how to submit changes in git
    * python2/datetimeModule.py  - how to use the datetime module
    * python2/django             - web framework
    * python2/pypy implimenation - http://pypy.org/
    * python2/sqlachemy          - http://www.sqlalchemy.org/
    * python2/unittest           - testing framework
    * python2/re module          - regex module for text searches
    * python2/MySQLdb            - direct MySQL db access
    * python2/excel write/read   - http://www.python-excel.org/
    * python/ec2                 - Amazon ec2 instances service through boto module
    * pytohn2/spot instances     - Amazon spot instance service through boto module
    * python/dynmodb             - Amazon dynmodb service through boto module
    * pyhon/elb                  - Amazon ELB(elastic load balancer) through boto module
    * python/rds                 - Amazon rds(MySQL servers) through boto module

* broken :-/
    * I tried to get cygwin working with easy_tools installing MySQL-python.  This failed for a number
      of reasons.  I tried installing some MySQL libraries as well gcc-core but still failed.
      I would love a patch for cygwin to work with the MySQLdb module otherwise just use linux.
    
* python 3.x 
    * python3-101.py                - first example of how to program in python 3.x
