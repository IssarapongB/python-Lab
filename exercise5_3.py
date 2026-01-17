
#3) sumcost(price, sales,product name,dateno)
def sumcost(price_list, sales_dict, productname, dateno):
    if productname == "soap":
        p = price_list[0]
    elif productname == "shampoo":
        p = price_list[1]
    elif productname == "cream":
        p = price_list[2]
    quantity = sales_dict[productname][dateno]
    result = p * quantity
    return result

price = [10, 20, 30] #soap , shampoo , cream
sales = {
    "soap" : [34, 20, 10, 30], #dateno. 1 ,2 ,3,4
    "shampoo" : [10, 25, 10, 20], #dateno. 1 ,2 ,3,4
    "cream" : [15, 10, 15, 40] #dateno. 1 ,2 ,3,4
}
dateno = int(input("dateno -> "))
productname = str(input("productname -> "))
total = sumcost(price, sales,productname,dateno)
print(f'price from date : {dateno } sumcost : {total}')



