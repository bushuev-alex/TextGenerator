whole_number = input()
list_of_numbers = list(whole_number)
numbers = [int(str_number) for str_number in list_of_numbers]
sum_numbers = [sum(numbers[:j]) for j in range(1, len(numbers) + 1)]
print(sum_numbers)
