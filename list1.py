# collections
# list,tuple,set,dict
from os import name

scores = 56
#list
scores = []
scores = [56,60,34,70,90,66]
# names = ['Issarapong' , 'kritsana' , 'thinaphop']

print(f'{len(scores)}')

scores.append(12)

print(f'{len(scores)=}')
print(scores[0:2]) # Except last position
print(scores[:3])
print(scores[-1])
print(scores[1:7:2])

for i in range(0,len(scores)):
    print(scores[i])


sum = 0
for num in scores:
    sum += num
print(sum)



names = ["urai" , "manee" , "chujai" ,"winai" ,"mali"]
names.remove("urai")

for idx,name in enumerate(names):
    print(f"{idx+1}. {name}")

newname = sorted(names, reverse=True)
print(newname)


# print('Select 1 : Americano price  : 30 bath')
# print('Select 2 : Cappuccino price : 40 bath')
# print('Select 3 : Matcha price     : 50 bath')
menus = ['Americano','Cappuccino','Matcha']
price = ['30','40','50']
print('Please select manu coffee')
select = 1
for i in range(0,len(menus)):
    print(f'Select {select} : {menus[i]} price  : {price[i]} bath')
    select = select + 1

alist =[['99323','python','aaa'],['99420','python','aaa'],['99323','python','aaa'],]
