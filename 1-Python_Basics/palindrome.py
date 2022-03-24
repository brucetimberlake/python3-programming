p_phrase = "was it a car or a cat I saw"

p_phrase_len = len(p_phrase)
r_phrase = p_phrase[p_phrase_len::-1]

p_test = p_phrase.lower().replace(" ", "")
r_test = r_phrase.lower().replace(" ", "")

print("p_test: ", p_test)
print("r_test: ", r_test)

if (r_test == p_test):
    print("'", p_phrase, "' is a palindrome")
