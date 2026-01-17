# ดึงไฟล์ account.py มาใช้
from account import Account

class User:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password # เก็บพาสเวิร์ดตรงๆ
        self.accounts = {}       # เก็บ object Account

    # ฟังก์ชันสร้างบัญชีใหม่ใส่ตัว User
    def create_account(self, acc_no):
        new_acc = Account(acc_no)
        self.accounts[acc_no] = new_acc