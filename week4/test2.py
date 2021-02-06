import os
print("\tโปรแกรมร้านค้าออนไลน์")
print('-'*35)
x = 0
choose_list = ['\t1.ปลั๊กไฟสายยาว','\t2.พัดลมอิเล็กทริค  ','\t3.โทรทัศน์จอโค้ง ','\t4.เครื่องปรับอากาศ ','\t5.เครื่องทำความร้อน ','\t6.เครื่องทำน้ำอุ่น    ']
price_list = [199,259,1999,15,500,999,1599]
cargo_list = [0,0,0,0,0,0]
def menu() :
    global choice
    print('1.แสดงรายการสินค้า\n2.หยิบสินค้าเข้าตะกร้า\n3.แสดงรายจำนวนและราคาของสินค้าที่หยิบ\n4.หยิบสินค้าออกจากตะกร้า\n5.ปิดโปรแกรม\n')
    choice = int(input('กรุณาเลือกทำรายการ'))

def choose_def() :
    for x in range(0,6) :
        print(choose_list[x],' ราคา ',price_list[x],' บาท')

def choice_def() :
    for x in range(0,6) :
        print(choose_list[x])
    pick = int(input('เลือกหยิบสินค้าหมายเลข หรือ พิมพ์ 7 เพื่อออก : '))
    if pick == 1 :
        cargo_list[0] += 1
    elif pick == 2 :
        cargo_list[1] += 1
    elif pick == 3 :
        cargo_list[2] += 1
    elif pick == 4 :
        cargo_list[3] += 1
    elif pick == 5 :
        cargo_list[4] += 1
    elif pick == 6 :
        cargo_list[5] += 1
    elif pick == 7 :
        menu()
    os.system('cls')


def showlist_def() :
    print('_'*10,'สินค้าที่คุณหยิบไปมีดังนี้','_'*10)
    print('-'*15,'{0:-<20}{1:-<15}{2:-<15}'.format('สินค้า','จำนวน','ราคา'))
    for x in range(0,6) :
        print('-'*5,'{0:-<30}{1:-<10}{2:-<10}'.format(choose_list[x],cargo_list[x],cargo_list[x]*price_list[x]))

def deletelist_def() :
    for x in range(0,6) :
        print(choose_list[x])
    pickde = int(input('เลือกสินค้าหมายเลขที่ต้องการหยิบออก หรือ พิมพ์ 7 เพื่อออก : '))
    if pickde == 1 :
        cargo_list[0] -= 1
    elif pickde == 2 :
        cargo_list[1] -= 1
    elif pickde == 3 :
        cargo_list[2] -= 1
    elif pickde == 4 :
        cargo_list[3] -= 1
    elif pickde == 5 :
        cargo_list[4] -= 1
    elif pickde == 6 :
        cargo_list[5] -= 1
    elif pickde == 7 :
        menu()
    os.system('cls')



while(True) :
    menu()
    if choice == 1 :
        os.system('cls')
        choose_def()
    elif choice == 2 :
        os.system('cls')
        choice_def()
    elif choice == 3 :
        os.system('cls')
        showlist_def()
    elif choice == 4 :
        os.system('cls')
        deletelist_def()
    elif choice == 5 :
        close = input('ต้องการปิดโปรแกรมใช่หรือไหม(y/n) : ')
        if close.lower() == 'y' :
            os.system('cls')
            break
        elif close.lower() == 'n' :
            os.system('cls')