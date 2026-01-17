list1 = [1,2,3,4,5]
list2 =[]
for item in list1:
    item = pow(item,2)
    list2.append(item)
print(list2)

list2 = []
for item in list1:
    list2.append(item**2)
print(list2)

list2 = [i**2 for i in list1]
print(list2)

list2 =[]
for item in list1:
    if item % 2 == 0 :
        item2 = item**2
        list2.append(item2)
    else:
        list2.append(item)
print(list2)

list2 = [i**2 if i%2==0 else i for i in list1]
print(list2)


#list3 = list1*3
#print
