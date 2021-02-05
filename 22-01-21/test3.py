print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
foodlist = []
x = 4
y = 0
while x > 3 :
    y = y + 1
    choose = input("อาหารโปรดลำดับที่  คือ\t")
    foodlist.append(choose)
    if choose == 'exit':
        break
print("รายการอาหารสุดโปรดของคุณ มีดังนี้")
for z in range(1,y) :
    print(z,".",foodlist[z-1])