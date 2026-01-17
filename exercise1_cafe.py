
#Stou cafe
#1) americano -> 30
#2) cappuccino -> 40
#3) matcha -> 50
print('#'*35)
print("#" * 12 +"Coffee Manu" + "#" * 12 )
print('#'*35)
print('Please select manu coffee')
print('Select 1 : Americano price  : 30 bath')
print('Select 2 : Cappuccino price : 40 bath')
print('Select 3 : Matcha price     : 50 bath')
print('#'*35)
manu = int(input("Select manu coffee : -> "))

if manu == 1:
    quantity = int(input("Please Input qty : -> "))
    print (f'Price = {quantity * 30} bath')
elif manu == 2:
    quantity = int(input("Please Input qty : -> "))
    print(f'Price = {quantity * 40} bath' )
elif manu == 3:
    quantity = int(input("Please Input qty : -> "))
    print(f'Price = {quantity * 50} bath')
else:
    print ('Not have this manu ')
