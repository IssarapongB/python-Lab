#3) sumcost(price, sales,dateno)
def sumcost(price_list, sales_dict, dateno):
    real_index = dateno - 1
    soap = sales_dict["soap"][real_index] * price_list[0]
    shampoo = sales_dict["shampoo"][real_index] * price_list[1]
    cream = sales_dict["cream"][real_index] * price_list[2]

    result = soap+shampoo+cream
    return result

price = [10, 20, 30] #soap , shampoo , cream
sales = {
    "soap" : [34, 20, 10, 30], #dateno. 1 ,2 ,3,4
    "shampoo" : [10, 25, 10, 20], #dateno. 1 ,2 ,3,4
    "cream" : [15, 10, 15, 40] #dateno. 1 ,2 ,3,4
}
total = sumcost(price, sales,1)
print(f' sumcost : {total}')