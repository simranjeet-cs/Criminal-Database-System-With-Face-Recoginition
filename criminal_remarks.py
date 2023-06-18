from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import connect

class Main:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.configure(bg="black")

        self.mainLabel = Label(self.root, text=' View Remarks ', font=('calibri', 26, 'bold'), fg ="black", bg="white", borderwidth=2, relief=RAISED, activebackground="black", activeforeground="white")
        self.mainLabel.pack(pady=20)

        self.f = Frame(self.root)
        self.f.pack(pady=10)

        font = ('calibri', 14)

        self.remarksTable = ttk.Treeview(self.root, columns=('id', 'criminal_id', 'center_id', 'date', 'time', 'description'))
        self.remarksTable.pack(pady=10, padx=20, expand=True, fill='both')

        self.remarksTable.heading('id', text='ID')
        self.remarksTable.heading('criminal_id', text='Criminal_ID')
        self.remarksTable.heading('center_id', text='Center_ID')
        self.remarksTable.heading('date', text='Date')
        self.remarksTable.heading('time', text='Time')
        self.remarksTable.heading('description', text='Description')

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 14), rowheight=40 )
        style.configure('Treeview.Heading', font=('arial', 14))

        self.remarksTable['show'] = 'headings'
        self.getValues()

        self.delBtn = Button(self.root, text="Delete", font=('arial', 14), width=20, command=self.delRemarks)
        self.delBtn.pack(pady=20)

        self.delBtn.bind("<Enter>", self.on_enter_delBtn)
        self.delBtn.bind("<Leave>", self.on_leave_delBtn)
        self.mainLabel.bind("<Enter>", self.on_enter_mainLabel)
        self.mainLabel.bind("<Leave>", self.on_leave_mainLabel)
        self.root.mainloop()

    def on_enter_delBtn(self, event):
        self.delBtn.configure(bg='grey', fg='white')

    def on_leave_delBtn(self, event):
        self.delBtn.configure(bg='SystemButtonFace', fg='black')
    def on_enter_mainLabel(self, event):
        self.mainLabel.configure(bg='grey', fg='white')

    def on_leave_mainLabel(self, event):
        self.mainLabel.configure(bg='SystemButtonFace', fg='black')

    def delRemarks(self):
        rowid = self.remarksTable.selection()[0]
        data = self.remarksTable.item(rowid)
        selectedRemark = data['values']
        RemarkID = selectedRemark[0]
        q = f"delete from criminal_remarks where id='{RemarkID}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('Success', "Criminal Remark deleted Successfully", parent=self.root)
        self.getValues()


    def getValues(self):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select id, criminal_id, center_id, date, time, description from criminal_remarks"
        self.cr.execute(q)
        data = self.cr.fetchall()
        # print(data)
        for k in self.remarksTable.get_children():
            self.remarksTable.delete(k)
            # print(k)
        for i in data:
            self.remarksTable.insert('', index=0, values=i)

            self.remarksTable.tag_configure('criminal_id', background='grey', foreground='black')
            self.remarksTable.tag_configure('', background='lightgrey', foreground='black')


# x = Main()