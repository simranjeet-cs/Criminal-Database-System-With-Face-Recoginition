from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View Category', font=('arial', 28, 'bold'))
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb1 = Label(self.f, text="Search Name", font=('arial', 14))
        self.txt1 = Entry(self.f, font=('arial', 14), width=30)
        self.btn1 = Button(self.f, text="Search", font=('arial', 14), command=self.searchCategory)
        self.btn2 = Button(self.f, text="Refresh", font=('arial', 14), command=self.refresh)
        self.lb1.grid(row=0, column=0, padx=10)
        self.txt1.grid(row=0, column=1, padx=10)
        self.btn1.grid(row=0, column=2, padx=10)
        self.btn2.grid(row=0, column=3, padx=10)

        self.categoryTable = ttk.Treeview(self.root, columns=('name', 'description'))
        self.categoryTable.pack(pady=10, padx=20,expand=True, fill='both')

        self.categoryTable.heading('name', text='Name')
        self.categoryTable.heading('description', text='Description')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14))

        self.categoryTable['show'] = 'headings'
        self.getValues()

        self.root.mainloop()

    def refresh(self):
        self.txt1.delete(0,'end')
        self.getValues()

    def searchCategory(self):
        text = self.txt1.get()
        q = f"select name, description from add_category where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.categoryTable.get_children():
            self.categoryTable.delete(k)
            # print(k)
        for i in data:
            self.categoryTable.insert('', index=0, values=i)



    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select name, description from add_category"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.categoryTable.get_children():
            self.categoryTable.delete(k)
            # print(k)
        for i in data:
            self.categoryTable.insert('', index=0, values=i)


#obj = Main()