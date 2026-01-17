#เพิ่มรายวิชา
#วิธีที่1 (dic ใน dic )
subjectdict = {}

for i in range(3):

    Subjectid = input("s_id: ")
    subjectname = input("s_name: ")
    credits = input("s_credit: ")
    subjectdict[Subjectid] = {
        "subjectname": subjectname,
        "credits": credits
    }
print("--------------------------------")
print("Dictionary :")
print(subjectdict)


#วิธีที่2 (dic ใน list )
subjectlist = []
subject1 = {}

for i in range(3):
    Subjectid = input("Subjectid -> ")
    subjectname = input("subjectname -> ")
    credits = int(input("credits -> "))
    newsubject = {}
    newsubject.update({
                "Subjectid": Subjectid,
                "subjectname": subjectname,
                "credits": credits
    })
    subjectlist.append(newsubject)

print("List of subjects :")
print(subjectlist)