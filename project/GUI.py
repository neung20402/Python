import sqlite3
from tkinter import *
from PIL import Image , ImageTk
from datetime import datetime
from tkinter import ttk,messagebox

conn = sqlite3.connect (r"C:\Users\acer\Documents\Sakphichet_Python\project\Data.db")
c = conn.cursor()

root = Tk()
Frame(root,width=1550,height=75,bg='#CC66FF').pack(fill=BOTH,expand=TRUE)
root.minsize(width=1525, height=780)
root.geometry('1525x780+0+0')
root.update()

FONT1 = ('Angsana New',25)
FONT2 = ('Angsana New',18)

root.title('ร้านเช่าหนังสือ')
Label(root, text='โปรแกรมร้านเช่าหนังสือ',font=FONT1,bg='#CC66FF').place(x=600,y=10)

style = ttk.Style()
style.configure("Treeview.Heading", font=FONT2)

##################################Tab###################################################################

Tab = ttk.Notebook(root)
Tab.pack(fill=BOTH,expand=TRUE)

ShBook = Frame(Tab)
ShBook.pack(fill=BOTH,expand=TRUE)
ShSeBook = Frame(Tab)

canvas1 = Canvas(ShBook, bg='lightsteelblue', width=root.winfo_width(), height=root.winfo_height())
canvas1.pack()

canvas2 = Canvas(ShSeBook, bg='lightsteelblue', width=root.winfo_width(), height=root.winfo_height())
canvas2.pack()

Tab.add(ShBook,text='Book')
Tab.add(ShSeBook,text='Show Select')

###################################################################################

c.execute ('''SELECT UserName FROM NewLogin''')
name_user = c.fetchall()
for i in range(len(name_user)) :
    userName = name_user[i]
    UserName = userName[0]
show_user = 'บัญชีผู้ใช้งาน : '+str(UserName)
Label(root, text=show_user,font=('Angsana New',15),bg='#CC66FF').place(x=1200,y=15)


def Logout() :
    endTime = datetime.now()
    all_ID = len(name_user)
    sql = '''UPDATE NewLogin SET EndTime = ? WHERE ID = ?'''
    c.execute (sql,(endTime,all_ID))
    conn.commit()
    messagebox.showinfo('Alert','Logout completed')
    root.destroy()
    import Login

Button(root,text='Logout',font=('Angsana New',15),command=Logout,bg='royalblue',fg='white').place(x=1370,y=5)

####################################ShowBook##############################################

images = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20']
AddBook_list = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,'']
img_list = []
New_balance = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def picture() :
    x,y=100,50
    for n in range(1,21) :
        img_list.append(ImageTk.PhotoImage(Image.open(f"C:\\Users\\acer\\Documents\\Sakphichet_Python\\project\\Picture\\{images[n-1]}.png")))
        showpic = Label(ShBook,image=img_list[n-1],bg='black')
        canvas1.create_window(x, y, window=showpic, anchor=NW)
        y+=200

def namebook() :
    x,y=350,50
    for n in range(1,21) :
        sql = '''SELECT NameBook FROM BookData WHERE ID = ?'''
        c.execute (sql,(str(n),))
        name_list = c.fetchone()
        name = StringVar()
        name.set(name_list[0])
        showname = Label(ShBook,textvariable=name,font=FONT2,bg='lightsteelblue')
        canvas1.create_window(x, y, window=showname, anchor=NW)
        y+=200

def balance():
    x,y=350,150
    for n in range(1,21) :
        c.execute ('''SELECT Balance FROM BookData WHERE ID = ?''',(str(n),))
        num_list = c.fetchone()
        show_text = StringVar()
        text_balance = 'สินค้าคงเหลือ '+str(num_list[0])+' ชิ้น'
        show_text.set(text_balance)
        show_balance = Label(ShBook,text=show_text.get(),font=('Angsana New',15),bg='lightsteelblue')
        canvas1.create_window(x, y, window=show_balance, anchor=NW)
        y+=200
    
def AddBook() :
    global num1,num2,num3,num4,num5,num6,num7,num8,num9,num10,num11,num12,num13,num14,num15,num16,num17,num18,num19,num20
    x,y=950,100
    NumAdd1 = IntVar()
    num1 = Entry(ShBook,textvariable=NumAdd1,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num1, anchor=NW)
    y+=200
    NumAdd2 = IntVar()
    num2 = Entry(ShBook,textvariable=NumAdd2,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num2, anchor=NW)
    y+=200
    NumAdd3 = IntVar()
    num3 = Entry(ShBook,textvariable=NumAdd3,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num3, anchor=NW)
    y+=200
    NumAdd4 = IntVar()
    num4 = Entry(ShBook,textvariable=NumAdd4,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num4, anchor=NW)
    y+=200
    NumAdd5 = IntVar()
    num5 = Entry(ShBook,textvariable=NumAdd5,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num5, anchor=NW)
    y+=200
    NumAdd6 = IntVar()
    num6 = Entry(ShBook,textvariable=NumAdd6,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num6, anchor=NW)
    y+=200
    NumAdd7 = IntVar()
    num7 = Entry(ShBook,textvariable=NumAdd7,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num7, anchor=NW)
    y+=200
    NumAdd8 = IntVar()
    num8 = Entry(ShBook,textvariable=NumAdd8,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num8, anchor=NW)
    y+=200
    NumAdd9 = IntVar()
    num9 = Entry(ShBook,textvariable=NumAdd9,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num9, anchor=NW)
    y+=200
    NumAdd10 = IntVar()
    num10 = Entry(ShBook,textvariable=NumAdd10,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num10, anchor=NW)
    y+=200
    NumAdd11 = IntVar()
    num11 = Entry(ShBook,textvariable=NumAdd11,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num11, anchor=NW)
    y+=200
    NumAdd12 = IntVar()
    num12 = Entry(ShBook,textvariable=NumAdd12,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num12, anchor=NW)
    y+=200
    NumAdd13 = IntVar()
    num13 = Entry(ShBook,textvariable=NumAdd13,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num13, anchor=NW)
    y+=200
    NumAdd14 = IntVar()
    num14 = Entry(ShBook,textvariable=NumAdd14,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num14, anchor=NW)
    y+=200
    NumAdd15 = IntVar()
    num15 = Entry(ShBook,textvariable=NumAdd15,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num15, anchor=NW)
    y+=200
    NumAdd16 = IntVar()
    num16 = Entry(ShBook,textvariable=NumAdd16,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num16, anchor=NW)
    y+=200
    NumAdd17 = IntVar()
    num17 = Entry(ShBook,textvariable=NumAdd17,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num17, anchor=NW)
    y+=200
    NumAdd18 = IntVar()
    num18 = Entry(ShBook,textvariable=NumAdd18,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num18, anchor=NW)
    y+=200
    NumAdd19 = IntVar()
    num19 = Entry(ShBook,textvariable=NumAdd19,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num19, anchor=NW)
    y+=200
    NumAdd20 = IntVar()
    num20 = Entry(ShBook,textvariable=NumAdd20,font=FONT2,width=20)
    canvas1.create_window(x, y, window=num20, anchor=NW)
    Button(ShBook,text='บันทึกจำนวน',font=('Angsana New',15),command=Get_NumBook,bg='royalblue',fg='white').place(x=1300,y=50)

def Get_NumBook() :
    AddBook_list[0] = int(num1.get())
    AddBook_list[1] = int(num2.get())
    AddBook_list[2] = int(num3.get())
    AddBook_list[3] = int(num4.get())
    AddBook_list[4] = int(num5.get())
    AddBook_list[5] = int(num6.get())
    AddBook_list[6] = int(num7.get())
    AddBook_list[7] = int(num8.get())
    AddBook_list[8] = int(num9.get())
    AddBook_list[9] = int(num10.get())
    AddBook_list[10] = int(num11.get())
    AddBook_list[11] = int(num12.get())
    AddBook_list[12] = int(num13.get())
    AddBook_list[13] = int(num14.get())
    AddBook_list[14] = int(num15.get())
    AddBook_list[15] = int(num16.get())
    AddBook_list[16] = int(num17.get())
    AddBook_list[17] = int(num18.get())
    AddBook_list[18] = int(num19.get())
    AddBook_list[19] = int(num20.get())
    AddBook_list[20] = str(UserName)
    for i in range(20):
        c.execute ('''SELECT Balance FROM BookData WHERE ID = ?''',(str(i+1),))
        balance_check = c.fetchone()
        if int(AddBook_list[i]) > balance_check[0] :
            messagebox.showinfo('ใส่จำนวนผิดพลาด','จำนวนหนังสือที่ท่านเพิ่มมีมากกว่าจำนวนคงเหลือในคลัง กรุณาแก้ไข')
            break
        elif int(AddBook_list[i]) < 0 :
            messagebox.showinfo('ใส่จำนวนผิดพลาด','จำนวนหนังสือไม่สามารถน้อยกว่า 0 ได้ กรุณาแก้ไข')
            break
        Select_book()

def re_balance() :
    for i in range(20) :
        sql = '''UPDATE BookData SET Balance = ? WHERE ID = ?'''
        Reset_balance = (20,str(i+1),)
        c.execute(sql,Reset_balance)
        conn.commit()
        c.execute ('''SELECT Balance FROM BookData WHERE ID = ?''',(str(i+1),))
        balance_check = c.fetchone()
        New_balance[i] = balance_check[0] - AddBook_list[i]
        sql = '''UPDATE BookData SET Balance = ? WHERE ID = ?'''
        Set_balance = (New_balance[i],str(i+1),)
        c.execute(sql,Set_balance)
        conn.commit()

c.execute('''SELECT NameBook FROM BookData''')
n1=c.fetchall()
y=(200*len(n1))+100
scrollbar = Scrollbar(canvas1, orient=VERTICAL, command=canvas1.yview)
scrollbar.place(relx=1, rely=0, relheight=1, anchor=NE)
canvas1.config(yscrollcommand=scrollbar.set, scrollregion=(0, 0, 0, y))

#############################################ShowSelectBook###############################
header = ['ID','Book Title','Volume','Price']
headerSize = [50,650,350,350]

Show_Select = ttk.Treeview(ShSeBook,columns=header,show='headings',height=25)
Show_Select.place(x=55,y=20)

for h,s in zip(header,headerSize):
	Show_Select.heading(h,text=h)
	Show_Select.column(h,width=s)

def Select_book() :
    allPrice = 0
    c.execute("SELECT ID,NameBook FROM Bookdata")
    Show_se = c.fetchall()
    Show_Select.delete(*Show_Select.get_children())
    for i,bookTit in enumerate(Show_se) :
        c.execute ('''SELECT Price FROM BookData WHERE ID = ?''',(str(i+1),))
        calcu = c.fetchone()
        bookTit_list = list(bookTit)
        bookTit_list.append(AddBook_list[i])
        price = calcu[0]*AddBook_list[i]
        allPrice += price
        bookTit_list.append(price)
        Show_Select.insert('','end',value=bookTit_list) 
    Show_Select.insert('','end',value=('','','','รวม '+str(allPrice)+' บาท'))    
    
def pay() :
    UpToDate =  '''UPDATE UserRent SET Book1=?,Book2=?,Book3=?,Book4=?,Book5=?,Book6=?,Book7=?,Book8=?,Book9=?,Book10=?,
        Book11=?,Book12=?,Book13=?,Book14=?,Book15=?,Book16=?,Book17=?,Book18=?,Book19=?,Book20=? WHERE UserID = ?'''
    c.execute(UpToDate,tuple(AddBook_list))
    conn.commit()
    re_balance()
    balance()

Button(ShSeBook,text='ยืนยันการเช่า',font=('Angsana New',15),command=pay,bg='royalblue',fg='white').place(x=1300,y=600)

picture()
namebook()
balance()
AddBook()
Select_book()
root.mainloop()