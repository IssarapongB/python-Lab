# ดึงไฟล์ transaction.py มาใช้
from transaction import Transaction


class Account:
    def __init__(self, acc_no):
        self.acc_no = acc_no
        self.balance = 0.0  # เงินในบัญชี
        self.transactions = []  # สมุดคู่ฝาก (เก็บใบเสร็จ)

    # ฟังก์ชันฝากเงิน (ทำหน้าที่แค่บวกเลขและจดบันทึก)
    def deposit(self, amount, remark):
        self.balance += amount
        # สร้างใบเสร็จแล้วเก็บ
        new_txn = Transaction("Deposit", amount, remark)
        self.transactions.append(new_txn)

    # ฟังก์ชันถอนเงิน
    def withdraw(self, amount, remark):
        if amount > self.balance:
            return False  # ถอนไม่ได้

        self.balance -= amount
        new_txn = Transaction("Withdraw", -amount, remark)
        self.transactions.append(new_txn)
        return True  # ถอนสำเร็จ