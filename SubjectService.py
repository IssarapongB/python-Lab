class SubjectService:
    def __init__(self):
        self.subjects = {} # เก็บข้อมูลแบบ Dictionary { "รหัสวิชา": Objectวิชา }

    def add_subject(self, new_subject):
        self.subjects[new_subject.id] = new_subject

    def get_subject_by_id(self, sub_id):
        return self.subjects.get(sub_id)

    def list_all_subjects(self):
        print("\n--- Available Subjects ---")
        for sub in self.subjects.values():
            print(sub)