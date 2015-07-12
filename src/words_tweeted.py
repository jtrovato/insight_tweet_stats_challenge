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



if __name__ == '__main__':

	input_filepath = sys.argv[1]
	output_filepath = sys.argv[2]
    outfile = open(output_filepath, 'w')


    with open(input_filepath,'r') as infile:
    	for line in infile:

	
