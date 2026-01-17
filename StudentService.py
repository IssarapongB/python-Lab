class StudentService:
    def __init__(self):
        self.students = {}  # เก็บข้อมูลแบบ Dictionary { "รหัสนักเรียน": Objectนักเรียน }

    def add_student(self, new_student):
        # เช็คก่อนว่ารหัสซ้ำไหม
        if new_student.id in self.students:
            print(f"Error: ID {new_student.id} already exists!")
            return False
        else:
            self.students[new_student.id] = new_student
            print(f"Success: Added student {new_student.name}")
            return True

    def get_student_by_id(self, s_id):
        # คืนค่า object นักเรียน ถ้าหาไม่เจอจะคืนค่า None
        return self.students.get(s_id)

    def search_by_name(self, keyword):
        print(f"\n--- Search Result for '{keyword}' ---")
        found = False
        for std in self.students.values():
            if keyword.lower() in std.name.lower():
                print(std)
                found = True

        if not found:
            print("Not found.")

    def list_all_students(self):
        print("\n--- All Students ---")
        if not self.students:
            print("No students found.")
        else:
            for std in self.students.values():
                print(std)