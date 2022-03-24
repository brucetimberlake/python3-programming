scores = "67 80 90 78 93 20 79 89 96 97 92 88 79 68 58 90 98 100 79 74 83 88 80 86 85 70 90 100"
all_scores = scores.split()
print(all_scores)
a_scores = 0
for score in all_scores:
    print(score)
    if (int(score) >= 90):
        a_scores = a_scores + 1

print("a_scores is ", a_scores)
