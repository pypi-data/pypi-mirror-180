import pandas as p
import re
from textblob import TextBlob

def clean_tweet(tweet):
  return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
		
	# create TextBlob object of passed tweet text
	analysis = TextBlob(clean_tweet(tweet))
	# set sentiment
	if analysis.sentiment.polarity > 0:
		return 'positive'
	elif analysis.sentiment.polarity == 0:
		return 'neutral'
	else:
		return 'negative'

def Sentiment(dfwt):
  sentiment = [];
  keys = list(dfwt.columns)
  indexoft = keys.index('text')
  for n in range(0, len(list(dfwt.index))):
    sent = get_tweet_sentiment(dfwt.iloc[n,indexoft])
    sentiment.append(sent)
  dfwt['sentiment'] = sentiment
  return dfwt

def Assignment(f):
  df = p.read_csv(f)
  sdf = Sentiment(df)
  only = sdf.head(30)
  print(only)

  sent = sdf['sentiment'].values

  pos = 0
  neg = 0 
  neu = 0
  num = 0
  for m in range(len(sent)):
    reception = sent[m]
    if reception == 'positive':
      pos += 1
      num += 1
    elif reception == 'negative':
      neg += 1
      num += 1
    elif reception == 'neutral':
      neu += 1
      num += 1

  print("Positive Reception = ", round((pos/len(sent))*100, 2), "%")
  print("Negative Reception = ", round((neg/len(sent))*100, 2), "%")
  print("Neutral Reception = ", round((neu/len(sent))*100, 2), "%")