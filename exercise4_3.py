studentdict = {}

def registration():
    print("--- ลงทะเบียนเรียน ---")
    studentid = input("Student ID: ")
    studentname = input("Student Name: ")
    subject_list = []

    print(" type '0' for 'exit'")
    while True:
        code = input("Subject Code: ")
        if code == '0':
            break
        subject_list.append(code)

    studentdict[studentid] = {
        "studentname": studentname,
        "subjectcode": subject_list
    }

    print("--------------------------------")
    print("Current Data:")
    print(studentdict)

while True:
    print("\n" + "#" * 20)
    print("Main Menu")
    print("1 -> Registration")
    print("2 -> Search Student ")
    print("3 -> Search Subject")
    print("9 -> Exit")
    choice = input("Your Choice -> ")

    if choice == '1':
        registration()

    elif choice == '2':
        search_name = input("search_name: ")
        found = False
        for sid, data in studentdict.items():
            if data["studentname"] == search_name:
                print(f"Result: {search_name} registered {data['subjectcode']}")
                found = True
        if not found:
            print("Not found")

    elif choice == '3':
        search_subj = input("search_subjectcode: ")
        found_count = 0
        students_who_took = []

        for sid, data in studentdict.items():
            if search_subj in data["subjectcode"]:
                found_count += 1
                students_who_took.append(data["studentname"])

        print(f"Subject {search_subj} | Count: {found_count} | Students: {students_who_took}")

    elif choice == '9':
        break