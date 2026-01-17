import datetime

class Enrollment:
    def __init__(self, enroll_id, student, subject):
        self.enroll_id = enroll_id
        self.student = student
        self.subject = subject
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        # แสดงผล: ใบที่ 1 | นาย ก ลงเรียน วิชา Python
        return f"No.{self.enroll_id} | {self.student.name} -> {self.subject.name}"