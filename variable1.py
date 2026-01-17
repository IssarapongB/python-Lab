fullname : str
fullname = 'issarapong'

age : int
age = 30

status : bool
status = True

temperature : float
temperature : 38.5

import datetime as dt
now = dt.datetime.now()
print(type(now))

# change type
a:int = 20
a_str = str(a)
print(type(a_str))
print(f'a_str = {a_str}')
print(f'{a_str = }')

t = "20"
b = int(a_str)
print(type(b))
C = int(t)
float(t)