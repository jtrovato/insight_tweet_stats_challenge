#!/usr/bin/env python
import optparse
import sys
import operator

#Python script to track tranding hashtags from a stream of tweets. 

'''
this function takes a list of words as input and adds any hashtags to a running dictionary
'''
def addHashtags(hashtag_dict, word_list, entry_number):
    for word in word_list:
        if word[0] == '#':
            if word in hashtag_dict:
                t = hashtag_dict[word]
                hashtag_dict[word] = (t[0]+1, i)
            else:
                hashtag_dict[word] = (1, i)

    return hashtag_dict

def rankHashtags(hastag_dict):
    hashtag_scores = {}
    #weights for componetns of trending formula
    count_weight = 0.4
    time_weight = 0.6


    max_count = max(t[0] for t in hashtag_dict.values())
    max_time = max(t[1] for t in hashtag_dict.values())+1
    for word, t in hashtag_dict.items():
        hashtag_scores[word] = count_weight*(t[0]/max_count) + time_weight*(1/(max_time - t[1]))
    return hashtag_scores



if __name__ == '__main__':

    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]
    hashtag_dict = {}

    # read file line by line adding words to the tweet dictionary
    with open(input_filepath,'r') as infile:
        for i, line in enumerate(infile):
            word_list = line.split()
            hashtag_dict = addHashtags(hashtag_dict, word_list, i)

    # iterate through the tweet dictionary, adding a line for each word and its count
    max_word_length = max(len(word) for word in hashtag_dict.keys()) # this operation is only used for formatting output. Can be removed for performance.
    with open(output_filepath, 'w') as outfile:
        hashtag_scores = rankHashtags(hashtag_dict)
        for word, count in sorted(hashtag_scores.items(), key = operator.itemgetter(1), reverse=True):
          outfile.write(word.ljust(max_word_length+1) + str(count) + '\n')




    
