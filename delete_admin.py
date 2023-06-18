from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')

        self.mainLabel = Label(self.root, text='View Admins', font=('arial', 28, 'bold'))
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb1 = Label(self.f, text="Search Name", font=('arial', 14))
        self.txt1 = Entry(self.f, font=('arial', 14), width=30)
        self.btn1 = Button(self.f, text="Search", font=('arial', 14), command=self.searchAdmin)
        self.btn2 = Button(self.f, text="Refresh", font=('arial', 14), command=self.refresh)
        self.lb1.grid(row=0, column=0, padx=10)
        self.txt1.grid(row=0, column=1, padx=10)
        self.btn1.grid(row=0, column=2, padx=10)
        self.btn2.grid(row=0, column=3, padx=10)

        self.adminTable = ttk.Treeview(self.root, columns=('id', 'name', 'email', 'mobile', 'role'))
        self.adminTable.pack(pady=10, padx=20,expand=True, fill='both')

        self.adminTable.heading('id', text='ID')
        self.adminTable.heading('name', text='Name')
        self.adminTable.heading('email', text='Email')
        self.adminTable.heading('mobile', text='Mobile')
        self.adminTable.heading('role', text='Role')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14))

        self.adminTable['show'] = 'headings'
        self.getValues()

        self.delBtn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.delAdmin)
        self.delBtn.pack(pady=20)

        self.root.mainloop()


    def delAdmin(self):
        rowid = self.adminTable.selection()[0]
        data = self.adminTable.item(rowid)
        selectedAdmin = data['values']
        adminID = selectedAdmin[0]
        q = f"delete from add_admin where id='{adminID}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Admin deleted Successfully", parent=self.root)
        self.getValues()


    def refresh(self):
        self.txt1.delete(0,'end')
        self.getValues()

    def searchAdmin(self):
        text = self.txt1.get()
        q = f"select id, name, email,mobile, role from add_admin where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.adminTable.get_children():
            self.adminTable.delete(k)
            # print(k)
        for i in data:
            self.adminTable.insert('', index=0, values=i)



    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select id, name, email,mobile, role from add_admin"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.adminTable.get_children():
            self.adminTable.delete(k)
            # print(k)
        for i in data:
            self.adminTable.insert('', index=0, values=i)


# obj = Main()