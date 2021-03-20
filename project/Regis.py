from tkinter import ttk, messagebox
from tkinter import *
import sqlite3
from datetime import datetime

conn = sqlite3.connect (r"C:\Users\acer\Documents\Sakphichet_Python\project\Data.db")
c = conn.cursor()
u = conn.cursor()
p = conn.cursor()

window = Tk()
window.minsize(width=650, height=500)
window.maxsize(width=650, height=500)
window.title('ร้านขายหนังสือ')
window.geometry('650x300+500+200')

############################login#################################

def regis() :
    u.execute ('''SELECT UserID FROM UsersData''')
    p.execute ('''SELECT Password FROM UsersData''')
    alluser = u.fetchall()
    user_list = []
    for x in range(len(alluser)) :
        user_list.append(alluser[x][0])
    try_ex()
    if test_type == 1:
        if user_box.get() in user_list :
            messagebox.showinfo('Alert','มีบัญชีผู้ใช้งานอยู่แล้ว')
        elif Fname_box.get() or Lname_box.get() or Address_box.get() or Credit_box.get() or user_box.get() or pass_box.get() or conPass_box.get() == '' :
            messagebox.showerror('Alert','กรุณากรอกข้อมูลให้ครบ')
        elif pass_box.get() != '' and pass_box.get() != conPass_box.get() :
            messagebox.showerror('Alert','ยืนยันรหัสผ่านไม่ถูกต้อง')
        elif not user_box.get() in user_list and pass_box.get() != '' and pass_box.get() == conPass_box.get():
            messagebox.showinfo('Alert','สมัครเสร็จสิ้น')
            sql = '''INSERT INTO UsersData (Fname,Lname,Address,Credit,UserID,Password) VALUES (?,?,?,?,?,?)'''
            newUser = (Fname_box.get(),Lname_box.get(),Address_box.get(),Credit_box.get(),user_box.get(),pass_box.get())
            c.execute (sql,(newUser))
            sql = '''INSERT INTO UserRent (ID,UserName,UserID,Book1,Book2,Book3,Book4,Book5,Book6,Book7,Book8,Book9,Book10,Book11,Book12,
            Book13,Book14,Book15,Book16,Book17,Book18,Book19,Book20) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)'''
            NewBuy = ((len(alluser)+1),Fname_box.get(),user_box.get(),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0)
            c.execute(sql,NewBuy)
            conn.commit()
            window.destroy()
            import Login 
    else:
        messagebox.showinfo('Alert','ข้อมูลเครดิตต้องเป็นตัวเลขเท่านั้น')
   

def login() :
    window.destroy()
    import Login

def try_ex() :
    global test_type
    try :
        int(Credit_box.get())
        test_type = 1
    except : test_type = 0

Frame(window,width=650,height=500,bg='gray').place(x=0,y=0)

Label(window,text='เข้าสู่ระบบบัญชีผู้ใช้งาน',font=('Angsana New',25),bg='gray').place(x=230,y=10)
Button(window,text='ล็อคอิน',font=('Angsana New',12),command=login,width=10).place(x=550,y=5)

Label(window,text='ชื่อ',font=('Angsana New',15),bg='gray').place(x=140,y=70)
Fname_box = ttk.Entry(window,font=('Angsana New',15),width=30)
Fname_box.place(x=230,y=70)
Fname_box.focus()

Label(window,text='สกุล',font=('Angsana New',15),bg='gray').place(x=140,y=130)
Lname_box = ttk.Entry(window,font=('Angsana New',15),width=30)
Lname_box.place(x=230,y=130)

Label(window,text='ที่อยู่',font=('Angsana New',15),bg='gray').place(x=140,y=180)
Address_box = ttk.Entry(window,font=('Angsana New',15),width=30)
Address_box.place(x=230,y=180)

Label(window,text='เครดิต',font=('Angsana New',15),bg='gray').place(x=140,y=230)
Credit_box = ttk.Entry(window,font=('Angsana New',15),width=30)
Credit_box.place(x=230,y=230)

Label(window,text='ชื่อผู้ใช้งาน',font=('Angsana New',15),bg='gray').place(x=140,y=280)
user_box = ttk.Entry(window,font=('Angsana New',15),width=30)
user_box.place(x=230,y=280)

Label(window,text='รหัสผ่าน',font=('Angsana New',15),bg='gray').place(x=140,y=330)
pass_box = ttk.Entry(window,font=('Angsana New',15),width=30,show='*')
pass_box.place(x=230,y=330)

Label(window,text='ยืนยันรหัสผ่าน',font=('Angsana New',15),bg='gray').place(x=140,y=380)
conPass_box = ttk.Entry(window,font=('Angsana New',15),width=30,show='*')
conPass_box.place(x=230,y=380)

Button(window,text='สมัครบัญชี',font=('Angsana New',15),command=regis).place(x=300,y=430)

window.mainloop()