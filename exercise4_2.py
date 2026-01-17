#เพิ่มรายวิชา
#วิธีที่1 (dic ใน dic )
studentdict = {}

for i in range(3):

    studentid = input("studentid: ")
    studentname = input("studentname: ")
    studentdict[studentid] = {
        "studentname": studentname,
    }
print("--------------------------------")
print("Dictionary :")
print(studentdict)
