from tkinter import *
import tkinter.messagebox as msg
import change_admin_password
import change_center_password
import add_admin
import view_admin
import delete_admin
import update_admin
import add_category
import view_category
import delete_category
import update_category
import add_area
import view_area
import delete_area
import update_area
import add_location
import view_location
import delete_location
import update_location
import add_report
import view_report
import delete_report
import update_report
import criminal_temp
import criminal_remarks
import criminals
import view_criminals
import delete_criminal
import update_criminals
import add_center
import view_center
import delete_center
import update_center
import center_login
from PIL import Image,ImageTk


class Main:

    def __init__(self):
        self.root = Toplevel()
        self.root.state('zoomed')
        self.root.configure(bg="black")

        self.rootMenu = Menu(self.root, font=('arial', 16))
        self.root.configure(menu=self.rootMenu)
        self.rootMenu.configure(bg="black")

        self.profileSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 14))
        self.rootMenu.add_cascade(label='Profile', menu=self.profileSubMenu)
        self.passSubMenu = Menu(self.profileSubMenu, tearoff=0)
        self.profileSubMenu.add_cascade(label='Change Password', menu=self.passSubMenu)
        self.passSubMenu.add_command(label='Change Admin Password', command=lambda: change_admin_password.Main())
        self.passSubMenu.add_command(label='Change Center Password', command=lambda: change_center_password.Main())
        self.profileSubMenu.add_command(label='Logout', command=lambda: self.root.destroy())

        self.adminSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 14))
        self.rootMenu.add_cascade(label='Manage Admins', menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label='Add Admin', command=self.openAddAdmin)
        self.adminSubMenu.add_command(label='View Admin', command=lambda: update_admin.Main())

        self.adminSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 14))
        self.rootMenu.add_cascade(label='Manage Center', menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label='Add Center', command=lambda: add_center.Main())
        self.adminSubMenu.add_command(label='View Center', command=lambda: update_center.Main())
        self.adminSubMenu.add_command(label='Center Login', command=lambda: center_login.Main())

        self.adminSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 14))
        self.rootMenu.add_cascade(label='Manage Category', menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label='Add Category', command=lambda: add_category.Main())
        self.adminSubMenu.add_command(label='View Category', command=lambda: update_category.Main())

        self.adminSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 14))
        self.rootMenu.add_cascade(label='Manage Areas', menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label='Add Area', command=lambda: add_area.Main())
        self.adminSubMenu.add_command(label='View Area', command=lambda: update_area.Main())

        self.adminSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 14))
        self.rootMenu.add_cascade(label='Manage Locations', menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label='Add Location', command=lambda: add_location.Main())
        self.adminSubMenu.add_command(label='View Location', command=lambda: update_location.Main())

        self.adminSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 14))
        self.rootMenu.add_cascade(label='Manage Criminals', menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label='Add Criminals', command=lambda: criminals.Main())
        self.adminSubMenu.add_command(label='View Criminals', command=lambda: update_criminals.Main())

        self.adminSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 14))
        self.rootMenu.add_cascade(label='Manage Reports', menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label='Add Report', command=lambda: add_report.Main())
        self.adminSubMenu.add_command(label='View Report', command=lambda: update_report.Main())

        self.adminSubMenu = Menu(self.rootMenu, tearoff=0, font=('arial', 14))
        self.rootMenu.add_cascade(label='Manage Criminal Remarks', menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label='View Remarks', command=lambda: criminal_remarks.Main())

        self.root.mainLabel = Label(self.root, text=' Welcome to Admin Dashboard ', font=('arial', 30, 'bold'))
        self.root.mainLabel.pack(pady=30)

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

    def openAddAdmin(self):
        add_admin.Main()

# x = Main()


