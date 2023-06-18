from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg

import openslips
from connection import connect
from tkinter.filedialog import askopenfilename
import cv2
import random

class Main:
    def __init__(self):
        self.root = Toplevel()
        self.root.state('zoomed')
        self.root.configure(bg="black")

        self.mainLabel = Label(self.root, text='View Criminals', font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        font = ('calibri', 14)

        self.lb1 = Label(self.f, text="Search Name", font=('arial', 14))
        self.txt1 = Entry(self.f, font=('arial', 14), width=30)
        self.btn1 = Button(self.f, text="Search", font=('arial', 14), command=self.searchCriminal)
        self.btn2 = Button(self.f, text="Refresh", font=('arial', 14), command=self.refresh)
        self.lb1.grid(row=0, column=0, padx=10)
        self.txt1.grid(row=0, column=1, padx=10)
        self.btn1.grid(row=0, column=2, padx=10)
        self.btn2.grid(row=0, column=3, padx=10)

        self.criminalTable = ttk.Treeview(self.root, columns=('id', 'name', 'father_name', 'mobile', 'email', 'address', 'image'))
        self.criminalTable.pack(pady=10, padx=20,expand=True, fill='both')

        self.criminalTable.heading('id', text='ID')
        self.criminalTable.heading('name', text='Name')
        self.criminalTable.heading('father_name', text='Father Name')
        self.criminalTable.heading('mobile', text='Mobile')
        self.criminalTable.heading('email', text='Email')
        self.criminalTable.heading('address', text='Address')
        self.criminalTable.heading('image', text='Image')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14))

        self.criminalTable['show'] = 'headings'
        self.criminalTable.bind("<Double-1>", self.makePoster)
        self.getValues()

        Label(self.root, text="Double Click to Create a Wanted Poster", font=('arial', 14)).pack(pady=20)

        self.btn1.bind("<Enter>", self.on_enter_btn1)
        self.btn1.bind("<Leave>", self.on_leave_btn1)
        self.btn2.bind("<Enter>", self.on_enter_btn2)
        self.btn2.bind("<Leave>", self.on_leave_btn2)
        self.mainLabel.bind("<Enter>", self.on_enter_mainLabel)
        self.mainLabel.bind("<Leave>", self.on_leave_mainLabel)

        self.root.mainloop()

    def on_enter_btn1(self, event):
        self.btn1.configure(bg='grey', fg='white')

    def on_leave_btn1(self, event):
        self.btn1.configure(bg='SystemButtonFace', fg='black')

    def on_enter_btn2(self, event):
        self.btn2.configure(bg='grey', fg='white')

    def on_leave_btn2(self, event):
        self.btn2.configure(bg='SystemButtonFace', fg='black')

    def on_enter_mainLabel(self, event):
        self.mainLabel.configure(bg='grey', fg='white')

    def on_leave_mainLabel(self, event):
        self.mainLabel.configure(bg='SystemButtonFace', fg='black')

    def makePoster(self, event):
        data = self.criminalTable.item(self.criminalTable.selection()[0])['values']
        openslips.makePDF(data)

    def refresh(self):
        self.txt1.delete(0,'end')
        self.getValues()

    def searchCriminal(self):
        text = self.txt1.get()
        q = f"select id, name,  father_name, mobile, email, address, image from criminals where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.criminalTable.get_children():
            self.criminalTable.delete(k)
            # print(k)
        for i in data:
            self.criminalTable.insert('', index=0, values=i)


    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select id, name,  father_name, mobile, email, address, image from criminals"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.criminalTable.get_children():
            self.criminalTable.delete(k)
            # print(k)
        for i in data:
            self.criminalTable.insert('', index=0, values=i)

#if __name__ == '__main__':
# x = Main()