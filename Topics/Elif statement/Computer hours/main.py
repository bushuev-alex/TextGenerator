# Make sure your output matches the assignment *exactly*
hours = int(input())


def computer_hours(n):
    if n < 2:
        return "That's rare nowadays!"
    elif 2 <= n < 4:
        return "This seems reasonable"
    else:
        return "Don't forget to take breaks!"


print(computer_hours(hours))
