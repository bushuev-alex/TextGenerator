random_dict.setdefault(word, 0)

if random_dict[word] == 0:
    print("Not in the dictionary")
else:
    print(random_dict[word])
