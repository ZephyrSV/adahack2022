import tweepy
from textblob import TextBlob

accessToken = open("../AccessToken.txt").read()
accessTokenSecret = open("../AccessTokenSecret.txt").read()
twitterConsumerKey = open("../TwitterConsumerKey.txt").read()
twitterConsumerSecret = open("../TwitterConsumerSecret.txt").read()
bearer_token = open("../BearerToken.txt").read()

auth = tweepy.OAuthHandler(twitterConsumerKey, twitterConsumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token)

search_term = "boris johnson"
search_term_set = set(search_term.split())
print(search_term_set)
search_query = search_term + " lang:en"
tweets = client.search_recent_tweets(query=search_query, max_results=100)     #returns Response Object

wordcount = {}
word_sentiment= {}
for tweet in tweets[0]:
    text = tweet.text
    words = set(text.lower().split())

    if not words.intersection(search_term_set):
        continue
    sentiment = TextBlob(text).sentiment.polarity
    for word in words:
        wordcount.setdefault(word, 0)
        wordcount[word] += 1
        word_sentiment.setdefault(word, 0)
        word_sentiment[word] += sentiment
    print(text)
    print("The polarity is: " + str(TextBlob(text).sentiment.polarity) + ", The subjectivity is: " + str(
            TextBlob(text).sentiment.subjectivity) + "\n")

wordcount_ = dict(sorted(wordcount.items(), key=lambda item: item[1], reverse=True))
print(wordcount_)

for word in word_sentiment:
    word_sentiment[word] = word_sentiment[word]/wordcount[word]

    word_sentiment_ = [(key, word_sentiment[key]) for key in wordcount_.keys()]

print(word_sentiment_)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
