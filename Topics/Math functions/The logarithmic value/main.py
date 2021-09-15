import math
number_1 = int(input())
number_2 = int(input())

if number_2 < 0 or number_2 == 0 or number_2 == 1:
    print(round(math.log(number_1), 2))
else:
    print(round(math.log(number_1, number_2), 2))
