#!/usr/bin/env python
import optparse
import sys

#Python script to track words from a stream of tweets

'''
this function takes a list of words as input and adds them to running dictionary counting instances of words
seen as tweets come in.
'''
def addWords(tweet_dict, word_list):
    for word in word_list:
        if word in tweet_dict:
            tweet_dict[word] += 1
        else:
            tweet_dict[word] = 1

    return tweet_dict



if __name__ == '__main__':

    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]
    tweet_dict = {}

    # read file line by line adding words to the tweet dictionary
    with open(input_filepath,'r') as infile:
        for line in infile:
            word_list = line.split()
            tweet_dict = addWords(tweet_dict, word_list)

    # iterate through the tweet dictionary, adding a line for each word and its count
    max_word_length = max(len(word) for word in tweet_dict.keys()) # this operation is only used for formatting output. Can be removed for performance.
    with open(output_filepath, 'w') as outfile:
        for word, count in sorted(tweet_dict.items()): # if output is not required in alphabetical order remove the sorted() for better performance
            outfile.write(word.ljust(max_word_length+1) + str(count) + '\n')




    
