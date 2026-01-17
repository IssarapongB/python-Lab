sum = 0
count = 1
while count != 0:
    print('#' * 35)
    print("#" * 12 + "Coffee Manu" + "#" * 12)
    print('#' * 35)
    print('Please select manu coffee')
    print('Select 1 : Americano price  : 30 bath')
    print('Select 2 : Cappuccino price : 40 bath')
    print('Select 3 : Matcha price     : 50 bath')
    print('Select 0 : Exit Calculate price')
    print('#'*35)
    manu = int(input("Select manu coffee : -> "))

    if manu == 1:
        quantity = int(input("Please Input qty : -> "))
        print (f'Americano Price = {quantity * 30} bath')
        sum += quantity * 30
    elif manu == 2:
        quantity = int(input("Please Input qty : -> "))
        print(f'Cappuccino Price = {quantity * 40} bath' )
        sum += quantity * 40
    elif manu == 3:
        quantity = int(input("Please Input qty : -> "))
        print(f'Matcha Price = {quantity * 50} bath')
        sum += quantity * 40
    elif manu == 0:
        print(f'Thank you for buy Coffee ')
        print(f'Calculate price total price = {sum}')
        count = 0
    else:
        print ('Not have this manu ')
