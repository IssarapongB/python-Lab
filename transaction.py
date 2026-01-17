import datetime

class Transaction:
    def __init__(self, txn_type, amount, remark, target="null"):
        self.timestamp = datetime.datetime.now()
        self.txn_type = txn_type
        self.amount = amount
        self.remark = remark
        self.target = target

    def __str__(self):
        # เวลาปริ้นท์จะแสดงข้อความแบบนี้
        return f"{self.timestamp}: {self.amount} : {self.remark}"