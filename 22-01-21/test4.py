a=[]
while(True):
    print("7-11 Member\n เพิ่ม [a]\n แสดง [s]\n ออกจากระบบ [x]")
    choose = input("เลือกรายการ\t")
    if choose == 'a' :
        pone = input("ป้อนรายการลูกค้า(รหัส:ชื่อ:จังหวัด)")
        a.append(pone)
        print("*"*7,"ข้อมูลได้เข้าสู่ระบแล้ว","*"*7)
    elif choose == 's' :
        print("{0:-<26}".format(""))
        print("{0:-<8}{1:-<10}{2:10}".format("รหัส","ชื่อ","จังหวัด"))
        print("{0:-<26}".format(""))
        for d in a :
            text = d.split(":")
            print("{0[0]:6}{0[1]:10}{0[2]:10}".format(text))
            continue
    elif choose == 'x' :
        break
print("ทำคำสั่งถัดไป")