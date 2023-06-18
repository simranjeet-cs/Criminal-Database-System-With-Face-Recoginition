from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect, verifyemail, verifymobile



class Main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('900x800')
        self.root.config(background="black")

        self.mainLabel = Label(self.root, text=" Add Center ", font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        font = ('calibri', 14)

        self.lb1 = Label(self.f, text='Enter Name', font="calibri 15", bg="black", fg="white")
        self.txt1 = Entry(self.f, font=font, width=30)
        self.lb1.grid(row=0, column=0, pady=10, padx=10)
        self.txt1.grid(row=0, column=1, pady=10, padx=10)

        self.lb2 = Label(self.f, text='Enter Email', font="calibri 15", bg="black", fg="white")
        self.txt2 = Entry(self.f, font=font, width=30)
        self.lb2.grid(row=1, column=0, pady=10, padx=10)
        self.txt2.grid(row=1, column=1, pady=10, padx=10)

        self.lb3 = Label(self.f, text='Enter Mobile', font="calibri 15", bg="black", fg="white")
        self.txt3 = Entry(self.f, font=font, width=30)
        self.lb3.grid(row=2, column=0, pady=10, padx=10)
        self.txt3.grid(row=2, column=1, pady=10, padx=10)

        self.lb4 = Label(self.f, text='Enter Password', font="calibri 15", bg="black", fg="white")
        self.txt4 = Entry(self.f, font=font, width=30, show='*')
        self.lb4.grid(row=3, column=0, pady=10, padx=10)
        self.txt4.grid(row=3, column=1, pady=10, padx=10)

        self.lb5 = Label(self.f, text="Select Area", font="calibri 15", bg="black", fg="white")
        self.txt5 = ttk.Combobox(self.f, font=font, width=30, values=self.get_values())
        self.lb5.grid(row=5, column=0, pady=10, padx=10)
        self.txt5.grid(row=5, column=1, pady=10, padx=10)
        self.status = 0

        self.lb6 = Label(self.f, text="Select Location", font="calibri 15", bg="black", fg="white")
        self.txt6 = ttk.Combobox(self.f, font=font, width=30, values=self.get_values1())
        self.lb6.grid(row=6, column=0, pady=10, padx=10)
        self.txt6.grid(row=6, column=1, pady=10, padx=10)
        self.status = 0

        self.btn = Button(self.root, text='Submit', font="calibri 25 bold", fg="black", bg="white", activeforeground="black", borderwidth=2, relief=RAISED, command=self.submitForm)
        self.btn.pack(pady=20)

        self.btn.bind("<Enter>", self.on_enter)
        self.btn.bind("<Leave>", self.on_leave)
        self.mainLabel.bind("<Enter>", self.on_enter_mainLabel)
        self.mainLabel.bind("<Leave>", self.on_leave_mainLabel)

        self.root.mainloop()

    def on_enter(self, event):
        self.btn.configure(bg='grey', fg='white')

    def on_leave(self, event):
        self.btn.configure(bg='SystemButtonFace', fg='black')

    def on_enter_mainLabel(self, event):
        self.mainLabel.configure(bg='grey', fg='white')

    def on_leave_mainLabel(self, event):
        self.mainLabel.configure(bg='SystemButtonFace', fg='black')

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

    def submitForm(self):
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        password = self.txt4.get()
        area = self.txt5.get()
        location = self.txt6.get()

        if len(name) == 0 or len(email) == 0 or len(mobile) == 0 or len(password) == 0 :
            msg.showwarning('Warning', 'PLease Enter Correct Details', parent=self.root)
        else:
            if verifyemail(email) == "invalid" or verifymobile(mobile) == "invalid":
                    msg.showwarning("Warning", "invalid email and mobile", parent=self.root)
            else:
                conn = connect()
                cr = conn.cursor()
                q = f"insert into center values (null, '{name}', '{email}', '{mobile}', '{password}', '{area}', '{location}')"

                cr.execute(q)
                conn.commit()
                msg.showinfo('Success', "Center has been Added..", parent=self.root)
                self.txt1.delete(0, 'end')
                self.txt2.delete(0, 'end')
                self.txt3.delete(0, 'end')
                self.txt4.delete(0, 'end')
                self.txt5.delete(0, 'end')
                self.txt6.delete(0, 'end')

# x = Main()