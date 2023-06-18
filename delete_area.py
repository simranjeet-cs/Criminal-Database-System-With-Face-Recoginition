from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View Areas', font=('arial', 28, 'bold'))
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb1 = Label(self.f, text="Search Name", font=('arial', 14))
        self.txt1 = Entry(self.f, font=('arial', 14), width=30)
        self.btn1 = Button(self.f, text="Search", font=('arial', 14), command=self.searchArea)
        self.btn2 = Button(self.f, text="Refresh", font=('arial', 14), command=self.refresh)
        self.lb1.grid(row=0, column=0, padx=10)
        self.txt1.grid(row=0, column=1, padx=10)
        self.btn1.grid(row=0, column=2, padx=10)
        self.btn2.grid(row=0, column=3, padx=10)

        self.areaTable = ttk.Treeview(self.root, columns=('name', 'city', 'state', 'landmark'))
        self.areaTable.pack(pady=10, padx=20,expand=True, fill='both')

        self.areaTable.heading('name', text='Name')
        self.areaTable.heading('city', text='city')
        self.areaTable.heading('state', text='State')
        self.areaTable.heading('landmark', text='Landmark')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14))

        self.areaTable['show'] = 'headings'
        self.getValues()

        self.delBtn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.delArea)
        self.delBtn.pack(pady=20)

        self.root.mainloop()


    def delArea(self):
        name = self.areaTable.selection()[0]
        data = self.areaTable.item(name)
        selectedArea = data['values']
        Name = selectedArea[0]
        q = f"delete from add_area where name='{Name}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Area deleted Successfully", parent=self.root)
        self.getValues()


    def refresh(self):
        self.txt1.delete(0,'end')
        self.getValues()

    def searchArea(self):
        text = self.txt1.get()
        q = f"select name, city, state, landmark from add_area where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.areaTable.get_children():
            self.areaTable.delete(k)
            # print(k)
        for i in data:
            self.areaTable.insert('', index=0, values=i)



    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select name, city, state, landmark from add_area"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.areaTable.get_children():
            self.areaTable.delete(k)
            # print(k)
        for i in data:
            self.areaTable.insert('', index=0, values=i)


# obj = Main()