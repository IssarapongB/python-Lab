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