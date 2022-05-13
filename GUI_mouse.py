import imp
from tkinter import * #Lib: Tk Interface
import pyautogui as pg
from tkinter import ttk
import webbrowser

GUI = Tk()
GUI.title('โปรแกรมสั่งกดปฏิทิน')
GUI.geometry('500x300')

def Calender():
    pg.click(1318,750)

def Google():
    webbrowser.open('https://www.google.com')


B1 = Button(GUI,text='Calender1',command=Calender)
B1.pack(ipadx=20,ipady=10, pady=20)

B2 = ttk.Button(GUI,text='Calender2',command=Calender)
B2.pack(ipadx=20,ipady=10, pady=20)

B3 = ttk.Button(GUI,text='Google',command=Google)
B3.pack(ipadx=20,ipady=10, pady=20)

GUI.mainloop()