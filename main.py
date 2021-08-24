from tkinter import *
# import sqlite3

root = Tk()
root.title('Registration')
root.geometry('1500x900')
# connect to database
#conn = sqlite3.connect('Schoolmanagement.db')
# create a cursor
#c = conn.cursor()

# c.execute(('''CREATE TABLE addressess(
#         first_name  text ,
#        last_name  text ,
#         age integer ,
#         gender text ,
#         date_of_birth integer,
#         Class integer,
#         Contact_number integer,
#          Email_address text,
#         address text ,
#          Father_name text ,
#         Mother_name text ,
#         Complaints

#      )'''))

# title
Title_frame = Frame(root, bd=10, width=1500, padx=20, relief=RIDGE)
Title_frame.pack(side=TOP)
Title_frame_label = Label(Title_frame, font=('Cambria 15 italic',25,'bold'), bg='light pink', text='SCHOOL MANAGEMENT SYSTEM',
                          padx=20)
Title_frame_label.grid()

Bottom_frame_details = Frame(root, bd=10, width=1350, height=200, padx=25, relief=RIDGE)
Bottom_frame_details.pack(side=BOTTOM)
Entry_frame_details = Frame(root, bd=10, width=1250, height=900, padx=250, relief=RIDGE)
Entry_frame_details.pack(side=BOTTOM)

# create textLabels
first_name_label = Label(Entry_frame_details, text='First Name', font='Cambria 15 italic').place(x=-250,y=55)

Middle_name_label = Label(Entry_frame_details, text='Middle Name', font='Cambria 15 italic').place(x=200,y=55)

last_name_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Last Name').place(x=600,y=55)

class_label = Label(Entry_frame_details, text='Class', font='Cambria 15 italic').place(x=-250,y=105)

age_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Age').place(x=90,y=105)


address_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Address').place(x=-250,y=160)


date_of_birth_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Date Of Birth(*in AD)').place(x=520,y=105)


gender_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Gender').place(x=290,y=105)


father_name_label = Label(Entry_frame_details, font='Cambria 15 italic', text="Father's name ").place(x=185,y=210)


mother_name_label = Label(Entry_frame_details, font='Cambria 15 italic', text="Mother's name ").place(x=-250,y=210)


Contact_number_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Contact Number').place(x=600,y=210)

Email_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Email address').place(x=365,y=160)

Date_of_admission_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Date of admission').place(x=-250,y=260)

complain_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Complaints ').place(x=250,y=260)

# create textboxes

first_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=-120,y=55)

Middle_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=330,y=55)

last_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=720,y=55)

Class = Entry(Entry_frame_details, font='Cambria 15 italic', width=13, borderwidth=5).place(x=-120,y=105)

age = Entry(Entry_frame_details, font='Cambria 15 italic', width=9, borderwidth=5).place(x=150,y=105)

address = Entry(Entry_frame_details, font='Cambria 15 italic', width=36, borderwidth=5).place(x=-120,y=160)

date_of_birth = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=720,y=105)

gender = Entry(Entry_frame_details, font='Cambria 15 italic', width=7, borderwidth=5).place(x=390,y=105)

father_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=325,y=210)

mother_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=-100,y=210)


Contact_number = Entry(Entry_frame_details, font='Cambria 15 italic', width=18, borderwidth=5).place(x=763,y=210)


Email_address = Entry(Entry_frame_details, font=('Cambria 15 italic', 14,), width=40, borderwidth=5).place(x=522,y=160)

Date_of_admission = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=-80,y=260)

complain = Entry(Entry_frame_details, font='Cambria 15 italic', width=53, borderwidth=5).place(x=380,y=260)

#conn.commit()
#conn.close()
mainloop()
