subject2 = {}
subjectkeys = ['subjectid','subjectname','credit','cost']
subjectdetail = input("Enter Subject Detail -> ").split(',')
for index,key in enumerate(subjectkeys):
    subject2.update({key:subjectdetail[index]})

print(subject2)

subject2 = {}
subjectkeys = ['subjectid', 'subjectname', 'credit', 'cost']

# รับค่าและแยกด้วย comma
raw_input = input("Enter Subject Detail (ID,Name,Credit,Cost) -> ")
subjectdetail = raw_input.split(',')

# เช็คว่าใส่ข้อมูลครบ 4 ตัวไหม
if len(subjectdetail) == len(subjectkeys):
    for index, key in enumerate(subjectkeys):
        # .strip() ช่วยตัดช่องว่างหน้าหลังออกให้ด้วยเผื่อเผลอพิมพ์เว้นวรรค
        subject2.update({key: subjectdetail[index].strip()})
    print(subject2)
else:
    print(f"Error: กรุณาป้อนข้อมูลให้ครบ {len(subjectkeys)} อย่าง และคั่นด้วยเครื่องหมาย ,")