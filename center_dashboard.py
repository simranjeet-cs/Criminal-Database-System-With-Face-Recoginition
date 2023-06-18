from tkinter import *
import tkinter.messagebox as msg
import change_center_password
import criminal_temp
import criminal_remarks
import criminals
import view_criminals
import update_criminals
import add_report
import update_report
from PIL import Image,ImageTk

class Main:

    def __init__(self, center_id):
        self.root = Toplevel()
        self.root.state('zoomed')
        self.root.configure(bg="black")

        self.rootMenu = Menu(self.root, font=('arial', 16))
        self.root.configure(menu=self.rootMenu)
        self.rootMenu.configure(bg="black")

        self.profileSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 16))
        self.rootMenu.add_cascade(label='Profile', menu=self.profileSubMenu)
        self.profileSubMenu.add_command(label='Change Password', command=lambda: change_center_password.Main())
        self.profileSubMenu.add_command(label='Logout', command=lambda: self.root.destroy())

        self.centerSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 16))
        self.rootMenu.add_cascade(label='Manage Criminals', menu=self.centerSubMenu)
        self.centerSubMenu.add_command(label='Add Criminals', command=self.openAddCriminal)
        self.centerSubMenu.add_command(label='Print Criminal Data', command=lambda: view_criminals.Main())
        self.centerSubMenu.add_command(label='View Criminals', command=lambda: update_criminals.Main())

        self.centerSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 16))
        self.rootMenu.add_cascade(label='Manage Reports', menu=self.centerSubMenu)
        self.centerSubMenu.add_command(label='Add Reports', command=lambda: add_report.Main())
        self.centerSubMenu.add_command(label='View Reports', command=lambda: update_report.Main())

        self.centerSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 16))
        self.rootMenu.add_cascade(label='Manage Criminal Remarks', menu=self.centerSubMenu)
        self.centerSubMenu.add_command(label='Add Remarks', command=lambda: criminal_temp.Main(center_id))
        self.centerSubMenu.add_command(label='View Remarks', command=lambda: criminal_remarks.Main())


        self.mainLabel = Label(self.root, text=' Welcome to Center Dashboard ', font=('arial', 30, 'bold'))
        self.mainLabel.pack(pady=30)

        img = Image.open('criminal-history-check.jpg')
        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())
        print(width, height)
        img = img.resize((width, height))
        bg = ImageTk.PhotoImage(img)

        canvas = Canvas(self.root, width=self.root.winfo_width(), height=self.root.winfo_height())
        canvas.pack(fill='both', expand=True)

        canvas.create_image(0, 0, image=bg, anchor='nw')

        self.root.mainloop()

    def openAddCriminal(self):
        criminals.Main()


# x = Main()
