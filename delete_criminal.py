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

        self.mainLabel = Label(self.root, text='View Criminals', font=('arial', 28, 'bold'))
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

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
        self.getValues()

        self.delBtn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.delCriminal)
        self.delBtn.pack(pady=20)

        self.root.mainloop()


    def delCriminal(self):
        rowid = self.criminalTable.selection()[0]
        data = self.criminalTable.item(rowid)
        selectedCriminal = data['values']
        criminalID = selectedCriminal[0]
        q = f"delete from criminals where id='{criminalID}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Criminal deleted Successfully", parent=self.root)
        self.getValues()


    def refresh(self):
        self.txt1.delete(0,'end')
        self.getValues()

    def searchCriminal(self):
        text = self.txt1.get()
        q = f"select id, name, father_name, mobile, email, address, image from criminals where name like '%{text}%'"
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
        q = f"select id, name, father_name, mobile, email, address, image from criminals"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.criminalTable.get_children():
            self.criminalTable.delete(k)
            # print(k)
        for i in data:
            self.criminalTable.insert('', index=0, values=i)


#obj = Main()