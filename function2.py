
def showMenu(menu):
    for index,(k,v) in enumerate(menu.items()):
        print(f'{index+1}---> {k}--->{v}')

menudict = {
    'kaopad' : 30,
    'kaidao' : 40,
}

menudict["kaolao"]=50
menudict["Espresso"]=50

new_name = input("Enter menu name: ")
new_price = int(input("Enter price: "))
menudict[new_name] = new_price
showMenu(menudict)



