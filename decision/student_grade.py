first_grade = input('Give one grade')
second_grade = input('Give another grade')

average = (first_grade + second_grade)/2

if(average == 10):
    print("Aproved with distinction")
elif(average < 10 and average >= 7 ):
    print("Aproved")
else:
    print("Reproved")