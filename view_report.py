from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect
from tkinter.filedialog import askopenfilename
import cv2
import random

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View Reports', font=('arial', 28, 'bold'))
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb1 = Label(self.f, text="Search Culprit Name", font=('arial', 14))
        self.txt1 = Entry(self.f, font=('arial', 14), width=30)
        self.btn1 = Button(self.f, text="Search", font=('arial', 14), command=self.searchReport)
        self.btn2 = Button(self.f, text="Refresh", font=('arial', 14), command=self.refresh)
        self.lb1.grid(row=0, column=0, padx=10)
        self.txt1.grid(row=0, column=1, padx=10)
        self.btn1.grid(row=0, column=2, padx=10)
        self.btn2.grid(row=0, column=3, padx=10)

        self.reportTable = ttk.Treeview(self.root, columns=('id', 'tittle', 'description', 'date', 'culprit_name', 'mobile', 'email', 'address', 'image'))
        self.reportTable.pack(pady=10, padx=20,expand=True, fill='both')

        self.reportTable.heading('id', text='ID')
        self.reportTable.heading('tittle', text='Tittle')
        self.reportTable.heading('description', text='Description')
        self.reportTable.heading('culprit_name', text='Culprit Name')
        self.reportTable.heading('mobile', text='Mobile')
        self.reportTable.heading('email', text='Email')
        self.reportTable.heading('address', text='Address')
        self.reportTable.heading('image', text='Image')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14))

        self.reportTable['show'] = 'headings'
        self.getValues()

        self.root.mainloop()

    def refresh(self):
        self.txt1.delete(0,'end')
        self.getValues()

    def searchReport(self):
        text = self.txt1.get()
        q = f"select id, tittle, description, date, culprit_name, mobile, email, address, image from reports where culprit_name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.reportTable.get_children():
            self.reportTable.delete(k)
            # print(k)
        for i in data:
            self.reportTable.insert('', index=0, values=i)


    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select id, tittle, description, date, culprit_name, mobile, email, address, image from reports"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.reportTable.get_children():
            self.reportTable.delete(k)
            # print(k)
        for i in data:
            self.reportTable.insert('', index=0, values=i)


#obj = Main()