from twython import Twython
import csv

from collections import Counter

CONSUMER_KEY = 'R2pWRXsbIvXqkHxljWC7muqf4'
CONSUMER_SECRET = 'RIPuyuK8wdd81M23xDqxSWUiwcBaQO5q4TbkfiqIEAIq8T4x1C'
ACCESS_TOKEN = '2806069908-UMVC9dsiI4gMqSBdDSKU1YiJ1fG8gOV0YY0dqCx'
ACCESS_TOKEN_SECRET = 'F93y3Nn9wgaPG91iX1Gm3nPsy5jrZCa00dVIYkYabLK8I'

twitter = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

all_words = []
tweets = twitter.search(q='#InfiniteKusama', count="500")
text = []

with open ('test6.csv', 'w') as fp:
    a = csv.writer(fp)
    # add a header row
    a.writerow(('#InfiniteKusama', 'Tweet Text', 'URL'))

    for result in tweets['statuses']:
        try:
            url = result['entities']['urls'][0]['expanded_url']
        except:
            url = None
            
        a.writerows((text))

# build list of words
for tweet in tweets['statuses']:
  tweet_words = tweet['text'].split()
  all_words.append(tweet_words)
  
# this is called a list comprehension. it's weird but awesome - it performs the same action to each item in a list.
all_words_flattened = [word.upper() for tweet_words in all_words for word in tweet_words]
counts = Counter(all_words_flattened)

for word, count in counts.most_common(15):
  print "%s: %d" % (word, count)
  
with open ('yayoikusama.csv', 'w') as fp:
	a = csv.writer(fp)
    # add a header row
a.writerow(('#YayoiKusama', 'Tweet Text', 'URL'))

for result in tweets['statuses']:
    try:
        url = result['entities']['urls'][0]['expanded_url']
    except:
        url = None
            
    a.writerows((text))
        
# build list of words
for tweet in tweets['statuses']:
  tweet_words = tweet['text'].split()
  all_words.append(tweet_words)
  
# this is called a list comprehension. it's weird but awesome - it performs the same action to each item in a list.
all_words_flattened = [word.upper() for tweet_words in all_words for word in tweet_words]
counts = Counter(all_words_flattened)