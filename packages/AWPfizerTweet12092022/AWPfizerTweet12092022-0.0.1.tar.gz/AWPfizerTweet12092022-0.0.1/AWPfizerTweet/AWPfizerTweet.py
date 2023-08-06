import re
from textblob import TextBlob
import pandas as pd

def get_tweet_sentiment(tweet):
  analysis = TextBlob(clean_tweet(tweet))
  if analysis.sentiment.polarity > 0: return 'positive'
  elif analysis.sentiment.polarity == 0: return 'neutral'
  else: return 'negative'

def clean_tweet(tweet):
  return ' '.join(
    re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ",
           tweet).split())

def addSent(dataFrame):
  dataFrame['sentiment'] = [get_tweet_sentiment(twt) for twt in dataFrame['text']]
  return dataFrame

df = pd.DataFrame()
df['text'] = pd.read_csv('vaccination_tweets.csv')['text']
df_sent = addSent(df)
print(df_sent.head(30))

sent = ['positive', 'negative', 'neutral']
val = [0, 0, 0]
for i in df_sent['sentiment']:
  if i == 'positive': val[0] += 1
  elif i == 'negative': val[1] += 1
  else: val[2] += 1

print(
  '''\n\n\nSentiment of Tweets Involving the Pfizer Vacccine:\n(Out of %d total tweets analyzed)\n'''
  % len(df))
for i in range(3):
  percent = val[i] / len(df) * 100
  print("%-8s: %4d%%" % (sent[i], percent))
