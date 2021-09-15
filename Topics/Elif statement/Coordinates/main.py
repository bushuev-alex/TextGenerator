number1 = float(input())
number2 = float(input())

if number1 > 0 and number2 > 0:
    print('I')
elif number1 < 0 and number2 > 0:
    print('II')
elif number1 < 0 and number2 < 0:
    print('III')
elif number1 > 0 and number2 < 0:
    print('IV')
elif number1 == 0 and number2 == 0:
    print("It's the origin!")
else:
    print("One of the coordinates is equal to zero!")
