import tweepy
import re, string
from nltk import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sid = SentimentIntensityAnalyzer()

stop_words = stopwords.words('english')

accessToken = open("../AccessToken.txt").read()
accessTokenSecret = open("../AccessTokenSecret.txt").read()
twitterConsumerKey = open("../TwitterConsumerKey.txt").read()
twitterConsumerSecret = open("../TwitterConsumerSecret.txt").read()
bearer_token = open("../BearerToken.txt").read()

auth = tweepy.OAuthHandler(twitterConsumerKey, twitterConsumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)
client = tweepy.Client(bearer_token)

search_term = "bad apples"
search_term_set = set(search_term.lower().split())
search_query = search_term + " lang:en -is:verified -is:retweet"
tweets = client.search_recent_tweets(query=search_query, max_results=100)  # returns Response Object


def remove_noise(tweet_tokens, stop_words=()):
    """
    takes a list of strings
    """

    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|' \
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', token)
        token = re.sub("(@[A-Za-z0-9_]+)", "", token)
        token = re.sub("([$-_.…“,”!?]+)", "", token)

        if tag.startswith("NN"):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stop_words and token != 'rt' and token != 'amp':
            cleaned_tokens.append(token.lower())
    return cleaned_tokens


wordcount = {}
word_sentiment = {}
for tweet in tweets[0]:
    text = tweet.text
    print(tweet.text + "\n")
    words1 = text.lower().split()
    words = set(remove_noise(words1, stop_words))
    #print(words)

    if not words.intersection(search_term_set):
        continue
    sentiment = sid.polarity_scores(text)["compound"]
    for word in words:
        wordcount.setdefault(word, 0)
        wordcount[word] += 1
        word_sentiment.setdefault(word, 0)
        word_sentiment[word] += sentiment
    print("The polarity is: " + str(sentiment)+"\n")

wordcount_ = dict(sorted(wordcount.items(), key=lambda item: item[1], reverse=True))
print(wordcount_)

for word in word_sentiment:
    word_sentiment[word] = word_sentiment[word] / wordcount[word]

    word_sentiment_ = [(key, word_sentiment[key]) for key in wordcount_.keys()]

print(word_sentiment_)

full_list = [[word, wordcount_[word], word_sentiment[word]] for word in wordcount_.keys()]

print(full_list[:50])
