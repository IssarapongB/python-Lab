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
