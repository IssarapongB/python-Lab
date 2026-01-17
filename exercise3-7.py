

names = ["urai" , "manee" , "Paitoon" ,"wittaya" ,"suda"]
names.remove("urai")

listsubjects =[['99423','BigDATA','3','1100']
    ,['99424','MachineLearning','3','4100']
    ,['99425','Datascience','3','2000']]

print("show current of list_subject")
for i in listsubjects:
  print(i)
count = 1
while count != 0:
    print('Please select manu ')
    print('Select 1 : add subject')
    print('Select 2 : add remove')
    print('Select 3 : search')
    print('Select 0 : exit')
    manu = int(input("Select manu : -> "))
    if manu == 1:
        print("add subject")
        code = input("Select code : -> ")
        subject = input("Select subject : -> ")
        credit = input("Select Credit : -> ")
        price = input("Select price : -> ")
        listsubjects.append([code,subject,credit,price])

        for item in listsubjects:
            print(item)
    elif manu == 2:
            print("add remove code")
            code = input("remove code : -> ")
            for sub in listsubjects:
                if sub[0] == code:
                    listsubjects.remove(sub)
                    for item in listsubjects:
                        print(item)
                    break
    elif manu == 3:
        print("search")
        code = input("search code : -> ")
        for sub in listsubjects:
            if sub[0] == code:
                print(f"Found: {sub}")
                break
            else:
                print(f"Not found")
    elif manu == 0:
        count = 0

