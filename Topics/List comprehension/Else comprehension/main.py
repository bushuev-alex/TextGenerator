# the following line reads the list from the input, do not modify it, please
old_list = [int(num) for num in input().split()]

binary_list = [1 if item > 0 else 0 for item in old_list]
print(binary_list)
