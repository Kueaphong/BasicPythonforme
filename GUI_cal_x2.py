#โปรแกรมยกกำลัง 2
from cProfile import label
from cgitb import text
import imp
from tkinter import *
from tkinter import ttk , messagebox
from tkinter import font

GUI = Tk() #T ตัวใหญ่ k ตัวเล็ก

GUI.title(' โปรแกรมยกกำลัง 2 ') #ตั้งชื่อโปรแกรม
GUI.geometry('700x600') #กำหนดขนาดหน้าต่างของโปรแกรม

bg = PhotoImage(file='x2-256x256.png')
bg = PhotoImage(file=r'C:\Users\TimeK\Desktop\Python\Basic\x2-256x256.png')
bg = PhotoImage(file='C:\\Users\\TimeK\\Desktop\\Python\\Basic\\x2-256x256.png')

BG = Label(GUI,image=bg) #แนะนำให้ set การตั้งค่าเพิ่มภาพแบบนี้
BG.pack()

L = Label(GUI,text='กรุณากรอกเลขฐาน',font=(None,20)) #font(ชนิดของfont,ขนาดของfont)
L.pack()

v_number = StringVar() #ตัวแปรที่ใช้เก็บของความจาก input
E1 = ttk.Entry(GUI, textvariable=v_number, font=(None,20))
E1.pack() # .pack() คือใส่ใน GUI

def Cal():
    try:
        num = float(v_number.get())
        calc = num**2
        messagebox.showinfo('ค่าที่ยกกำลังแล้ว','ค่า คือ {}'.format(calc))
    except:
        messagebox.showwarning('ใส่ค่าไม่ถูกต้อง','กรุณาใส่เฉพาะตัวเลข')
        v_number.set('') # set ค่าใหม่ที่ต้องการ
        E1.focus()

B = ttk.Button(GUI, text='คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=20,pady=20) # ipad x y คือ ขนาดปุ่ม pad x y ระยะห่าง

GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา