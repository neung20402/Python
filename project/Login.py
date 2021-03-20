from tkinter import ttk, messagebox
from tkinter import *
import sqlite3
from datetime import datetime

conn = sqlite3.connect (r"C:\Users\acer\Documents\Sakphichet_Python\project\Data.db")
c = conn.cursor()
u = conn.cursor()
p = conn.cursor()

window = Tk()
window.minsize(width=650, height=300)
window.maxsize(width=650, height=300)
window.title('ร้านขายหนังสือ')
window.geometry('650x300+500+200')

############################login#################################

def login(event=None) :
    u.execute ('''SELECT UserID FROM UsersData''')
    p.execute ('''SELECT Password FROM UsersData''')
    alluser = u.fetchall()
    allpass = p.fetchall()
    users = {}
    for x in range(len(alluser)) :
        user_list = alluser[x]
        pass_list = allpass[x]
        for i in range(len(user_list)) :
            users[user_list[i]]=pass_list[i]
    if user_box.get() in users and users[user_box.get()]==pass_box.get() :
        messagebox.showinfo('Alert','Login Sucess')
        sql = '''INSERT INTO NewLogin (UserName,StartTime,EndTime) VALUES (?,?,'')'''
        now = datetime.now()
        UserLogin = user_box.get()
        c.execute (sql,(UserLogin,now))
        conn.commit()
        window.destroy()
        import GUI  
    elif user_box.get() in users and users[user_box.get()]!=pass_box.get() :
        messagebox.showerror('Alert','Loging Error : Password is not correct')
        pass_box.focus()
    elif user_box.get() == '' or pass_box.get() == '' :
        messagebox.showerror('Alert','Login Error : Please enter information')
        user_box.focus()
    elif not user_box.get() in users :
        messagebox.showerror('Alert','Login Error : The user account could not be found')
        user_box.focus()

def Close_pro() :
    messagebox.showinfo('Alert','Close program completed')
    window.destroy()

def regis() :
    window.destroy()
    import Regis

Frame(window,width=650,height=300,bg='gray').place(x=0,y=0)

Label(window,text='เข้าสู่ระบบบัญชีผู้ใช้งาน',font=('Angsana New',25),bg='gray').place(x=230,y=10)

Label(window,text='ชื่อผู้ใช้งาน',font=('Angsana New',15),bg='gray').place(x=150,y=70)
user_box = ttk.Entry(window,font=('Angsana New',15),width=30)
user_box.place(x=230,y=70)
user_box.focus()

Label(window,text='รหัสผ่าน',font=('Angsana New',15),bg='gray').place(x=150,y=130)
pass_box = ttk.Entry(window,font=('Angsana New',15),width=30,show='*')
pass_box.place(x=230,y=130)

Button(window,text='เข้าสู่ระบบ',font=('Angsana New',15),command=login).place(x=300,y=190)
Button(window,text='สมัครบัญชีผู้ใช้',font=('Angsana New',15),command=regis).place(x=290,y=240)
Button(window,text='ปิดโปรแกรม',font=('Angsana New',12),command=Close_pro,width=10).place(x=550,y=5)

user_box.bind('<Return>',login)
pass_box.bind('<Return>',login)

window.mainloop()