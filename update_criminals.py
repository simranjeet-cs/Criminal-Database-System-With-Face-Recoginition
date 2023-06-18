from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.configure(bg="black")

        self.mainLabel = Label(self.root, text=' View Criminals ', font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        font = ('calibri', 14)

        self.lb1 = Label(self.f, text="Search Name", font=('arial', 14))
        self.txt1 = Entry(self.f, font=('arial', 14), width=30)
        self.btn1 = Button(self.f, text="Search", font=('arial', 14), width=20, command=self.searchCriminal)
        self.btn2 = Button(self.f, text="Refresh", font=('arial', 14), width=20, command=self.refresh)
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
        self.criminalTable.bind("<Double-1>", self.openUpdateWindow)

        self.delBtn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.delCriminal)
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
        rowid = self.criminalTable.selection()[0]
        data = self.criminalTable.item(rowid)
        selectedCriminal = data['values']

        self.root1 = Toplevel()

        self.root1.geometry('900x800')
        self.root1.configure(bg="black")

        self.mainLabel1 = Label(self.root1, text=" Update Criminals ", font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel1.pack(pady=20)

        self.f = Frame(self.root1)
        self.f.pack(pady=10)

        font = ('calibri', 14)


        self.lb0 = Label(self.f, text='Criminal ID', font="calibri 15", bg="black", fg="white")
        self.txt0 = Entry(self.f, font=font, width=30)
        self.lb0.grid(row=0, column=0, pady=10, padx=10)
        self.txt0.grid(row=0, column=1, pady=10, padx=10)
        self.txt0.insert(0, selectedCriminal[0])
        self.txt0.config(state='readonly')

        self.lb1 = Label(self.f, text='Enter Name', font="calibri 15", bg="black", fg="white")
        self.txt1 = Entry(self.f, font=font, width=30)
        self.lb1.grid(row=1, column=0, pady=10, padx=10)
        self.txt1.grid(row=1, column=1, pady=10, padx=10)
        self.txt1.insert(0, selectedCriminal[1])

        self.lb2 = Label(self.f, text='Enter Father Name', font="calibri 15", bg="black", fg="white")
        self.txt2 = Entry(self.f, font=font, width=30)
        self.lb2.grid(row=2, column=0, pady=10, padx=10)
        self.txt2.grid(row=2, column=1, pady=10, padx=10)
        self.txt2.insert(0, selectedCriminal[2])

        self.lb3 = Label(self.f, text='Enter Mobile', font="calibri 15", bg="black", fg="white")
        self.txt3 = Entry(self.f, font=font, width=30)
        self.lb3.grid(row=3, column=0, pady=10, padx=10)
        self.txt3.grid(row=3, column=1, pady=10, padx=10)
        self.txt3.insert(0, selectedCriminal[3])

        self.lb4 = Label(self.f, text='Enter Email', font="calibri 15", bg="black", fg="white")
        self.txt4 = Entry(self.f, font=font, width=30)
        self.lb4.grid(row=4, column=0, pady=10, padx=10)
        self.txt4.grid(row=4, column=1, pady=10, padx=10)
        self.txt4.insert(0, selectedCriminal[4])

        self.lb5 = Label(self.f, text='Enter Address', font="calibri 15", bg="black", fg="white")
        self.txt5 = Entry(self.f, font=font, width=30)
        self.lb5.grid(row=5, column=0, pady=10, padx=10)
        self.txt5.grid(row=5, column=1, pady=10, padx=10)
        self.txt5.insert(0, selectedCriminal[5])

        self.lb6 = Label(self.f, text='Enter Image', font="calibri 15", bg="black", fg="white")
        self.txt6 = Entry(self.f, font=font, width=30)
        self.lb6.grid(row=6, column=0, pady=10, padx=10)
        self.txt6.grid(row=6, column=1, pady=10, padx=10)
        self.txt6.insert(0, selectedCriminal[6])
        self.txt6.config(state='readonly')

        self.btn = Button(self.root1, text='Submit', font="calibri 25 bold", fg="black", bg="white", activeforeground="black", borderwidth=2, relief=RAISED, command=self.updateCriminal)
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
    def updateCriminal(self):
        id = self.txt0.get()
        name = self.txt1.get()
        father_name = self.txt2.get()
        mobile = self.txt3.get()
        email = self.txt4.get()
        address = self.txt5.get()
        image = self.txt6.get()
        q = f"update criminals set name='{name}', father_name='{father_name}', mobile='{mobile}', email='{email}', address='{address}', image='{image}'where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Criminal has been Updated", parent=self.root)
        self.getValues()
        self.root1.destroy()


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


# x = Main()