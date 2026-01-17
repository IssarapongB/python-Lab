#Disply
from turtledemo.chaos import f

print("*" * 8 +"Student Information" + "*" * 8 )
print("Name : Issarapong")
print("Surname : boonsong")
print("*" * 35)

print('welcome', end ='-')
print('99232')


# end
print ("081-234-5678")

print('081' ,end ='-')
print('234' ,end ='-')
print('5678' )

#sep
print('081','234','5678' ,end='\n')
print('081','234','5678' ,sep='-')
print('-' * 35)

#print format
data = 12.455678
print(f'hello my data is {data:.2f}')

str = "Student"
print(f'{str}')
print(f'{str:^20}')
print(f'{str:>20}')
print(f'{str:<20}')


# 1
# S00000000002
# 00000000020

queue = 1234
print(f'S{queue:05d}')

#date
import datetime as dt
Now = dt.datetime.now()
print(f'Current date time is {Now:%Y/%m/%d}')
print(f'Current date time is {Now:%Y/%m/%d , %H:%M:%S}')
