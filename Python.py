from tkinter import *
import datetime
from mypeople import Mypeople
from addpeople import Addpeople

date = datetime.datetime.now().date()
date = str(date)


class Application(object):
    def __init__(self, master):
        self.master = master

        self.top = Frame(master, height=150, bg='white')
        self.top.pack(fill=X)

        self.bottom = Frame(master, height=500, bg='#4ba9a5')
        self.bottom.pack(fill=X)
        # top frame design
        self.top_image = PhotoImage(file='contacts.png')
        self.top_image_label = Label(self.top, image=self.top_image, bg='white')
        self.top_image_label.place(x=80, y=20)
        self.heading = Label(self.top, text='Phonebook', font='ariel 15 bold', bg='white', fg='#4ba9a5')
        self.heading.place(x=280, y=50)
        self.date_lbl = Label(self.top, text="Today's date:" + date, font='ariel 12 bold', fg='#4ba9a5', bg='white')
        self.date_lbl.place(x=450, y=110)

        # button_1 view people
        self.viewButton = Button(self.bottom, text="  My People  ", font='ariel 12 bold', command=self.my_people)
        self.viewButton.place(x=280, y=70)
        # button_1 add people
        self.addButton = Button(self.bottom, text=" Add People ", font='ariel 12 bold', command=self.addpeoplefunction)
        self.addButton.place(x=280, y=130)


    def my_people(self):
        people = Mypeople()

    def addpeoplefunction(self):
        addpeoplewindow= Addpeople()



def main():
    root = Tk()
    app = Application(root)
    root.title("Phonebook")
    root.geometry("660x550+350+200")
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    main()