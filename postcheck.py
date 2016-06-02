#!/usr/bin/python3

import sys #for sys.stdin, sys.argv
import string #for string.punctuation
import argparse
from collections import Counter

def skip_header(file_to_read):
    '''Jekyll posts start with a header consisting of a block of stuff this program doesn't care about. This function skips over that part if it exists.'''
    started_header = False
    for line in file_to_read:
        if line.startswith('---'):
            if started_header == False:
                started_header = True
            else:
                break
    return file_to_read;
        


parser = argparse.ArgumentParser(description = "Find most used words and phrases in a Jekyll post.")
parser.add_argument('-w', nargs='?', default=5, const=None, type=int)
parsed_args = parser.parse_args();


post = skip_header(sys.stdin).read();

words = Counter(post.translate(str.maketrans("", "", string.punctuation)).lower().split()).most_common(parsed_args.w)

if parsed_args.w == None or parsed_args.w > len(words):
    start = "Word frequency"
else:
    start = "Top " + str(parsed_args.w) + " words"

print(start + " in post:")
print(words)

