import os
voca_list = []
type_list = []
mean_list = []
add_dict = {'คำศัพท์':''}
del_voca_dict = {}
num = 0
type_dict = {'n.':'คำนาม\t','v.':'คำกริยา\t','adj.':'คำคุณศัพท์\t','adv.':'คำกริยาวิเศษณ์'}
def menu() :
    global choose
    print('1.) เพิ่มคำศัพท์\n2.) แสดงคำศัพท์\n3.) ลบคำศัพท์\n4.) ออกจากโปรแกรม\n')
    choose = int(input('กรุณาเลือกประเภทรายการ : '))

def add_def() :
    global add_dict
    add1 = input('เพิ่มคำศัพท์\t')
    add2 = input('ชนิดคำศัพท์(n. , v. , adj. , adv.)')
    add3 = input('ความหมาย\t')
    voca_list.append(add1)
    type_list.append(add2)
    mean_list.append(add3)
    add_dict = {'คำศัพท์':voca_list,'ชนิดคำศัพท์':type_list,'ความหมาย':mean_list}
    print('เพิ่มคำศัพท์เรียบร้อยแล้ว')

def show_def() :
    global num
    num = len(add_dict['คำศัพท์'])
    if num < 5 :
        print('-'*45)
        print(' '*10,'โปรดป้อนคำศัพท์อย่างน้อย 5 คำ')
        print(' '*15,'(ขณะนี้มี %d คำ)'%num)
        print('-'*45)
    else :
        print('-'*45)
        print(' '*12,'คำศัพท์มีทั้งหมด ',int(num),' คำ')
        print('-'*45)
        print('\tความหมาย\t\tประเภท\t\tความหมาย')
        for x in range(0,num) :

            print('\t',add_dict['คำศัพท์'][x],end='\t\t')
 
            for m,n in type_dict.items() :
                if m == add_dict['ชนิดคำศัพท์'][x] :
                    print(m,n,end='\t')
                    break
                if not m in add_dict['ชนิดคำศัพท์'] :
                    print('โปรดป้อนชนิดคำศัพท์ให้ถูกต้อง',end=' ')
                    break

            print(add_dict['ความหมาย'][x])

def delete_def() :
    del_voca = input('กรุณาพิมพ์คำศัพท์ที่ต้องการลบ : ')
    for x in range(0,num) :
        if del_voca == add_dict['คำศัพท์'][x] :
            del voca_list[x]
            del type_list[x]
            del mean_list[x]
            break
   
while True :
    print('พจนานุกรม')
    menu()
    if choose == 1 :
        os.system('cls')
        print('กรุณาเลือกประเภทรายการ : 1')
        add_def()
    elif choose == 2 :
        os.system('cls')
        print('กรุณาเลือกประเภทรายการ : 2')
        show_def()
    elif choose == 3 :
        os.system('cls')
        print('กรุณาเลือกประเภทรายการ : 3')
        delete_def()
    elif choose == 4 :
        os.system('cls')
        print('กรุณาเลือกประเภทรายการ : 4')
        out_pro = input('ต้องการออกจากโปรแกรมใช่หรือไม่ (y/n) : ')
        if out_pro == 'y' :
            print('ปิดโปรแกรมเรียบร้อยแล้ว')
            break
        elif out_pro == 'n' :
            os.system('cls')