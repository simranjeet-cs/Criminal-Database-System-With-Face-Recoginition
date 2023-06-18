from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect
import admin_dashboard

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('900x800')
        self.root.config(background="black")

        self.mainLabel = Label(self.root, text=" Admin Login ", font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        font = ('calibri', 14)

        self.lb1 = Label(self.f, text='Enter Email', font="calibri 15", bg="black", fg="white")
        self.txt1 = Entry(self.f, font=font, width=30)
        self.lb1.grid(row=0, column=0, pady=10, padx=10)
        self.txt1.grid(row=0, column=1, pady=10, padx=10)

        self.lb2 = Label(self.f, text='Enter Password', font="calibri 15", bg="black", fg="white")
        self.txt2 = Entry(self.f, font=font, width=30, show='*')
        self.lb2.grid(row=1, column=0, pady=10, padx=10)
        self.txt2.grid(row=1, column=1, pady=10, padx=10)

        self.btn = Button(self.root, text='Submit', font="calibri 25 bold", fg="black", bg="white", activeforeground="black", borderwidth=2, relief=RAISED, command=self.verifyAdmin)
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


    def verifyAdmin(self):
        email = self.txt1.get()
        password = self.txt2.get()
        conn = connect()
        cr = conn.cursor()
        q = f"select * from add_admin where email='{email}' and password='{password}'"
        cr.execute(q)
        data = cr.fetchall()
        if len(data) == 0:
            msg.showwarning('Warning', 'Invalid Email/Password', parent=self.root)
            self.txt2.delete(0, 'end')
        else:
            msg.showinfo("Success", "Login Successful", parent=self.root)
            self.txt1.delete(0, 'end')
            self.txt2.delete(0, 'end')
            self.root.destroy()
            admin_dashboard.Main()


# x = Main()