print("          เลือกเมนูเพื่อทำรายการ          ")
print("#####################################")
print("           กด 1 เลือกเหมาจ่าย          ")
print("          กด 2 เลือกจ่ายเพิ่มเติม         ")
choose = int(input("เลือกประเภทการจ่าย : "))
long = int(input("กรุณากรอกระยะทาง\n"))
if choose == 1 :
    if long <= 25 :
        bill = 25
    else :
        bill = 55
if choose == 2 :
    if long <= 25 :
        bill = 25
    else :
        bill = 80
print("ค่าใช้จ่าย รวมทั้งหมด ",bill," บาท")