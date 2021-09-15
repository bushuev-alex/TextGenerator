from collections import Counter

text = ("all I want is a proper cup of coffee made in a proper copper coffee pot. "
        + "I may be off my dot but I want a cup of coffee from a proper coffee pot.")
text_list = text.split(" ")

freq_counter = Counter(text_list)
n = int(input())
for word in freq_counter.most_common(n):
    print(*word, sep=' ')
