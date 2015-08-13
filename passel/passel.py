#! /user/bin/env python3

##############################################################################
#
# Copycenter (c) [2015-08-06], ISC, [Ampling]
#
##############################################################################
""" Passel 

Passel is a friendly command-line password selection interface
for people with a lot of digital credentials.
"""

from subprocess import call, Popen, PIPE
from glob import glob
import argparse
import gpgme


# CONFIGURABLE {
# Password Files:-$HOME/
PASSWORD_STORE_DIR = '.password-store/test'
# Let pass handle gpg
use_Pass = 1
#}

# global variables #{
home = os.path.expanduser("~")
store = home + "/" + PASSWORD_STORE_DIR + "/"
#}

#
# BEGIN helper functions
#

#{ shell to Xclip
def _copyXclip(text):
        p = Popen(['xclip', '-selection', 'c', '-l', '1', '-quiet'], stdin=PIPE,
                close_fds=True)
        p.communicate(input=text.encode('utf-8'))
#}

#{ shell to pass
def _pass(text):
        p = Popen(['pass', ''], stdin=PIPE,
                close_fds=True)
        p.communicate(input=text.encode('utf-8'))
#}



#
# BEGIN platform definable
#

#entry
def entry(): #{
    global entry_file
    for file in entry_file:
        global path
        names = glob(store+"/"+file+"*.gpg")
        global name
        name = names[0]
        reclip()
#}

#reclip it
def reclip(): #{
    global store
    global name
    afile = name.replace(store, '', 1)
    os.environ['afile'] = afile
    _copyXclip(afile)
#}


#{ Define Options
def main():
    parser = argparse.ArgumentParser(description='Select some files', prog='passel')
    parser.add_argument("entry", help="Sends the entry to Xclip",
            type=str)
    #parser.add_argument("path", "path",help="path/to/file",
    #        type=str)
    args = parser.parse_args()
    
    global entry_file
    entry_file = list(str(args.entry))
    

    #entry_count = (len(entry_file))
    #print(entry_file[entry_count - 1])
#}

if __name__ == '__main__':
    main()
    entry()
