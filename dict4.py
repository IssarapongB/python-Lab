# สร้างตัวแปร dictionary
#สร้างตัวแปร dictionaly เก็บรายวิชา
# subject1 = {
#     "Subjectid": "99423",
#     "subjectname":"BigDATA",
#     "credits" : "6"
# },
# subject2 = {
#     "Subjectid": "99424",
#     "subjectname":"MachineLearning",
#     "credits" : "6"
# },
# subject3 = {
#     "Subjectid": "99424",
#     "subjectname":"Datascience",
#     "credits" : "6"
# }

subjectlist = []
subject1 = {}
subject1.update({"Subjectid":"99423"})
subject1.update({"subjectname":"BigDATA"})
subject1.update({"credits":"6"})

subjectlist.append(subject1)

Subjectid = input("Subjectid -> ")
subjectname = input("subjectname -> ")
credits = int(input("credits -> "))

# subject1.update({
#             "Subjectid": Subjectid,
#             "subjectname": subjectname,
#             "credits": credits
#             })
# print(subject1)

newsubject = {}
newsubject.update({
            "Subjectid": Subjectid,
            "subjectname": subjectname,
            "credits": credits
})
subjectlist.append(newsubject)

print(subjectlist)

dict4.py