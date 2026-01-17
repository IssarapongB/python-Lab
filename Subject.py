class Subject:
    def __init__(self, sub_id, name, credit, fee):
        self.id = sub_id
        self.name = name
        self.credit = credit
        self.fee = fee

    def __str__(self):
        return f"Code: {self.id} | Subject: {self.name} | Price: {self.fee} THB"