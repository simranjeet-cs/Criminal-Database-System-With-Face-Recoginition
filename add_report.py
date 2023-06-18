from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import connect
from tkinter.filedialog import askopenfilename
import cv2
import random


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('900x800')
        self.root.config(background="black")

        self.mainLabel = Label(self.root, text=" Add Report ", font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        font = ('calibri', 14)

        self.lb1 = Label(self.f, text='Enter Tittle', font= "calibri 15", bg="black", fg="white")
        self.txt1 = Entry(self.f, font=font, width=30)
        self.lb1.grid(row=0, column=0, pady=10, padx=10)
        self.txt1.grid(row=0, column=1, pady=10, padx=10)

        self.lb2 = Label(self.f, text='Enter Description', font= "calibri 15", bg="black", fg="white")
        self.txt2 = Entry(self.f, font=font, width=30)
        self.lb2.grid(row=1, column=0, pady=10, padx=10)
        self.txt2.grid(row=1, column=1, pady=10, padx=10)

        self.lb3 = Label(self.f, text='Enter Date (YYYY-MM-DD)', font= "calibri 15", bg="black", fg="white")
        self.txt3 = Entry(self.f, font=font, width=30)
        self.lb3.grid(row=2, column=0, pady=10, padx=10)
        self.txt3.grid(row=2, column=1, pady=10, padx=10)

        self.lb4 = Label(self.f, text='Enter Culprit Name', font= "calibri 15", bg="black", fg="white")
        self.txt4 = Entry(self.f, font=font, width=30)
        self.lb4.grid(row=3, column=0, pady=10, padx=10)
        self.txt4.grid(row=3, column=1, pady=10, padx=10)

        self.lb5 = Label(self.f, text='Enter Mobile', font= "calibri 15", bg="black", fg="white")
        self.txt5 = Entry(self.f, font=font, width=30)
        self.lb5.grid(row=4, column=0, pady=10, padx=10)
        self.txt5.grid(row=4, column=1, pady=10, padx=10)

        self.lb6 = Label(self.f, text='Enter Email', font= "calibri 15", bg="black", fg="white")
        self.txt6 = Entry(self.f, font=font, width=30)
        self.lb6.grid(row=5, column=0, pady=10, padx=10)
        self.txt6.grid(row=5, column=1, pady=10, padx=10)

        self.lb7 = Label(self.f, text='Enter Address', font= "calibri 15", bg="black", fg="white")
        self.txt7 = Entry(self.f, font=font, width=30)
        self.lb7.grid(row=6, column=0, pady=10, padx=10)
        self.txt7.grid(row=6, column=1, pady=10, padx=10)

        self.lb8 = Label(self.f, text='Enter Image', font= "calibri 15", bg="black", fg="white")
        self.txt8 = Entry(self.f, font=font, width=30)
        self.lb8.grid(row=7, column=0, pady=10, padx=10)
        self.txt8.grid(row=7, column=1, pady=10, padx=10)

        self.btn11 = Button(self.f, text='Select', font="calibri 25 bold", fg="black", bg="white", activeforeground="black", activebackground="white", borderwidth=2, relief=RAISED, command=self.selectImage)
        self.btn11.grid(row=7, column=2, pady=10, padx=10)

        self.btn = Button(self.root, text='Submit', font="calibri 25 bold", fg="black", bg="white", activeforeground="black", borderwidth=2, relief=RAISED, command=self.submitForm)
        self.btn.pack(pady=20)

        self.btn.bind("<Enter>", self.on_enter_btn)
        self.btn.bind("<Leave>", self.on_leave_btn)

        self.btn11.bind("<Enter>", self.on_enter_btn11)
        self.btn11.bind("<Leave>", self.on_leave_btn11)
        self.mainLabel.bind("<Enter>", self.on_enter_mainLabel)
        self.mainLabel.bind("<Leave>", self.on_leave_mainLabel)

        self.root.mainloop()

    def on_enter_btn(self, event):
        self.btn.configure(bg='grey', fg='white')

    def on_enter_btn11(self, event):
        self.btn11.configure(bg='grey', fg='white')

    def on_leave_btn(self, event):
        self.btn.configure(bg='SystemButtonFace', fg='black')

    def on_leave_btn11(self, event):
        self.btn11.configure(bg='SystemButtonFace', fg='black')
    def on_enter_mainLabel(self, event):
        self.mainLabel.configure(bg='grey', fg='white')

    def on_leave_mainLabel(self, event):
        self.mainLabel.configure(bg='SystemButtonFace', fg='black')

    def selectImage(self):
        culprit_name = self.txt1.get()
        path = askopenfilename()
        print(path)
        img = cv2.imread(path)
        cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        face = cascade.detectMultiScale(img, 1.1, 4)
        if len(face) == 0:
            msg.showwarning("Warning", 'Image is not Valid', parent=self.root)
        else:
            msg.showinfo("Success", 'Image is Valid', parent=self.root)
            img_name = f"{culprit_name}_{random.randint(10000, 99999)}.jpeg"
            cv2.imwrite(f"reports/{img_name}", img)
            self.txt8.insert(0, img_name)

    def submitForm(self):
        tittle = self.txt1.get()
        description = self.txt2.get()
        date = self.txt3.get()
        culprit_name = self.txt4.get()
        mobile = self.txt5.get()
        email = self.txt6.get()
        address = self.txt7.get()
        image = self.txt8.get()

        if len(tittle) == 0 or len(description) == 0 or len(date) == 0 or len(culprit_name) == 0 or len(mobile) == 0 or len(email) == 0 or len(address) == 0 or mobile.isalpha():
            msg.showwarning('Warning', 'PLease Enter Correct Details', parent=self.root)
        else:
            conn = connect()
            cr = conn.cursor()
            q = f"insert into reports values (null, '{tittle}', '{description}', '{date}', '{culprit_name}', '{mobile}', '{email}', '{address}', '{image}')"

            cr.execute(q)
            conn.commit()
            msg.showinfo('Success',"Report has been Added..", parent=self.root)
            self.txt1.delete(0, 'end')
            self.txt2.delete(0, 'end')
            self.txt3.delete(0, 'end')
            self.txt4.delete(0, 'end')
            self.txt5.delete(0, 'end')
            self.txt6.delete(0, 'end')
            self.txt7.delete(0, 'end')
            self.txt8.delete(0, 'end')

# x = Main()