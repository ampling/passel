#! /user/bin/env python3
#
# Copycenter [2015-08-06], ISC, [Ampling] 


import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("entry", help="Sends the protected entry to Xclip",
            type=str)
    args = parser.parse_args()
    
    entry_list = list(str(args.entry))
    entry_count = (len(entry_list))

    print(entry_list[entry_count - 1])


if __name__ == '__main__':
    main()
