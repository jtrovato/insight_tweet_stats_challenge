#!/usr/bin/env python
import optparse
import sys

#Python script to track the median unique number of words in a stream of tweets

'''
This function uses a min heap and a max heap to keep track of the middle two or middle number in a set of incoming integers
from these numbers the median can easily be found based on the number of elements in each heap
'''
def calcMedianHeaps(word_list, min_heap, max_heap):
    cur_num_words = len(unique(word_list))
    # add the current number to one of the heaps
    if cur_num_words < max_heap[0]:
    	max_heap._push_max(cur_num_words)
    else:
    	min_heap.push(cur_num_words)
    #adjust the heaps so that min and max are balanced
    if len(max_heap) - len(min_heap) > 1
    	min_heap.push(max_heap._pop_max())
    elif: len(min_heap) - len(max_heap) > 1
    	max_heap._push_max(min_heap.pop())
    #find the median
    if len(min_heap) == len(max_heap):
        median = (min_heap[0] + max_heap[0])/2
    elif len(min_heap) > len(max_heap):
        median = min_heap[0]
    elif len(max_heap) > len(min_heap):
        median = max_heap[0]

    return median, min_heap, max_heap
    


def calcMedian(word_list, unique_words):
    cur_unique_words = len(unique(word_list))

if __name__ == '__main__':

    input_filepath = sys.argv[1]
    output_filepath = sys.argv[2]
    min_heap = []
    max_heap = []

    # read file line by line calculating the median at each step
    with open(input_filepath,'r'), open(output_filepath, 'w') as infile, outfile:
        for line in infile:
            word_list = line.split()
            median, min_heap, max_heap = calcMedianHeaps(tweet_dict, word_list)
            outfile.write(str(median) + '\n')