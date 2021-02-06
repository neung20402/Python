print("ป้อนชื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
foodlist = []
x = 0
while(True):
    x = x + 1
    choose = input("อาหารโปรดลำดับที่ %d คือ\t"%x) 
    foodlist.append(choose)
    if choose == 'exit':
        break
print("รายการอาหารสุดโปรดของคุณ มีดังนี้",end=" ")
for z in range(0,x-1) :
    print('{0}{1}{2}'.format(z+1,'. ',foodlist[z]),end='   ')