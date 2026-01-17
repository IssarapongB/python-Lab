# 2)mapsquare(list) -- return listofsquare
def mapsquare(numberlist):
    result_list = []
    for number in numberlist:
        square = number * number
        result_list.append(square)
    return result_list


numberlist = [1, 4, 5, 7]
squarelist = mapsquare(numberlist)
print(squarelist)
