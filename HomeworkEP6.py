# HomeworkEP6.py
# โปรแกรมคำนวณ หา ค่าน้ำหนักสูงสุดที่คานจะรับได้

from email import message
from tkinter import *
from tkinter import ttk , PhotoImage
from tkinter import font
from tkinter import messagebox

def Cal():
    try:
        L=int(v_length.get())
        E=int(v_elasticity.get())
        I=int(v_inertia.get())
        if L and E and I != 0 :
            CalP = (E*I)/((L**2)*120)
            messagebox.showinfo('น้ำหนักสูงสุดที่คานสามารถรับได้ Pmax','ค่าของน้ำหนักคือ {:2f} kN'.format(CalP))
        else:
            messagebox.showwarning('ข้อมูลไม่ถูกต้อง','กรุณาระบุตัวเลขที่ไม่ใช่ 0 ก่อนทำการคำนวณ')
    except:
        messagebox.showwarning('ใส่ค่าไม่ถูกต้อง','กรุณาใส่เฉพาะตัวเลข')
        

GUI = Tk()

GUI.title('Software Calculate Maximum Load on Beam')
GUI.geometry('1000x450')

L1 = Label(GUI,text=' โปรแกรมคำนวณน้ำหนักสูงสุดที่คานสามารถรับได้ ',font=(None,40))
L1.pack()

bg = PhotoImage(file='Beam.png')
BG = Label(GUI,image=bg)
BG.pack(side=RIGHT)

L1 = Label(GUI,text='ค่าความยาวของคาน,L (m)',font=(None,20))
L1.pack()

v_length = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_length,font=(None,20))
E1.pack()

L2 = Label(GUI,text='ค่ามอดูลัสของสภาพยืดหยุ่นของคาน,E (GPa)',font=(None,20))
L2.pack()

v_elasticity = StringVar()
E2 = ttk.Entry(GUI,textvariable=v_elasticity,font=(None,20))
E2.pack()

L3 = Label(GUI,text='โมเมนต์ความเฉื่อยคาน,I (10^6 mm^4)',font=(None,20))
L3.pack()

v_inertia = StringVar()
E3 = ttk.Entry(GUI,textvariable=v_inertia,font=(None,20))
E3.pack()
   
      
B = ttk.Button(GUI, text='คำนวณ',command=Cal)
B.pack(ipadx=30,ipady=20,pady=20) 

L4 = Label(GUI,text='โดยกำหนดให้ระยะโก่งตัวของคานไม่เกิน L/360',font=(None,20))
L4.pack()

GUI.mainloop()