print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
foodlist = []
x = 0
while(True):
    x = x + 1
    print("อาหารโปรดลำดับที่ ",x,end=" ") 
    choose = input("คือ\t")
    foodlist.append(choose)
    if choose == 'exit':
        break
print("รายการอาหารสุดโปรดของคุณ มีดังนี้",end=" ")
for z in range(1,x) :
    print(z,".",foodlist[z-1],end="   ")