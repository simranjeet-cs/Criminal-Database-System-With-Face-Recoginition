from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.configure(bg="black")

        self.mainLabel = Label(self.root, text=' View Category ', font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        font = ('calibri', 14)

        self.lb1 = Label(self.f, text="Search Name", font=('arial', 14))
        self.txt1 = Entry(self.f, font=('arial', 14), width=30)
        self.btn1 = Button(self.f, text="Search", font=('arial', 14), width=20, command=self.searchCategory)
        self.btn2 = Button(self.f, text="Refresh", font=('arial', 14), width=20, command=self.refresh)
        self.lb1.grid(row=0, column=0, padx=10)
        self.txt1.grid(row=0, column=1, padx=10)
        self.btn1.grid(row=0, column=2, padx=10)
        self.btn2.grid(row=0, column=3, padx=10)

        self.categoryTable = ttk.Treeview(self.root, columns=( 'name', 'description'))
        self.categoryTable.pack(pady=10, padx=20,expand=True, fill='both')

        self.categoryTable.heading('name', text='Name')
        self.categoryTable.heading('description', text='Description')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40)
        style.configure('Treeview.Heading', font=('arial', 14))

        self.categoryTable['show'] = 'headings'
        self.getValues()
        self.categoryTable.bind("<Double-1>", self.openUpdateWindow)

        self.delBtn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.delCategory)
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
        name = self.categoryTable.selection()[0]
        data = self.categoryTable.item(name)
        selectedCategory = data['values']

        self.root1 = Toplevel()

        self.root1.geometry('900x800')
        self.root1.configure(bg="black")

        self.mainLabel1 = Label(self.root1, text=" Update Category ", font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel1.pack(pady=20)

        self.f = Frame(self.root1)
        self.f.pack(pady=10)

        font = ('calibri', 14)


        self.lb0 = Label(self.f, text='Name', font="calibri 15", bg="black", fg="white")
        self.txt0 = Entry(self.f, font=font, width=30)
        self.lb0.grid(row=0, column=0, pady=10, padx=10)
        self.txt0.grid(row=0, column=1, pady=10, padx=10)
        self.txt0.insert(0, selectedCategory[0])
        self.txt0.config(state='readonly')

        self.lb1 = Label(self.f, text='Enter Description', font="calibri 15", bg="black", fg="white")
        self.txt1 = Entry(self.f, font=font, width=30)
        self.lb1.grid(row=1, column=0, pady=10, padx=10)
        self.txt1.grid(row=1, column=1, pady=10, padx=10)
        self.txt1.insert(0, selectedCategory[1])



        self.btn = Button(self.root1, text='Submit', font="calibri 25 bold", fg="black", bg="white", activeforeground="black", borderwidth=2, relief=RAISED, command=self.updateCategory)
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
    def updateCategory(self):
        name = self.txt0.get()
        description = self.txt1.get()
        q = f"update add_category set name='{name}', description='{description}' where name='{name}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Categoory has been Updates", parent=self.root)
        self.getValues()
        self.root1.destroy()


    def delCategory(self):
        Name = self.categoryTable.selection()[0]
        data = self.categoryTable.item(Name)
        selectedCategory = data['values']
        Name = selectedCategory[0]
        q = f"delete from add_category where name = '{Name}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Category deleted Successfully", parent=self.root)
        self.getValues()




    def refresh(self):
        self.txt1.delete(0,'end')
        self.getValues()

    def searchCategory(self):
        text = self.txt1.get()
        q = f"select name, description from add_category where name like '%{text}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.categoryTable.get_children():
            self.categoryTable.delete(k)
            # print(k)
        for i in data:
            self.categoryTable.insert('', index=0, values=i)



    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select name, description from add_category"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.categoryTable.get_children():
            self.categoryTable.delete(k)
            # print(k)
        for i in data:
            self.categoryTable.insert('', index=0, values=i)

# x = Main()