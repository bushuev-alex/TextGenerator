from collections import Counter

data = input().split(' ')

data_count = Counter(data)
print(data_count.most_common(1)[0][0])
