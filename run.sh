#!/usr/bin/env bash

#simple bash script to run tweet stat scripts.
# Each line runs a new feature: python source_file input_tweets_file output_file

python ./src/words_tweeted.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt
python ./src/median_unique.py ./tweet_input/tweets.txt ./tweet_output/ft2.txt
