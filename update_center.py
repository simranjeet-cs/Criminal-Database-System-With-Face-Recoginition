from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect, verifyemail, verifymobile

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.configure(bg="black")

        self.mainLabel = Label(self.root, text=' View Center ', font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        font = ('calibri', 14)

        self.lb1 = Label(self.f, text="Search Name", font=('arial', 14))
        self.txt1 = Entry(self.f, font=('arial', 14), width=30)
        self.btn1 = Button(self.f, text="Search", font=('arial', 14), width=20, command=self.searchCenter)
        self.btn2 = Button(self.f, text="Refresh", font=('arial', 14), width=20, command=self.refresh)
        self.lb1.grid(row=0, column=0, padx=10)
        self.txt1.grid(row=0, column=1, padx=10)
        self.btn1.grid(row=0, column=2, padx=10)
        self.btn2.grid(row=0, column=3, padx=10)

        self.centerTable = ttk.Treeview(self.root, columns=('id', 'name', 'email', 'mobile', 'area', 'location'))
        self.centerTable.pack(pady=10, padx=20, expand=True, fill='both')

        self.centerTable.heading('id', text='ID')
        self.centerTable.heading('name', text='Name')
        self.centerTable.heading('email', text='Email')
        self.centerTable.heading('mobile', text='Mobile')
        self.centerTable.heading('area', text='AREA')
        self.centerTable.heading('location', text='LOCATION')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14))

        self.centerTable['show'] = 'headings'
        self.getValues()
        self.centerTable.bind("<Double-1>", self.openUpdateWindow)

        self.delBtn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.delCenter)
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
        rowid = self.centerTable.selection()[0]
        data = self.centerTable.item(rowid)
        selectedCenter = data['values']

        self.root1 = Toplevel()

        self.root1.geometry('900x800')
        self.root1.configure(bg="black")

        self.mainLabel1 = Label(self.root1, text=" Update Center ", font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel1.pack(pady=20)

        self.f = Frame(self.root1)
        self.f.pack(pady=10)

        font = ('calibri', 14)

        self.lb0 = Label(self.f, text='Center ID', font="calibri 15", bg="black", fg="white")
        self.txt0 = Entry(self.f, font=font, width=30)
        self.lb0.grid(row=0, column=0, pady=10, padx=10)
        self.txt0.grid(row=0, column=1, pady=10, padx=10)
        self.txt0.insert(0, selectedCenter[0])
        self.txt0.config(state='readonly')

        self.lb1 = Label(self.f, text='Enter Name', font="calibri 15", bg="black", fg="white")
        self.txt1 = Entry(self.f, font=font, width=30)
        self.lb1.grid(row=1, column=0, pady=10, padx=10)
        self.txt1.grid(row=1, column=1, pady=10, padx=10)
        self.txt1.insert(0, selectedCenter[1])

        self.lb2 = Label(self.f, text='Enter Email', font="calibri 15", bg="black", fg="white")
        self.txt2 = Entry(self.f, font=font, width=30)
        self.lb2.grid(row=2, column=0, pady=10, padx=10)
        self.txt2.grid(row=2, column=1, pady=10, padx=10)
        self.txt2.insert(0, selectedCenter[2])

        self.lb3 = Label(self.f, text='Enter Mobile', font="calibri 15", bg="black", fg="white")
        self.txt3 = Entry(self.f, font=font, width=30)
        self.lb3.grid(row=3, column=0, pady=10, padx=10)
        self.txt3.grid(row=3, column=1, pady=10, padx=10)
        self.txt3.insert(0, selectedCenter[3])

        self.lb4 = Label(self.f, text='Enter Area', font="calibri 15", bg="black", fg="white")
        self.txt4 = ttk.Combobox(self.f, font=font, width=30, state = 'readonly' , values=self.get_values())
        self.lb4.grid(row=4, column=0, pady=10, padx=10)
        self.txt4.grid(row=4, column=1, pady=10, padx=10)
        self.txt4.set(selectedCenter[4])

        self.lb5 = Label(self.f, text="Select Location", font="calibri 15", bg="black", fg="white")
        self.txt5 = ttk.Combobox(self.f, font=font, width=30, state = 'readonly', values=self.get_values1())
        self.lb5.grid(row=5, column=0, pady=10, padx=10)
        self.txt5.grid(row=5, column=1, pady=10, padx=10)
        self.status = 0
        self.txt5.set(selectedCenter[5])

        self.btn = Button(self.root1, text='Submit', font="calibri 25 bold", fg="black", bg="white", activeforeground="black", borderwidth=2, relief=RAISED, command=self.updateCenter)
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

    def get_values(self):
        conn = connect()
        cr = conn.cursor()
        q = f"select name from add_area"
        cr.execute(q)
        result = cr.fetchall()
        lst = []
        for i in result:
            lst.append(i[0])
        return lst

    def get_values1(self):
        conn = connect()
        cr = conn.cursor()
        q = f"select name from surveilance_location"
        cr.execute(q)
        self.result = cr.fetchall()
        lst = []
        for i in self.result:
            lst.append(i[0])
        return lst

    def updateCenter(self):
        id = self.txt0.get()
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        area = self.txt4.get()
        location = self.txt5.get()

        if len(name) == 0 or len(email) == 0 or len(mobile) == 0 or len(area) == 0 or len(location) == 0:
            msg.showwarning('Warning', 'PLease Enter Correct Details', parent=self.root)
        else:
            if verifyemail(email) == "invalid" or verifymobile(mobile) == "invalid":
                msg.showwarning("Warning", "invalid email and mobile", parent=self.root)
            else:
                q = f"UPDATE center set name='{name}', email='{email}', mobile='{mobile}', area='{area}', location='{location}' WHERE id='{id}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo('Success', "Center has been Updated", parent=self.root)
                self.getValues()
                self.root1.destroy()


    def delCenter(self):
        rowid = self.centerTable.selection()[0]
        data = self.centerTable.item(rowid)
        selectedCenter = data['values']
        centerID = selectedCenter[0]
        q = f"delete from center WHERE id='{centerID}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Center deleted Successfully", parent=self.root)
        self.getValues()

    def refresh(self):
        self.txt1.delete(0,'end')
        self.getValues()

    def searchCenter(self):
        text = self.txt1.get()
        q = f"select id, name, email, mobile, area, location from center where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.centerTable.get_children():
            self.centerTable.delete(k)
            # print(k)
        for i in data:
            self.centerTable.insert('', index=0, values=i)


    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select id, name, email, mobile, area, location from center"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.centerTable.get_children():
            self.centerTable.delete(k)
            # print(k)
        for i in data:
            self.centerTable.insert('', index=0, values=i)

    def get_values(self):
        conn = connect()
        cr = conn.cursor()
        q = f"select name from add_area"
        cr.execute(q)
        result = cr.fetchall()
        lst = []
        for i in result:
            lst.append(i[0])
        return lst

    def get_values1(self):
        conn = connect()
        cr = conn.cursor()
        q = f"select name from surveilance_location"
        cr.execute(q)
        self.result = cr.fetchall()
        lst = []
        for i in self.result:
            lst.append(i[0])
        return lst


#  x = Main()