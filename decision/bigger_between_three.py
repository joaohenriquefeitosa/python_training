number1 = int(input('Give one number'))
number2 = int(input('Give one number'))
number3 = int(input('Give one number'))

greater = number2;
if(number1 > number2):
    greater = number1

if(number3 > greater):
    greater = number3

print(greater)