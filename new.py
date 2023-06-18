import datetime
from tkinter import *
import customtkinter
from PIL import Image, ImageTk
import cv2
from deepface import DeepFace
import os
import tkinter.messagebox as msg
from connection import connect
import maildemo

class Main:


    def __init__(self, center_id):
        customtkinter.set_appearance_mode('dark')
        windowColor = '#000000'
        frameColor = '#000000'
        self.root = customtkinter.CTk()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry(f"{sw}x{sh}+0+0")
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.sideFrame1 = customtkinter.CTkFrame(self.root, height=sh - 100, width=int(sw / 3))
        self.sideFrame1.pack_propagate(0)
        self.sideFrame2 = customtkinter.CTkFrame(self.root, height=sh - 100, width=int(sw / 3 * 2))
        self.sideFrame2.pack_propagate(0)
        self.sideFrame1.grid(row=0, column=0, padx=10, pady=20)
        self.sideFrame2.grid(row=0, column=1, padx=10, pady=20)

        self.mainLabel2 = customtkinter.CTkButton(self.sideFrame1, text=' Criminal Database System ', font=('arial', 26), bg=frameColor, fg='white')
        self.mainLabel2.pack(pady=60)

        self.formFrame = customtkinter.CTkFrame(self.sideFrame1, bg=frameColor)
        self.formFrame.pack(pady=10, expand=True)
        self.mainLabel1 = customtkinter.CTkButton(self.formFrame, text='Get Details', font=('arial', 20), width=200, bg=frameColor, fg='white')
        self.mainLabel1.pack(pady=10)

        self.txt0 = customtkinter.CTkEntry(self.formFrame, placeholder_text='Center ID :', width=400, bg=windowColor, fg='white')
        self.txt0.insert(0, center_id)
        self.txt0.configure(state='readonly')
        self.txt0.pack(pady=10)

        self.txt1 = customtkinter.CTkEntry(self.formFrame, placeholder_text='Criminal ID :', width=400, bg=windowColor, fg='white')
        self.txt1.pack(pady=10)

        self.txt2 = customtkinter.CTkEntry(self.formFrame, placeholder_text='Criminal Name', width=400, bg=windowColor, fg='white')
        self.txt2.pack(pady=10)

        self.txt3 = customtkinter.CTkEntry(self.formFrame, width=400, bg=windowColor, fg='white')
        self.txt3.insert(0, datetime.date.today())
        self.txt3.pack(pady=10)

        self.txt4 = customtkinter.CTkEntry(self.formFrame, width=400, bg=windowColor, fg='white')
        self.txt4.insert(0, str(datetime.datetime.now().time()).split('.')[0])
        self.txt4.pack(pady=10)


        self.txt5 = customtkinter.CTkTextbox(self.formFrame, width=400)
        self.txt5.pack(pady=10)
        self.btn2 = customtkinter.CTkButton(self.formFrame, text='Submit', command=self.getvalues1)
        self.btn2.pack(pady=10)

        self.displayFrame = customtkinter.CTkFrame(self.sideFrame2)
        self.displayFrame.pack(pady=10, expand=True, fill='both', padx=10)

        self.label = Label(self.displayFrame)
        self.label.pack(anchor=NE)

        self.camLabel = Label(self.displayFrame)
        self.camLabel.pack(anchor=NW)

        file = Image.open('face.gif')
        self.file_frames = file.n_frames
        self.im = [PhotoImage(file='face.gif', format=f'gif -index {i}') for i in range(self.file_frames)]
        self.frameCount = 0
        self.animnate()

        self.btnFrame = customtkinter.CTkFrame(self.sideFrame2, width=int(sw / 3 * 1.3) + 200)
        self.btnFrame.pack(pady=10, padx=10)
        self.btnFrame.pack_propagate(0)
        self.cameraButton = customtkinter.CTkButton(self.btnFrame, text='Open Camera', command=self.openCamera, font=('arial', 20), width=200)
        self.cameraButton.grid(row=0, column=0, pady=20, padx=10)

        self.themeButton = customtkinter.CTkButton(self.btnFrame, text='Dark Theme', font=('arial', 20), width=200, command=self.changeTheme)
        self.themeButton.grid(row=0, column=2, pady=20, padx=10)

        self.root.mainloop()

    def openCamera(self):
        self.cap = cv2.VideoCapture(0)
        self.show_frames()
        self.cameraButton.configure(command=self.closeCamera, text='Close Camera')
        self.imageButton = customtkinter.CTkButton(self.btnFrame, text='Capture', font=('arial', 20), width=200, command=self.recface)
        self.imageButton.grid(row=0, column=1, pady=20, padx=10)

    def closeCamera(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.camLabel.configure(image='')
        self.cameraButton.configure(command=self.openCamera, text='Open Camera')
        self.imageButton.destroy()

    def recface(self):
        image_list = os.listdir('criminals_dir')
        for img in image_list:
            try:
                result = DeepFace.verify(img1_path=self.frame, img2_path=f"criminals_dir/{img}", model_name='Facenet512')
                if result['verified'] == True:
                    self.getValues(img)
                    break
            except:
                print('Face not Found')

    def getValues(self, img):
        self.conn = connect()
        self.cr = self.conn.cursor()
        q = f"select * from criminals where image='{img}'"
        self.cr.execute(q)
        data = self.cr.fetchall()
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt1.insert(0, data[0][0])
        self.txt2.insert(0, data[0][1])

    def getvalues1(self):
        criminal_id = self.txt1.get()
        center_id = self.txt0.get()
        date = self.txt3.get()
        time = self.txt4.get()
        description = self.txt5.get('1.0', 'end-1c')

        conn = connect()
        cr = conn.cursor()
        q = f"insert into criminal_remarks values(null,'{criminal_id}','{center_id}','{date}','{time}','{description}')"
        cr.execute(q)
        conn.commit()
        self.sendRemarks(criminal_id)
        msg.showinfo("success", "Remarks have been added.", parent=self.root)
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt5.delete('1.0', 'end')

    def animnate(self):
        self.label.configure(image=self.im[self.frameCount])
        self.frameCount += 1
        if self.frameCount == self.file_frames:
            self.frameCount = 0
        self.label.after(50, self.animnate)

    def show_frames(self):
        flag, self.frame = self.cap.read()
        if flag:
            self.frame = cv2.resize(self.frame, (720, 480))
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            _, self.frame = cv2.threshold(self.frame, 128, 255, cv2.THRESH_BINARY)
            self.frame = cv2.cvtColor(self.frame, cv2.COLOR_GRAY2RGB)
            self.frame = cv2.flip(self.frame, 1)
            img = Image.fromarray(self.frame)
            self.frame2 = ImageTk.PhotoImage(image=img)
            self.camLabel.imgtk = self.frame2
            self.camLabel.configure(image=self.frame2)
            self.camLabel.after(20, self.show_frames)

    def changeTheme(self):
        if self.themeButton.cget('text') == 'Dark Theme':
            customtkinter.set_appearance_mode('dark')
            self.themeButton.configure(text='Light Theme')
        else:
            customtkinter.set_appearance_mode('light')
            self.themeButton.configure(text='Dark Theme')

    def sendRemarks(self, criminal_id):
        q = f"select name, email from criminals where id='{criminal_id}'"
        self.cr.execute(q)
        criminals_data = self.cr.fetchone()
        center_id = self.txt0.get()

        q1 = f"select name, email, mobile, area, location from center where id='{center_id}'"
        self.cr.execute(q1)
        center_data = self.cr.fetchone()
        date = self.txt3.get()
        time = self.txt4.get()
        description = self.txt5.get('1.0', 'end-1c')

        message = f'''
            Criminal Name - {criminals_data[0]} has been identified at {time} on {date}.

            Here are Center Details - 
            Center Name - {center_data[0]}
            Center Mobile - {center_data[2]}
            Center Email - {center_data[1]}
            Location - {center_data[4]}
            Area - {center_data[3]}

            Here are Center Remarks - 
            {description}
        '''
        subject = "Criminal Report"

        x = maildemo.sendEmail(to=center_data[1], message=message, subject=subject)
        if x:
            msg.showinfo("Sent", "Mail has been sent.", parent=self.root)
        else:
            msg.showwarning('Warn', 'Mail could not be sent.', parent=self.root)



x = Main