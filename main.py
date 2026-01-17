import random
# ดึงแค่ User มาก็พอ เพราะ User ถือ Account อยู่แล้ว
from user import User

# ตัวแปรเก็บ User ทั้งหมด {username: UserObject}
all_members = {}
current_user = None


def registration():
    print("--- สมัครสมาชิก ---")
    name = input("ชื่อ: ")
    username = input("Username: ")
    password = input("Password: ")

    if username in all_members:
        print("ชื่อนี้มีคนใช้แล้ว")
    else:
        # สร้าง User ใหม่
        new_user = User(name, username, password)
        all_members[username] = new_user
        print("สมัครเสร็จสิ้น")


def login():
    global current_user
    print("--- เข้าสู่ระบบ ---")
    user_in = input("Username: ")
    pass_in = input("Password: ")

    # เช็ค Username
    if user_in in all_members:
        real_user = all_members[user_in]

        # [จุดที่แก้] เช็ค Password ตรงๆ แบบไม่ Encapsulate
        # เปรียบเทียบรหัสที่พิมพ์มา กับ รหัสใน object เลย
        if real_user.password == pass_in:
            print("Login สำเร็จ!")
            current_user = real_user
            user_menu()
        else:
            print("รหัสผ่านผิด")
    else:
        print("ไม่พบผู้ใช้นี้")


def user_menu():
    while True:
        # เข้าถึงข้อมูลตรงๆ (ไม่ผ่านฟังก์ชัน get)
        print(f"\n--- สวัสดีคุณ {current_user.name} ---")
        print("1. เปิดบัญชีใหม่")
        print("2. ดูข้อมูลบัญชี")
        print("3. ฝากเงิน")
        print("9. ออกจากระบบ")

        choice = input("เลือก: ")

        if choice == '1':
            # สุ่มเลขบัญชี
            acc_no = str(random.randint(10000, 99999))
            current_user.create_account(acc_no)
            print(f"เปิดบัญชีเบอร์ {acc_no} เรียบร้อย")

        elif choice == '2':
            # วนลูปดูบัญชีที่มีในตัว current_user ตรงๆ
            for acc_no, acc_obj in current_user.accounts.items():
                print(f"เบอร์: {acc_no} | เงิน: {acc_obj.balance} บาท")

        elif choice == '3':
            acc_no = input("ฝากเข้าเบอร์บัญชีไหน: ")
            if acc_no in current_user.accounts:
                amt = float(input("จำนวนเงิน: "))

                # เรียกใช้ object Account ให้ทำงาน
                current_user.accounts[acc_no].deposit(amt, "ฝากเงินสด")
                print("ฝากเงินเรียบร้อย")
            else:
                print("คุณไม่มีบัญชีเบอร์นี้")

        elif choice == '9':
            break


# เริ่มโปรแกรมตรงนี้
if __name__ == "__main__":
    while True:
        print("\n--- Main Menu ---")
        print("1. สมัครสมาชิก")
        print("2. เข้าสู่ระบบ")
        cmd = input("เลือก: ")
        if cmd == '1':
            registration()
        elif cmd == '2':
            login()