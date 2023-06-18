from tkinter import *
import center_login
import admin_login
import add_center
from PIL import Image, ImageTk


class Main:
    def __init__(self):
        self.root = Tk()
        self.root.title("Main Login Page")
        self.root.state("zoomed")
        self.root.configure(bg="black")

        self.lb1=Label(self.root, text=" LOGIN  PAGE ", font="calibri 26 bold", fg="black", bg="white", borderwidth=3, relief=RAISED)
        self.lb1.pack(padx=10, pady=10)

        self.f = Frame(self.root)
        self.f.pack(pady=20)

        self.btn1 = Button(self.f, text="ADMIN  LOGIN", font="calibri 25 bold", command=self.admin, fg="black", bg="white", activeforeground="black")
        self.btn1.grid(row=0, column=0)
        self.btn1.configure(anchor=CENTER)

        self.btn2 = Button(self.f, text="CENTER  LOGIN", font="calibri 25 bold", fg="black", bg="white", activeforeground="black",command=self.center)
        self.btn2.grid(row=0, column=1)
        self.btn2.configure(anchor=CENTER)

        self.btn3 = Button(self.f, text="REGISTER CENTER", font="calibri 25 bold", fg="black", bg="white", activeforeground="black", command=self.register_center)
        self.btn3.grid(row=0, column=2)
        self.btn3.configure(anchor=CENTER)

        img = Image.open('criminal-history-check.jpg')
        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())
        print(width, height)
        img = img.resize((width, height))
        bg = ImageTk.PhotoImage(img)

        canvas = Canvas(self.root, width=self.root.winfo_width(), height=self.root.winfo_height())
        canvas.pack(fill='both', expand=True)

        canvas.create_image(0, 0, image=bg, anchor='nw')

        self.btn1.bind("<Enter>", self.on_enter_btn1)
        self.btn1.bind("<Leave>", self.on_leave_btn1)

        self.btn2.bind("<Enter>", self.on_enter_btn2)
        self.btn2.bind("<Leave>", self.on_leave_btn2)

        self.btn3.bind("<Enter>", self.on_enter_btn3)
        self.btn3.bind("<Leave>", self.on_leave_btn3)

        self.lb1.bind("<Enter>", self.on_enter_lb1)
        self.lb1.bind("<Leave>", self.on_leave_lb1)

        self.root.mainloop()

    def on_enter_btn1(self, event):
        self.btn1.configure(bg='grey', fg='white')

    def on_enter_btn2(self, event):
        self.btn2.configure(bg='grey', fg='white')

    def on_enter_btn3(self, event):
        self.btn3.configure(bg='grey', fg='white')

    def on_leave_btn1(self, event):
        self.btn1.configure(bg='SystemButtonFace', fg='black')

    def on_leave_btn2(self, event):
        self.btn2.configure(bg='SystemButtonFace', fg='black')

    def on_leave_btn3(self, event):
        self.btn3.configure(bg='SystemButtonFace', fg='black')

    def on_enter_lb1(self, event):

        self.lb1.configure(bg='grey', fg='white')

    def on_leave_lb1(self, event):

        self.lb1.configure(bg='SystemButtonFace', fg='black')

    def center(self):
        center_login.Main()

    def admin(self):
        admin_login.Main()

    def register_center(self):
        add_center.Main()


x = Main()