from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View locations', font=('arial', 28, 'bold'))
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb1 = Label(self.f, text="Search Name", font=('arial', 14))
        self.txt1 = Entry(self.f, font=('arial', 14), width=30)
        self.btn1 = Button(self.f, text="Search", font=('arial', 14), command=self.searchLocation)
        self.btn2 = Button(self.f, text="Refresh", font=('arial', 14), command=self.refresh)
        self.lb1.grid(row=0, column=0, padx=10)
        self.txt1.grid(row=0, column=1, padx=10)
        self.btn1.grid(row=0, column=2, padx=10)
        self.btn2.grid(row=0, column=3, padx=10)

        self.locationTable = ttk.Treeview(self.root, columns=('name', 'description', 'area', 'timings'))
        self.locationTable.pack(pady=10, padx=20,expand=True, fill='both')

        self.locationTable.heading('name', text='Name')
        self.locationTable.heading('description', text='Description')
        self.locationTable.heading('area', text='Area')
        self.locationTable.heading('timings', text='Timings')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14))

        self.locationTable['show'] = 'headings'
        self.getValues()

        self.root.mainloop()

    def refresh(self):
        self.txt1.delete(0,'end')
        self.getValues()

    def searchLocation(self):
        text = self.txt1.get()
        q = f"select name, description, area, timings from surveilance_location where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.locationTable.get_children():
            self.locationTable.delete(k)
            # print(k)
        for i in data:
            self.locationTable.insert('', index=0, values=i)



    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select name, description, area, timings from surveilance_location"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.locationTable.get_children():
            self.locationTable.delete(k)
            # print(k)
        for i in data:
            self.locationTable.insert('', index=0, values=i)


#obj = Main()