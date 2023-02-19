from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox

GUI = Tk() #หน้าจอหลัก
GUI.title('โปรแกรมบันทึกข้อมูล') #ชิ้อโปรแกรม
GUI.geometry('500x400') #กว้างxสูง

B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท?')
B1.pack(ipadx=20,ipady=20)

#################
def Button2():
    text = 'ตอนนี้มีเงินนในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท?',command=Button2)
B2.pack(ipadx=20,ipady=20)
#################


GUI.mainloop()
