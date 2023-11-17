from textblob import TextBlob
from newspaper import Article

with open('input.txt','r') as f:
    text=f.read()
    
blob=TextBlob(text)
sentiment=blob.sentiment.polarity #-1 to 1
print(sentiment)