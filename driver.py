import string
from collections import Counter
import matplotlib.pyplot as plt

# NLP Sentiment/Text Analysis

# Create text variable and clean itp
text = open('read.txt', encoding='utf-8').read().lower().translate(str.maketrans('','',string.punctuation))

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
