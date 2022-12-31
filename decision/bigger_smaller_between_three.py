number1 = int(input('Give one number: '))
number2 = int(input('Give one number: '))
number3 = int(input('Give one number: '))

greater = number2
smaller = number1

if(number1 > number2):
    greater = number1
    smaller = number2

if(number3 > number1):
    greater = number3
else:
    if(number2 > number3):
        smaller = number3

print(f"\nThe greater number {greater}\n")
print(f"The smaller number {smaller}\n")