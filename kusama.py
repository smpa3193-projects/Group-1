from twython import Twython
import csv

from collections import Counter

CONSUMER_KEY = 'R2pWRXsbIvXqkHxljWC7muqf4'
CONSUMER_SECRET = 'RIPuyuK8wdd81M23xDqxSWUiwcBaQO5q4TbkfiqIEAIq8T4x1C'
ACCESS_TOKEN = '2806069908-UMVC9dsiI4gMqSBdDSKU1YiJ1fG8gOV0YY0dqCx'
ACCESS_TOKEN_SECRET = 'F93y3Nn9wgaPG91iX1Gm3nPsy5jrZCa00dVIYkYabLK8I'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

all_words = []
infinite_tweets = twitter.search(q='#InfiniteKusama', count=1000)
yayoi_tweets = twitter.search(q='#YayoiKusama', count=1000)
# setup containers for csvs
inf_tweets = []
yay_tweets = []

with open ('infinite4.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(['Hashtag', 'id', 'screen_name', 'Tweet Text', 'URL'])

    for result in infinite_tweets['statuses']:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        # add tweet info to csv containers
        inf_tweets.append(['#InfiniteKusama', result['id'], result['user']['screen_name'], result['text'].encode('utf-8'), url])
    a.writerows(inf_tweets)

# build list of words
for tweet in infinite_tweets['statuses']:
  tweet_words = tweet['text'].split()
  all_words.append(tweet_words)

for tweet in yayoi_tweets['statuses']:
  tweet_words = tweet['text'].split()
  all_words.append(tweet_words)


with open ('yayoikusama4.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(['Hashtag', 'id', 'screen_name', 'Tweet Text', 'URL'])

    for result in yayoi_tweets['statuses']:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
        yay_tweets.append(['#YayoiKusama', result['id'], result['user']['screen_name'], result['text'].encode('utf-8'), url])
    a.writerows(yay_tweets)
    
try:
    twitter.update_status(status='YAYOIKUSAMA 89, INFINITEKUSAMA 87, RT 81, THE 58, TO 52, IN 37, OF 35, A 33, @HIRSHHORN 28, AT 27, AND 25, @ 24, YAYOI 21, FOR 20')
except TwythonError as e:
    print e

# read from csv

# this is called a list comprehension. it's weird but awesome - it performs the same action to each item in a list.
all_words_flattened = [word.upper() for tweet_words in all_words for word in tweet_words]
counts = Counter(all_words_flattened)

for word, count in counts.most_common(15):
  print "%s: %d" % (word, count)