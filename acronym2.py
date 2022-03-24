stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', 'The']
sent = "The water earth and air are vital"


acro = ""
sent_list = sent.split()
for word in sent_list:
    if (word not in stopwords):
        letters = word[0].upper() + word[1].upper() + ". "
        acro = acro + letters

print(acro)
