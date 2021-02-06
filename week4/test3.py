print('พจนานุกรม')
num = 0
q = 0
add_dict = {}
type_dict = {'n.':'คำนาม','v.':'คำกริยา','adj.':'คำคุณศัพท์','adv.':'คำกริยาวิเศษณ์'}
def menu() :
    global choose
    print('1.) เพิ่มคำศัพท์\n2.) แสดงคำศัพท์\n3.) ลบคำศัพท์\n4.) ออกจากโปรแกรม\n')
    choose = int(input('กรุณาเลือกประเภทรายการ : '))

def add_def() :
    add1 = input('เพิ่มคำศัพท์\t')
    add2 = input('ชนิดคำศัพท์(n. , v. , adj. , adv.)')
    add3 = input('ความหมาย\t')
    add_dict[add1]='คำศัพท์'
    add_dict[add2]='ชนิดคำศัพท์'
    add_dict[add3]='ความหมาย'
    print('เพิ่มคำศัพท์เรียบร้อยแล้ว')

def show_def() :
    global num
    global q
    for a in add_dict.values() :
        if a == 'คำศัพท์' :
            num = num + 1
    '''if num < 5 :
        print('-'*45)
        print(' '*10,'โปรดป้อนคำศัพท์อย่างน้อย 5 คำ')
        print('-'*45)'''
    #else :
    print('-'*45)
    print(' '*12,'คำศัพท์มีทั้งหมด ',int(num),' คำ')
    print('-'*45)
    print('\tความหมาย\tประเภท\t\tความหมาย')
    py_dict = list(add_dict.items())
    while True :
        q += 1
        for g,h in py_dict :
            print(g,h)
            for k,v in py_dict :
                del add_dict[k]
                add_dict[k]=v
                py_dict = list(add_dict.items())
                if v == 'คำศัพท์' :
                    print('\t',k,'\t',end=' ')
                if v == 'ชนิดคำศัพท์' :
                    for m in add_dict.keys() :
                        for o,r in type_dict.items() :
                            if m == o :
                                print(o,r,'\t',end=' ')
                if v == 'ความหมาย' :
                    print(k,'\t')
                print(py_dict[-1])
                print
            if py_dict[q+num] == py_dict[-1] :
                break
while True :
    menu()
    if choose == 1 :
        add_def()
    elif choose == 2 :
        show_def()
    elif choose == 4 :
        print('ปิดโปรแกรมเรียบร้อยแล้ว')
        break
