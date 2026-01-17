# if condition :
#  ???
#else :
#  ???


criteria1 = 80
criteria2 = 60

score = float(input("Input Score -> "))

if score >= criteria1:
    grade = 'H'
elif score >= criteria2:
    grade = 'S'
else :
    grade = 'U'

print (f' Your score is {score} , you got {grade}')


#vars = actiontrue if condition else actionfalse
grade = 'S' if score >= criteria1 else ' U'
print (f' Your score is {score} , you got {grade}')
print ('H') if score >= 80 else print('s') if score >=60 else print('U')

grade = 'H' if score >= 80 else 'S' if score >=60 else 'u'
print(grade)

