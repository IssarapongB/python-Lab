# 1) searchbyname(list,name) ---> return bool
def searchbyname(namelist, target_name):
    for name in namelist:
        if name == target_name:
            return True
    return False

frirenlist  = ['urai' , 'pichit' , 'paitoon' , 'urai']
found = searchbyname(frirenlist ,'pirom')
print(found)