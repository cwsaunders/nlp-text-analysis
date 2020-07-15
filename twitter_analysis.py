import string
from collections import Counter
import matplotlib.pyplot as plt
import GetOldTweets3 as got

# NLP Sentiment/Text Analysis Program

# GetOldTweets3 function used for gathering twitter data to analyze
def get_old_tweets():
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch('europe refugees')\
    .setSince("2015-05-01")\
    .setUntil("2015-09-30")\
    .setMaxTweets(1000)

    # Storing list of objects into tweets variable
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    # Storing tweets into text_tweets variable (list of lists)
    text_tweets = [[tweet.text] for tweet in tweets]
    return text_tweets

text = ""
text_tweets = get_old_tweets()
length = len(text_tweets)

for i in range(0,length):
    text = text_tweets[i][0] + " " + text



# Clean text
text.lower().translate(str.maketrans('','',string.punctuation))

tokenized_words = text.split()

# Take specified stop words from .txt file
stop_words = open('stop-words.txt', encoding='utf-8').read().lower().split()

final_words = []

for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# print(final_words)

emotion_list = []
with open('emotions.txt', 'r') as emotions:
    for line in emotions:
        line = line.replace('\n','').replace(',', '').replace("'",'').strip()
        word, emotion = line.split(':')
        # print("Word :",word,"Emotion :",emotion)

        if word in final_words:
            emotion_list.append(emotion)
# print(emotion_list)

emotion_counter = Counter(emotion_list)
# print(emotion_counter)


fig, ax1 = plt.subplots()
ax1.bar(emotion_counter.keys(),emotion_counter.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
