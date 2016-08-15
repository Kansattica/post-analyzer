#!/usr/bin/python3

import sys #for sys.stdin, sys.argv
import string #for string.punctuation
import argparse
from collections import Counter
from enum import Enum

class Options(Enum):
    top_words = 0
    top_phrases = 1
    to_filter = 2

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
        
def make_arg_dict():
    #Todo: "Only" modifiers. For example- -wo only analyzes words and implies -p 0
    parser = argparse.ArgumentParser(description = "Find most used words and phrases in a Jekyll post.")

    parser.add_argument('-w', nargs='?', default=5, const=None, type=int, help="Output the top N most used words. If used with no numerical argument, will output the frequency of all words. If not specified, will display the top 5. -w 0 will not print word frequency.")

    parser.add_argument('-p', nargs='?', default=5, const=None, type=int, help="Output the top N most used phrases. If used with no numerical argument, will output the frequency of all phrases. If not specified, will display the top 5. -p 0 will not print phrase frequency. Phrase analysis works much like word analysis and the same options are used.")

    common_words = ['the','be','to','of','and','a', 'in', 'that', 'it']
    parser.add_argument('-f', '--filter', nargs='*', default=common_words, dest='to_filter',  help="Words to filter out of the analysis when doing word-by-word analysis. By default, the following words are excluded: " + ', '.join(common_words) + ". To filter out no words, specify this flag with no arguments. Note that only words are excluded. Phrase analysis is not affected." )

    parsed_args = parser.parse_args();

    toReturn = {}
    toReturn[Options.top_words] = parsed_args.w
    toReturn[Options.top_phrases] = parsed_args.p
    toReturn[Options.to_filter] = {x.casefold() for x in parsed_args.to_filter}

    return toReturn;

def prettyprint_pair_list(from_counter):
    toReturn = ""

    for pair in from_counter:
        toReturn += "{}: {}\n".format(pair[0].title() ,pair[1])

    return toReturn

def do_word_frequency(post, option_dict):

    #C-c-c-combo!
    most_frequent_words = Counter(filter(lambda x: x not in option_dict[Options.to_filter], post.translate(str.maketrans("", "", string.punctuation)).casefold().split())).most_common(option_dict[Options.top_words])

    if option_dict[Options.top_words] == None or option_dict[Options.top_words] > len(most_frequent_words):
        start = "Word frequency"
    else:
        start = "Top " + str(option_dict[Options.top_words]) + " words"

    print(start + " in post:")
    print(prettyprint_pair_list(most_frequent_words))

def make_func_list(option_dict):
    toReturn = []

    if option_dict[Options.top_words] != 0:
        toReturn.append(do_word_frequency)

    return toReturn

if __name__ == "__main__":
    option_dict = make_arg_dict()

    post = skip_header(sys.stdin).read()

    for post_func in make_func_list(option_dict):
        post_func(post, option_dict)

