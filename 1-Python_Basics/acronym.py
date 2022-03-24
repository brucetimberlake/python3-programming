stopwords = ['to', 'a', 'for', 'by', 'an', 'am', 'the', 'so', 'it', 'and', "The"]
org = "The organization for health, safety, and education"

acro = ""
org_list = org.split()
for word in org_list:
    print("Checking ", word)
    if (word not in stopwords):
        print(word, "is not in ", stopwords)
        letter = word[0].upper()
        print("letter is ", letter)
        acro = acro + letter
        print("acro is now ", acro)

print(acro)
