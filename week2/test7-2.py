print("     โปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์     ")
print("---------------------------------------")
print("       รถยนต์       4 ล้อ    กด 1       ")
print("       รถยนต์       6 ล้อ    กด 2       ")
print("       รถยนต์มากกว่า 6 ล้อ    กด 3       ")
choose = int(input("\n         เลือกประเภทยานภาหนะ : "))


four = [25 , 30 , 45 , 55 , 60]
six = [45 , 45 , 75 , 90 , 100]
mostsix = [60 , 70 , 110 , 130 , 140]
text = ["\n       ค่าบริการรถยนต์ประเภท 4 ล้อ       \n","\n       ค่าบริการรถยนต์ประเภท 6 ล้อ       \n","\n    ค่าบริการรถยนต์ประเภทมากกว่า 6 ล้อ    \n"]
calist = [list(four), list(six), list(mostsix)]
clist = calist[choose-1]

print(text[choose-1])

print("ลาดกระบัง-->บางบ่อ.....",clist[0],".....บาท")
print("ลาดกระบัง-->บางประกง..",clist[1],".....บาท")
print("ลาดกระบัง-->พนัสคม....",clist[2],".....บาท")
print("ลาดกระบัง-->บ้านบึง.....",clist[3],".....บาท")
print("ลาดกระบัง-->บางพระ....",clist[4],".....บาท")
