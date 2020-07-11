import string

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

print(final_words)
