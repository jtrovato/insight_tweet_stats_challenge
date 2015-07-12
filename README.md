# insight_tweet_stats_challenge
**Author:** Joe Trovato

**Date:** July 2015

**Usage:** ./run.sh (in top level directory)

More specifically, each feature has its own python script that is run with the following command: python featurename.py input_filepath output_filepath. Sample input and output files are included in this repo.

**Input tweets:** tweet_input/tweets.txt

**Output files:** ft1.txt, ft2.txt, ft3.txt, ft4.txt (files correspond to the feature numbers described below)

This challenge was completed as a part of Insight Data Engineering's coding challenge. The challenge consists of reading tweets from a text file and completing some basic statistics on the "stream" of tweets. The code contained in this repo was written to be scaled to much larger tweet inputs than the example, tweets.txt. For instance, tweets are parsed one at a time as oppossed to all at once to avoid memory issues when loading large datasets.

# Feature 1: Word Count
This feature calcualtes the number of times each word appears. A word is defined as anything that is seperated by whitespace. The output file displays the word in alphabetical order.

# Feature 2: Unique Word Median
This feature updates the median number of unique words in a stream of tweets. The median is recalcualted for every new tweet that comes in. I used a max heap to keep track of the sorted first half of unique word counts and a min heap to keep track of the sorted second half of unique word counts. This way, the root of the heap with the larger number of elements is the median, if the heaps are the same size, the average of the two roots is the median. Keeping track of the median this way allows the computation to scale nicely with large numbers of tweets.

# Feature 3: Hashtag Counts
This feature is a simple extension of the **Word Count** feature, but I believe gives more information than a simple word count. This feature counts only hashtags from the input tweet stream and outputs them in order of decreasing frequency.

# Feature 4: Trending Hashtags:
This feature extends the **Hashtag Counts** by introducing time as factor. Hashtags with the most mentions are not always trending. For instance, #TDF2015 , the Tour de France hashtag, had thousands of tweets over the past two weeks, but since the tour ended, other hastags have started gaining momentum and would be classified as "trending", but still have less metions than #TDF2015. To account for time, this algorithm discounts hashtags proportionaly to how recently they were mentioned, giving a more accurate list of 'trending' hashtags. Feel free to edit the *time_weight* and *count_weight* variables in the *rankHashtags( )* function to see different ways of calculating trending hastags. The output file display hashtags in order of their score according the weighting function in *rankHashtags( )*.
