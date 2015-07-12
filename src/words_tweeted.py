#!/usr/bin/env python
import optparse
import sys

#Python script to track words from stream of tweets


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
    outfile = open(output_filepath, 'w')
    tweet_dict = {}

    # read file line by line adding words to the tweet dictionary
    with open(input_filepath,'r') as infile:
    	for line in infile:
    		word_list = line.split()
    		tweet_dict = addWords(tweet_dict, word_list)

    # iterate through the tweet dictionary, adding a line for each word and its count
    max_word_length = max(len(word) for word in tweet_dict.keys()) # this operation is only used for formatting output. Can be removed for performance.
    with open(output_filepath, 'w') as outfile:
    	for word, count in tweet_dict.items()
    		outfile.write(word.ljust(max_word_length+1) + str(count))




	
