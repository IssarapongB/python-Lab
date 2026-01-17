
subject1 = {
    "Subjectid": "99423",
    "subjectname":"BigDATA",
    "credits" : "3"
}

subject2 = {
    "Subjectid": "99424",
    "subjectname":"MachineLearning",
    "credits" : "3"
}

subject3 = {
    "Subjectid": "99424",
    "subjectname":"Datascience",
    "credits" : "3"
}


aperson1 = {
    "id": "6796000245",
    "name": "issarapong",
    'subject':[
        {
        "Subjectid": "99423",
        "subjectname":"BigDATA",
        "credits" : "3"
        },
        {
        "Subjectid": "99424",
        "subjectname":"MachineLearning",
        "credits" : "3"
        }]
}

aperson2 = {
    "id": "6796000246",
    "name": "pirot",
    'subject':[
        {
            "Subjectid": "99423",
            "subjectname": "BigDATA",
            "credits": "3"
        },
        {
            "Subjectid": "99424",
            "subjectname": "MachineLearning",
            "credits": "3"
        }
    ]
}

print(aperson1['id'], aperson1)


