# math
# +, - , * , / , // , % , **
a : int = 10
a = 6
b = 3
c = a // b
print(f'{a} + {b} ={c}') # 10 + 3 = 13

print(f'{10+3=}')


import math
print(pow(c,c))
print(math.sqrt(c))
answer = (math.sqrt(c))
print(f'{answer:.2f}')
print(f'{answer=:.2f}')


# comparison --> bool
# == , != ,<= ,< ,> ,>=,in,!
a = 10
b = 6
result = a < b
print(f'{a} < {b} = {result}')

atuple = (1,2,3,4,5)
result = 3 in atuple
result2 = 10 in atuple
print(result)
print(result2)

print(end="\n")

# and , or
result = (a>10) and (b<6)
result2 = (a>=10) or (b<6)
print(result)
print(result2)
