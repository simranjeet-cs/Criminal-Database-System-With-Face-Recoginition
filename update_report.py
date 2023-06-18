from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.configure(bg="black")

        self.mainLabel = Label(self.root, text=' View Reports ', font=('arial', 28, 'bold'))
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        self.lb1 = Label(self.f, text="Search Culprit Name", font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.txt1 = Entry(self.f, font=('arial', 14), width=30)
        self.btn1 = Button(self.f, text="Search", font=('arial', 14), width=20, command=self.searchReport)
        self.btn2 = Button(self.f, text="Refresh", font=('arial', 14), width=20, command=self.refresh)
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
        self.reportTable.bind("<Double-1>", self.openUpdateWindow)

        self.delBtn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.delReport)
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
        rowid = self.reportTable.selection()[0]
        data = self.reportTable.item(rowid)
        selectedReport = data['values']

        self.root1 = Toplevel()

        self.root1.geometry('900x800')
        self.root1.configure(bg="black")

        self.mainLabel1 = Label(self.root1, text=" Update Reports ", font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel1.pack(pady=20)

        self.f = Frame(self.root1)
        self.f.pack(pady=10)

        font = ('calibri', 14)


        self.lb0 = Label(self.f, text='Report ID', font="calibri 15", bg="black", fg="white")
        self.txt0 = Entry(self.f, font=font, width=30)
        self.lb0.grid(row=0, column=0, pady=10, padx=10)
        self.txt0.grid(row=0, column=1, pady=10, padx=10)
        self.txt0.insert(0, selectedReport[0])
        self.txt0.config(state='readonly')

        self.lb1 = Label(self.f, text='Enter Tittle', font="calibri 15", bg="black", fg="white")
        self.txt1 = Entry(self.f, font=font, width=30)
        self.lb1.grid(row=1, column=0, pady=10, padx=10)
        self.txt1.grid(row=1, column=1, pady=10, padx=10)
        self.txt1.insert(0, selectedReport[1])

        self.lb2 = Label(self.f, text='Enter Description', font="calibri 15", bg="black", fg="white")
        self.txt2 = Entry(self.f, font=font, width=30)
        self.lb2.grid(row=2, column=0, pady=10, padx=10)
        self.txt2.grid(row=2, column=1, pady=10, padx=10)
        self.txt2.insert(0, selectedReport[2])

        self.lb3 = Label(self.f, text='Enter Date', font="calibri 15", bg="black", fg="white")
        self.txt3 = Entry(self.f, font=font, width=30)
        self.lb3.grid(row=3, column=0, pady=10, padx=10)
        self.txt3.grid(row=3, column=1, pady=10, padx=10)
        self.txt3.insert(0, selectedReport[3])

        self.lb4 = Label(self.f, text='Enter Culprit Name', font="calibri 15", bg="black", fg="white")
        self.txt4 = Entry(self.f, font=font, width=30)
        self.lb4.grid(row=4, column=0, pady=10, padx=10)
        self.txt4.grid(row=4, column=1, pady=10, padx=10)
        self.txt4.insert(0, selectedReport[4])

        self.lb5 = Label(self.f, text='Enter Mobile', font="calibri 15", bg="black", fg="white")
        self.txt5 = Entry(self.f, font=font, width=30)
        self.lb5.grid(row=5, column=0, pady=10, padx=10)
        self.txt5.grid(row=5, column=1, pady=10, padx=10)
        self.txt5.insert(0, selectedReport[5])

        self.lb6 = Label(self.f, text='Enter Email', font="calibri 15", bg="black", fg="white")
        self.txt6 = Entry(self.f, font=font, width=30)
        self.lb6.grid(row=6, column=0, pady=10, padx=10)
        self.txt6.grid(row=6, column=1, pady=10, padx=10)
        self.txt6.insert(0, selectedReport[6])

        self.lb7 = Label(self.f, text='Enter Address', font="calibri 15", bg="black", fg="white")
        self.txt7 = Entry(self.f, font=font, width=30)
        self.lb7.grid(row=7, column=0, pady=10, padx=10)
        self.txt7.grid(row=7, column=1, pady=10, padx=10)
        self.txt7.insert(0, selectedReport[7])

        self.lb8 = Label(self.f, text='Enter image', font="calibri 15", bg="black", fg="white")
        self.txt8 = Entry(self.f, font=font, width=30)
        self.lb8.grid(row=8, column=0, pady=10, padx=10)
        self.txt8.grid(row=8, column=1, pady=10, padx=10)
        self.txt8.insert(0, selectedReport[8])
        self.txt8.config(state='readonly')

        self.btn = Button(self.root1, text='Submit', font=font, command=self.updateReport)
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


    def updateReport(self):
        id = self.txt0.get()
        tittle = self.txt1.get()
        description = self.txt2.get()
        date = self.txt3.get()
        culprit_name = self.txt4.get()
        mobile = self.txt5.get()
        email = self.txt6.get()
        address = self.txt7.get()
        image = self.txt8.get()
        q = f"update reports set tittle='{tittle}', description='{description}', date='{date}', culprit_name='{culprit_name}', mobile='{mobile}', email='{email}', address='{address}', image='{image}'where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Report has been Updated", parent=self.root)
        self.getValues()
        self.root1.destroy()


    def delReport(self):
        rowid = self.reportTable.selection()[0]
        data = self.reportTable.item(rowid)
        selectedReport = data['values']
        reportID = selectedReport[0]
        q = f"delete from reports where id='{reportID}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Report deleted Successfully", parent=self.root)
        self.getValues()




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
        q = f"select id, tittle, description, date, culprit_name, mobile, email, address,image from reports"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.reportTable.get_children():
            self.reportTable.delete(k)
            # print(k)
        for i in data:
            self.reportTable.insert('', index=0, values=i)


# x = Main()