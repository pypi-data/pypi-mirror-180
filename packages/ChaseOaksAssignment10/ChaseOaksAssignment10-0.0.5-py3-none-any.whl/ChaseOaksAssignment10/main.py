import pandas as pd
import re
from textblob import TextBlob


def clean_tweet(tweet):
	return ' '.join(
	 re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",
	        tweet).split())


# Define a function to get the sentiment of a tweet
def get_tweet_sentiment(tweet):
	analysis = TextBlob(clean_tweet(tweet))
	if analysis.sentiment.polarity > 0:
		return 'positive'
	elif analysis.sentiment.polarity == 0:
		return 'neutral'
	else:
		return 'negative'


# Define a function to process the tweets in a dataframe
def process_tweets(dataframe):
	# Create a new column named 'sentiment' in the dataframe
	dataframe['sentiment'] = dataframe['text'].apply(get_tweet_sentiment)
	return dataframe

def processData(filename):
# Load the tweets from a CSV file
	tweets = pd.read_csv(filename)
	
	# Process the tweets and create a new dataframe with the sentiment of each tweet
	tweet_sentiments = process_tweets(tweets)
	
	# Display the first 30 records from the dataframe
	print(tweet_sentiments.head(30))
	
	# Calculate and display the percentages of positive, negative, and neutral tweets
	sentiment_counts = tweet_sentiments['sentiment'].value_counts()
	total_tweets = len(tweet_sentiments)
	print('Positive tweets: %.2f%%' %
	      (sentiment_counts['positive'] / total_tweets * 100))
	print('Negative tweets: %.2f%%' %
	      (sentiment_counts['negative'] / total_tweets * 100))
	print('Neutral tweets: %.2f%%' %
	      (sentiment_counts['neutral'] / total_tweets * 100))
