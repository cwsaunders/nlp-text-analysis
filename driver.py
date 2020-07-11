import string

# NLP Sentiment/Text Analysis

# Create text variable and clean itp
text = open('read.txt', encoding='utf-8').read().lower().translate(str.maketrans('','',string.punctuation))
print(text)
