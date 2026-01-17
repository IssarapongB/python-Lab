from Student import Student
from Subject import Subject
from StudentService import StudentService
from SubjectService import SubjectService
from EnrollmentService import EnrollmentService


# --- ส่วนตั้งค่าข้อมูลเริ่มต้น (Mock Data) ---
def load_initial_data(std_service, sub_service):
    # เพิ่มวิชา
    sub_service.add_subject(Subject('101', 'Python Programming', 3, 5000))
    sub_service.add_subject(Subject('102', 'Web Development', 3, 4500))
    sub_service.add_subject(Subject('103', 'Data Science', 3, 6000))

    # เพิ่มนักเรียน
    std_service.add_student(Student('S01', 'Somchai', 'som', '1234'))
    std_service.add_student(Student('S02', 'Somsri', 'sri', '5678'))


# --- ฟังก์ชันหลักของโปรแกรม ---
def main():
    # สร้าง Service เตรียมไว้ใช้งาน
    student_sv = StudentService()
    subject_sv = SubjectService()
    enroll_sv = EnrollmentService()

    # โหลดข้อมูลตัวอย่าง
    load_initial_data(student_sv, subject_sv)

    while True:
        print("\n" + "=" * 30)
        print("   UNIVERSITY SYSTEM v2.0")
        print("=" * 30)
        print("1. Register New Student")
        print("2. Show All Students")
        print("3. Search Student")
        print("4. Show All Subjects")
        print("5. Enroll (Register Subject)")
        print("6. Show Enrollment History")
        print("0. Exit")

        choice = input("Select Menu: ")

        if choice == '1':
            print("\n--- Register Student ---")
            s_id = input("ID: ")
            name = input("Name: ")
            user = input("Username: ")
            pw = input("Password: ")
            # สร้าง object Student
            new_std = Student(s_id, name, user, pw)
            # ส่งให้ Service บันทึก
            student_sv.add_student(new_std)

        elif choice == '2':
            student_sv.list_all_students()

        elif choice == '3':
            keyword = input("Enter name to search: ")
            student_sv.search_by_name(keyword)

        elif choice == '4':
            subject_sv.list_all_subjects()

        elif choice == '5':
            print("\n--- Enrollment Process ---")
            # 1. หาตัวนักเรียนก่อน
            s_id = input("Enter Student ID: ")
            found_std = student_sv.get_student_by_id(s_id)

            if found_std:
                print(f"Student Selected: {found_std.name}")
                # 2. หาวิชาที่จะลง
                sub_id = input("Enter Subject Code (e.g., 101): ")
                found_sub = subject_sv.get_subject_by_id(sub_id)

                if found_sub:
                    print(f"Subject Selected: {found_sub.name} ({found_sub.fee} THB)")
                    confirm = input("Confirm? (y/n): ")
                    if confirm.lower() == 'y':
                        # 3. สั่งให้ Service ทำการลงทะเบียน
                        enroll_sv.enroll(found_std, found_sub)
                else:
                    print("Error: Subject not found!")
            else:
                print("Error: Student ID not found!")

        elif choice == '6':
            enroll_sv.list_all_enrollments()

        elif choice == '0':
            print("Good Bye!")
            break
        else:
            print("Invalid choice!")


if __name__ == '__main__':
    main()