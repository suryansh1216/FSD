from tkinter import *
import sqlite3
from tkinter import messagebox
conn=sqlite3.connect('database.db')
cur= conn.cursor()
class Addpeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("Add New People")
        self.resizable(False, False)
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#4ba9a5')
        self.bottom.pack(fill=X)
        # top frame design
        self.top_image = PhotoImage(file='people.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=80, y=20)
        self.heading = Label(self.top, text='Add New People', font='ariel 15 bold', bg='white', fg='#4ba9a5')
        self.heading.place(x=280, y=50)

        #name
        self.label_name=Label(self.bottom, text="   Name  ", font='ariel 12 bold', fg='black')
        self.label_name.place(x=40, y=40)
        self.entry_name= Entry(self.bottom, width=50, bd=4)
        self.entry_name.insert(0, "")
        self.entry_name.place(x=150, y=40)

        #surname
        self.label_surname = Label(self.bottom, text="Surname", font='ariel 12 bold', fg='black')
        self.label_surname.place(x=40, y=100)
        self.entry_surname = Entry(self.bottom, width=50, bd=4)
        self.entry_surname.insert(0, "")
        self.entry_surname.place(x=150, y=100)
        #email
        self.label_email = Label(self.bottom, text="  E-mail   ", font='ariel 12 bold', fg='black')
        self.label_email.place(x=40, y=160)
        self.entry_email = Entry(self.bottom, width=50, bd=4)
        self.entry_email.insert(0, "")
        self.entry_email.place(x=150, y=160)

        #phone_number
        self.label_phone = Label(self.bottom, text="  Phone   ", font='ariel 12 bold', fg='black')
        self.label_phone.place(x=40, y=220)
        self.entry_phone = Entry(self.bottom, width=50, bd=4)
        self.entry_phone.insert(0, "")
        self.entry_phone.place(x=150, y=220)

        #Button
        button=Button(self.bottom, text="Add Person", command=self.add_people)
        button.place(x=280, y=280)

    def add_people(self):
        name= self.entry_name.get()
        surname= self.entry_surname.get()
        email= self.entry_email.get()
        phone= self.entry_phone.get()

        if name!="" and surname!="" and email!="" and phone !="":
            try:
                #add to thr database
                query="insert into 'Person' (Person_name, Person_surname, Person_email, phone) values(?,?,?,?) "
                cur.execute(query,(name, surname, email, phone))
                conn.commit()
                messagebox.showinfo("Success","Contact Added")
            except Exception as e:
                messagebox.showerror("Error", str(e))

        else:
            messagebox.showerror("Error","Fill all the fields", icon='warning')



