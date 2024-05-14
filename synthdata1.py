import nltk
nltk.download('punkt')
text = 'Received my new job offer letter today, job offer is fantastic!, I am so excited for my new job !'
sentences = nltk.sent_tokenize(text)
print(sentences)


