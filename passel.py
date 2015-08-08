#! /user/bin/env python3
#
# Copycenter [2015-08-06], ISC, [Ampling] 


import argparse
from glob import glob
import subprocess
import os
import sys


# CONFIG
PASSWORD_STORE_DIR = '.password-store/'

# global veriables
home = os.path.expanduser("~")
store = home + "/" + PASSWORD_STORE_DIR


#loop
def loop(): #{
    global entry_list
    for file in entry_list:
        global path
        names = glob(store+"/"+file+"*")
        global name
        name = names[0]
        clip()
#}

# shell magic
def clip(): #{
    global store
    global name
    afile = name.replace(store, '', 1)
    os.environ['afile'] = afile
    print(afile)
    #subprocess.call('pass $afile | xclip -l 1 -quiet -selection clipboard',shell=True)
#}


# Define Options
def main(): #{
    parser = argparse.ArgumentParser(description='Select some files')
    parser.add_argument("entry", help="Sends the entry to Xclip",
            type=str)
    #parser.add_argument("path", "path",help="path/to/file",
    #        type=str)
    args = parser.parse_args()
    
    global entry_list
    entry_list = list(str(args.entry))
    


    #entry_count = (len(entry_list))
    #print(entry_list[entry_count - 1])
#}

if __name__ == '__main__':
    main()
    loop()
