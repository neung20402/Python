loop = int(input("กรุณากรอกจำนวนครั้งการรับค่า\n"))
total = 0
for x in range(0,loop):
    num = int(input("กรอกตัวเลข : "))
    total = total + num
print("ผลรวมค่าที่รับมาทั้งหมด = ",total)