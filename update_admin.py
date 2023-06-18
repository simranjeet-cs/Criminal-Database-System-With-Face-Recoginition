from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect, verifyemail, verifymobile

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.configure(bg="black")

        self.mainLabel = Label(self.root, text=' View Admins ', font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        font = ('calibri', 14)

        self.lb1 = Label(self.f, text="Search Name", font=('arial', 14))
        self.txt1 = Entry(self.f, font=('arial', 14), width=30)
        self.btn1 = Button(self.f, text="Search", font=('arial', 14), width=20, command=self.searchAdmin)
        self.btn2 = Button(self.f, text="Refresh", font=('arial', 14), width=20, command=self.refresh)
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
        self.adminTable.bind("<Double-1>", self.openUpdateWindow)

        self.delBtn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.delAdmin)
        self.delBtn.pack(pady=20)

        self.delBtn.bind("<Enter>", self.on_enter_delBtn)
        self.delBtn.bind("<Leave>", self.on_leave_delBtn)
        self.mainLabel.bind("<Enter>", self.on_enter_mainLabel)
        self.mainLabel.bind("<Leave>", self.on_leave_mainLabel)
        self.btn1.bind("<Enter>", self.on_enter_btn1)
        self.btn1.bind("<Leave>", self.on_leave_btn1)
        self.btn2.bind("<Enter>", self.on_enter_btn2)
        self.btn2.bind("<Leave>", self.on_leave_btn2)

        self.root.mainloop()

    def on_enter_delBtn(self, event):
        self.delBtn.configure(bg='grey', fg='white')

    def on_leave_delBtn(self, event):
        self.delBtn.configure(bg='SystemButtonFace', fg='black')
    def on_enter_mainLabel(self, event):
        self.mainLabel.configure(bg='grey', fg='white')

    def on_leave_mainLabel(self, event):
        self.mainLabel.configure(bg='SystemButtonFace', fg='black')
    def on_enter_btn1(self, event):
        self.btn1.configure(bg='grey', fg='white')

    def on_leave_btn1(self, event):
        self.btn1.configure(bg='SystemButtonFace', fg='black')
    def on_enter_btn2(self, event):
        self.btn2.configure(bg='grey', fg='white')

    def on_leave_btn2(self, event):
        self.btn2.configure(bg='SystemButtonFace', fg='black')
    def openUpdateWindow(self, event):
        rowid = self.adminTable.selection()[0]
        data = self.adminTable.item(rowid)
        selectedAdmin = data['values']

        self.root1 = Toplevel()

        self.root1.geometry('900x800')
        self.root1.configure(bg="black")

        self.mainLabel1 = Label(self.root1, text=" Update Admins ", font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel1.pack(pady=20)

        self.f = Frame(self.root1)
        self.f.pack(pady=10)

        font = ('calibri', 14)


        self.lb0 = Label(self.f, text='Admin ID', font="calibri 15", bg="black", fg="white")
        self.txt0 = Entry(self.f, font=font, width=30)
        self.lb0.grid(row=0, column=0, pady=10, padx=10)
        self.txt0.grid(row=0, column=1, pady=10, padx=10)
        self.txt0.insert(0, selectedAdmin[0])
        self.txt0.config(state='readonly')

        self.lb1 = Label(self.f, text='Enter Name', font="calibri 15", bg="black", fg="white")
        self.txt1 = Entry(self.f, font=font, width=30)
        self.lb1.grid(row=1, column=0, pady=10, padx=10)
        self.txt1.grid(row=1, column=1, pady=10, padx=10)
        self.txt1.insert(0, selectedAdmin[1])

        self.lb2 = Label(self.f, text='Enter Email', font="calibri 15", bg="black", fg="white")
        self.txt2 = Entry(self.f, font=font, width=30)
        self.lb2.grid(row=2, column=0, pady=10, padx=10)
        self.txt2.grid(row=2, column=1, pady=10, padx=10)
        self.txt2.insert(0, selectedAdmin[2])

        self.lb3 = Label(self.f, text='Enter Mobile', font="calibri 15", bg="black", fg="white")
        self.txt3 = Entry(self.f, font=font, width=30)
        self.lb3.grid(row=3, column=0, pady=10, padx=10)
        self.txt3.grid(row=3, column=1, pady=10, padx=10)
        self.txt3.insert(0, selectedAdmin[3])

        self.lb4 = Label(self.f, text='Select Role', font="calibri 15", bg="black", fg="white")
        self.txt4 = ttk.Combobox(self.f, font=font, width=28, state='readonly', values=['Super Admin', 'Admin'])
        self.lb4.grid(row=4, column=0, pady=10, padx=10)
        self.txt4.grid(row=4, column=1, pady=10, padx=10)
        self.txt4.set(selectedAdmin[4])

        self.btn = Button(self.root1, text='Submit', font="calibri 25 bold", fg="black", bg="white", activeforeground="black", borderwidth=2, relief=RAISED, command=self.updateAdmin)
        self.btn.pack(pady=20)

        self.btn.bind("<Enter>", self.on_enter_btn)
        self.btn.bind("<Leave>", self.on_leave_btn)
        self.mainLabel1.bind("<Enter>", self.on_enter_mainLabel1)
        self.mainLabel1.bind("<Leave>", self.on_leave_mainLabel1)

        self.root1.mainloop()

    def on_enter_btn(self, event):
        self.btn.configure(bg='grey', fg='white')

    def on_leave_btn(self, event):
        self.btn.configure(bg='SystemButtonFace', fg='black')

    def on_enter_mainLabel1(self, event):
        self.mainLabel1.configure(bg='grey', fg='white')

    def on_leave_mainLabel1(self, event):
        self.mainLabel1.configure(bg='SystemButtonFace', fg='black')

    def updateAdmin(self):
        id = self.txt0.get()
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        role = self.txt4.get()

        if len(name) == 0 or len(email) == 0 or len(mobile) == 0 or len(role) == 0:
            msg.showwarning('Warning', 'PLease Enter Correct Details', parent=self.root)

        else:
            if verifyemail(email) == "invalid" or verifymobile(mobile) == "invalid":
                msg.showwarning("Warning", "invalid email and mobile", parent=self.root)

            else:
                q = f"update add_admin set name='{name}', email='{email}', mobile='{mobile}',role='{role}' where id='{id}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo('Success', "Admin has been Updated", parent=self.root)
                self.getValues()
                self.root1.destroy()



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
        q = f"select id, name, email, mobile, role from add_admin where name like '%{text}%'"
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

# x = Main()