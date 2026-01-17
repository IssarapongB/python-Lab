class Student:
    def __init__(self, s_id, name, username, password):
        self.id = s_id
        self.name = name
        self.username = username
        self.password = password

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name}"