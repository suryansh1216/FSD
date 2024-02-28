from tkinter import *
import sqlite3
from addpeople import Addpeople
from tkinter import messagebox

con = sqlite3.connect('database.db')
cur = con.cursor()


class Mypeople(Toplevel):
    def __init__(self):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("My People")
        self.resizable(False, False)
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#4ba9a5')
        self.bottom.pack(fill=X)
        # top frame design
        self.top_image = PhotoImage(file='people.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=80, y=20)
        self.heading = Label(self.top, text='My People', font='ariel 15 bold', bg='white', fg='#4ba9a5')
        self.heading.place(x=280, y=50)

        self.scroll=Scrollbar(self.bottom, orient=VERTICAL)

        self.listbox= Listbox(self.bottom, width=40, height=27)
        self.listbox.grid(row=0, column=0, padx=(40,0))
        self.scroll.config(command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scroll.set)

        persons= cur.execute("select * from 'Person'").fetchall()
        count=0
        for person in persons:
            self.listbox.insert(count, str(person[0])+". "+person[1]+" "+person[2]+"   "+person[4])
            count+=1



        self.scroll.grid(row=0, column=1, sticky=N+S)

        #BUTTON
        btnadd=Button(self.bottom, text="Add", width=12, font='ariel 12 bold', command=self.add_people)
        btnadd.grid(row=0, column=2, padx=20, pady=10, sticky=N)

        btnupdate = Button(self.bottom, text="Update", width=12, font='ariel 12 bold', command=self.update_function)
        btnupdate.grid(row=0, column=2, padx=20, pady=50, sticky=N)

        btndelete = Button(self.bottom, text="Delete", width=12, font='ariel 12 bold', command= self.delete_person)
        btndelete.grid(row=0, column=2, padx=20, pady=90, sticky=N)

    def add_people(self):
        add_page=Addpeople()
        self.destroy()

    def update_function(self):
        selected_item= self.listbox.curselection()
        person= self.listbox.get(selected_item)
        person_id= person.split(".")[0]
        updtatepage= Update(person_id)

    def delete_person(self):
        selected_item = self.listbox.curselection()
        person = self.listbox.get(selected_item)
        person_id = person.split(".")[0]

        query="delete from Person where person_id= {} ".format(person_id)
        answer=messagebox.askquestion("Warning", "Are you sure you want to delete")
        if answer=='yes':
           try:
               cur.execute(query)
               con.commit()
               messagebox.showinfo("Success", "Contact Deleted")
               self.destroy()
           except Exception as e:
               messagebox.showinfo("Info", str(e))



class Update(Toplevel):
    def __init__(self, person_id):
        Toplevel.__init__(self)
        self.geometry("650x650+600+200")
        self.title("Update Person")
        self.resizable(False, False)
        query = "select * from 'Person' where Person_id= '{}'".format(person_id)
        result = cur.execute(query).fetchone()
        print("result:", result)
        self.person_id=person_id
        person_name = result[1]
        person_surname = result[2]
        person_email = result[3]
        person_phone = result[4]
        self.top = Frame(self, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(self, height=500, bg='#4ba9a5')
        self.bottom.pack(fill=X)
        # top frame design
        self.top_image = PhotoImage(file='people.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=80, y=20)
        self.heading = Label(self.top, text='Update Person', font='ariel 15 bold', bg='white', fg='#4ba9a5')
        self.heading.place(x=280, y=50)

        # name
        self.label_name = Label(self.bottom, text="   Name  ", font='ariel 12 bold', fg='black')
        self.label_name.place(x=40, y=40)
        self.entry_name = Entry(self.bottom, width=50, bd=4)
        self.entry_name.insert(0, person_name)
        self.entry_name.place(x=150, y=40)

        # surname
        self.label_surname = Label(self.bottom, text="Surname", font='ariel 12 bold', fg='black')
        self.label_surname.place(x=40, y=100)
        self.entry_surname = Entry(self.bottom, width=50, bd=4)
        self.entry_surname.insert(0, person_surname)
        self.entry_surname.place(x=150, y=100)
        # email
        self.label_email = Label(self.bottom, text="  E-mail   ", font='ariel 12 bold', fg='black')
        self.label_email.place(x=40, y=160)
        self.entry_email = Entry(self.bottom, width=50, bd=4)
        self.entry_email.insert(0, person_email)
        self.entry_email.place(x=150, y=160)

        # phone_number
        self.label_phone = Label(self.bottom, text="  Phone   ", font='ariel 12 bold', fg='black')
        self.label_phone.place(x=40, y=220)
        self.entry_phone = Entry(self.bottom, width=50, bd=4)
        self.entry_phone.insert(0, person_phone)
        self.entry_phone.place(x=150, y=220)

        # Button
        button = Button(self.bottom, text="Update Person", command=self.update_people)
        button.place(x=280, y=280)

    def update_people(self):
        person_id=self.person_id
        name = self.entry_name.get()
        surname = self.entry_surname.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        query = "update Person set Person_name= '{}', Person_surname= '{}', Person_email= '{}', phone='{}' where person_id={}".format(name, surname, email, phone, person_id)
        try:
            cur.execute(query)
            con.commit()
            messagebox.showinfo("Success", "Contact Updated")
        except Exception as e:
            print(e)









