from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect


class Main():



    def __init__(self):

        self.root = Tk()
        self.root.geometry("900x800")
        self.root.state('zoomed')

        self.mainlabel = Label(self.root, text="View Center", font=("arial",24,"bold"))
        self.mainlabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb11 = Label(self.f, text="Search Name", font=("arial",14))
        self.lb11.grid(row=0, column=0, padx=10)

        self.txt11 = Entry(self.f, font=("arial", 14), width=30)
        self.txt11.grid(row=0, column=1, padx=10)

        self.bt1=Button(self.f, text="Search", font=("arial", 14), command=self.searchCenter)
        self.bt1.grid(row=0, column=2, padx=10)

        self.bt2 = Button(self.f, text="Refresh", font=("arial", 14), command=self.refresh)
        self.bt2.grid(row=0, column=3, padx=10)

        self.centerTable = ttk.Treeview(self.root, columns=('id', 'name', 'email', 'mobile','area', 'location'))
        self.centerTable.pack(pady=10, padx=20, expand=True, fill='both')

        self.centerTable.heading('id', text='ID')
        self.centerTable.heading('name', text='Name')
        self.centerTable.heading('email', text='Email')
        self.centerTable.heading('mobile', text='Mobile')
        self.centerTable.heading('area', text='AREA')
        self.centerTable.heading('location', text='LOCATION')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14), rowheight=40)

        self.centerTable['show'] = 'headings'
        self.getValues()

        self.root.mainloop()

    def refresh(self):
        self.txt11.delete(0, 'end')
        self.getValues()

    def searchCenter(self):
        text = self.txt11.get()
        q = f"select id, name, email, mobile, area, location from center where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.centerTable.get_children():
            self.centerTable.delete(k)
        for i in data:
            self.centerTable.insert('', index=0, values=i)

    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select id, name, email, mobile, area, location from center"
        self.cr.execute(q)
        data = self.cr.fetchall()
        for k in self.centerTable.get_children():
            self.centerTable.delete(k)
        for i in data:
            self.centerTable.insert('', index=0, values=i)


# obj = Main()