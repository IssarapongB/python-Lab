if manu == 1:
    print("add subject")
    # แสดงตัวอย่างให้ user เห็นว่าจะต้องพิมพ์ยังไง
    raw_input = input("Enter data (code,subject,credit,price) : -> ")

    # ใช้ split แยกข้อความด้วยเครื่องหมายจุลภาค (,)
    new_data = raw_input.split(',')

    # เพิ่มข้อมูลลงใน list ใหญ่
    listsubjects.append(new_data)

    print("\n--- Updated List ---")
    for item in listsubjects:
        print(item)
    print()