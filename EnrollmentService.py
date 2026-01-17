from Enrollment import Enrollment


class EnrollmentService:
    def __init__(self):
        self.enrollment_list = []  # เก็บประวัติการลงทะเบียนทั้งหมดใน List

    def enroll(self, student, subject):
        # 1. ตรวจสอบว่าเคยลงวิชานี้ไปหรือยัง
        for e in self.enrollment_list:
            if e.student.id == student.id and e.subject.id == subject.id:
                print(f"Warning: {student.name} is already enrolled in {subject.name}")
                return

        # 2. ถ้ายังไม่เคย ให้สร้างใบลงทะเบียนใหม่
        new_id = len(self.enrollment_list) + 1
        new_record = Enrollment(new_id, student, subject)

        # 3. บันทึกลง List
        self.enrollment_list.append(new_record)
        print(f"Enroll Success: {student.name} enrolled in {subject.name}")

    def list_all_enrollments(self):
        print("\n--- Enrollment History ---")
        if not self.enrollment_list:
            print("No records yet.")
        else:
            for record in self.enrollment_list:
                print(record)