import os , sqlite3
def choose_def() :
    global choose
    choose = input('\tกรุณาเลือกทำรายการ :\t')
def show_desktop() :
    print('-'*10,'ระบบทะเบียนนักเรียน','-'*10)
    print('='*38)
    print('\tเพิ่มข้อมูลนักเรียน กด [a]\n\tแสดงข้อมูลนักเรียน กด [s]\n\tแก้ไขข้อมูลนักเรียน กด [e]\n\tลบข้อมูลนักเรียน กด [d]\n\tออกจากโปรแกรม กด [x]')
def input_data() :
    global text , name , sex , age , gyear , email
    data_input = input(('ชื่อ-นามสกุล:เพศ:อายุ:ระดับชั้น:อีเมลล์ พิมพ์ exit เพื่อออก \t'))
    text = data_input.split(':')
    if text[0] == 'exit' :
        os.system('cls')
    else :
        name = text[0]
        sex = text[1]
        age = text[2]
        gyear = text[3]
        email = text[4]
        insert_table(name,sex,age,gyear,email)
def input_data_2() :
    global data_input_2 , text , name , sex , age , gyear , email
    data_input_2 = input(('ชื่อ-นามสกุล:เพศ:อายุ:ระดับชั้น:อีเมลล์ \t'))
    text = data_input_2.split(':')
    name = text[0]
    sex = text[1]
    age = text[2]
    gyear = text[3]
    email = text[4]
def insert_table(Name,Sex,Age,Gyear,Email) :
    conn = sqlite3.connect (r'C:\Users\acer\Documents\Sakphichet_Python\week6\work6.db')
    c = conn.cursor()
    supinput = '''INSERT INTO data VALUES (NULL,?,?,?,?,?)'''
    insert_data = (Name,Sex,Age,Gyear,Email)
    c.execute(supinput,insert_data)
    conn.commit()
    conn.close()
def show_data_table() :
    conn = sqlite3.connect (r'C:\Users\acer\Documents\Sakphichet_Python\week6\work6.db')
    c = conn.cursor()
    c.execute ('''SELECT * FROM data''')
    d = conn.cursor()
    d.execute ('''SELECT ID FROM data''')
    numb = d.fetchall()
    result = c.fetchall()
    print('{0: <13}{1: <33}{2: <15}{3: <15}{4: <19}{5}'.format('ลำดับที่','ชื่อ-สกุล','เพศ','อายุ','ชั้นปี','อีเมลล์'))
    for x in range(0,len(numb)) :
        total = result[x]
        print('{0: <10}{1: <33}{2: <15}{3: <15}{4: <15}{5}'.format(total[0],total[1],total[2],total[3],total[4],total[5]))
def choose_ID() :
    global idchoose
    idchoose = input('เลือกลำดับที่ต้องการ กรอก 0 เพื่อยกเลิก: ')
def yousure() :
    global confirm
    confirm = input('ยืนยันการดำเนินการหรือไม่ [y/n] : ')
def modify_data() :
    choose_ID()
    if idchoose == '0' :
        os.system('cls')
    else :
        input_data_2()
        yousure()
        if confirm == 'y' :
            conn = sqlite3.connect (r'C:\Users\acer\Documents\Sakphichet_Python\week6\work6.db')
            c = conn.cursor()
            update_data = (name,sex,age,gyear,email,idchoose)
            c.execute ('''UPDATE data SET Name = ? , Sex = ? , Age = ? , GradeYear = ? , Email = ? WHERE ID = ?''',update_data)
            conn.commit()
            conn.close()
        elif confirm == 'n' :
            os.system('cls')
def del_data() :
    choose_ID()
    if idchoose == '0' :
        os.system('cls')
    else :
        yousure()
        if confirm == 'y' :
            conn = sqlite3.connect (r'C:\Users\acer\Documents\Sakphichet_Python\week6\work6.db')
            c = conn.cursor()
            c.execute ('''DELETE FROM data WHERE ID = ?''',idchoose)
            d = conn.cursor()
            d.execute ('''SELECT * FROM data''')
            setID = d.fetchall()
            update_ID = '''UPDATE data SET ID = ? WHERE ID = ?'''
            for x in range(0,len(setID)) :
                if x == (int(idchoose)-1) :
                    set_data = (str(x+1),str(int(idchoose)+1))
                    c.execute (update_ID,set_data)
                elif x > (int(idchoose)-1) :
                    set_data = (str(x),str(x+1))
                    c.execute (update_ID,set_data)
            conn.commit()
            conn.close()
        elif confirm == 'n' :
            os.system('cls')
def show_choose(Uschoose) :
    print('กรุณาเลือกทำรายการ :\t',Uschoose)
while True :
    show_desktop()
    choose_def()
    if choose == 'a' :
        os.system('cls')
        show_desktop()
        show_choose(choose)
        input_data()
    if choose == 's' :
        os.system('cls')
        show_desktop()
        show_choose(choose)
        show_data_table()
    if choose == 'e' :
        os.system('cls')
        show_desktop()
        show_choose(choose)
        modify_data()
    if choose == 'd' :
        os.system('cls')
        show_desktop()
        show_choose(choose)
        del_data()
    if choose == 'x' :
        os.system('cls')
        close_pro = input('ต้องการปิดโปรแกรมใช่หรือไม่ [y/n]')
        if close_pro == 'n' :
            os.system('cls')
        elif close_pro == 'y' :
            print('ปิดโปรแกรมเรียบร้อย')
            break