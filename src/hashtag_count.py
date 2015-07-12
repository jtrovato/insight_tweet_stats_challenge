#!/usr/bin/env python
import optparse
import sys
import operator

#Python script to track tranding hashtags from a stream of tweets. 

'''
this function takes a list of words as input and adds any hashtags to a running dictionary
'''
def addHashtags(hashtag_dict, word_list):
    for word in word_list:
        if word[0] == '#':
            if word in hashtag_dict:
                hashtag_dict[word] += 1
            else:
                hashtag_dict[word] = 1

    return hashtag_dict



if __name__ == '__main__':

    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]
    hashtag_dict = {}

    # read file line by line adding words to the tweet dictionary
    with open(input_filepath,'r') as infile:
        for line in infile:
            word_list = line.split()
            hashtag_dict = addHashtags(hashtag_dict, word_list)

    # iterate through the tweet dictionary, adding a line for each word and its count
    max_word_length = max(len(word) for word in hashtag_dict.keys()) # this operation is only used for formatting output. Can be removed for performance.
    with open(output_filepath, 'w') as outfile:
        for word, count in sorted(hashtag_dict.items(), key=operator.itemgetter(1), reverse=True): # if output is not required in alphabetical order remove the sorted() for better performance
            outfile.write(word.ljust(max_word_length+1) + str(count) + '\n')




    
