from tkinter import *
from PIL import ImageTk, Image

# import sqlite3

root = Tk()
root.title('Registration')
root.geometry('1500x900')
root.configure(bg='Light Blue')
root.iconbitmap('icon.ico')
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
#         Mother_name text

#      )'''))




# title
Title_frame = Frame(root, bd=10,bg='black', width=1500, relief=RIDGE)
Title_frame.place(x=250,y=15)
Title_frame_label = Label(Title_frame, font=('Cambria 15 italic',25,'bold'), bg='light pink', text='SOFTWARICA COLLEGE OF IT AND E-COMMERCE',padx=20)
Title_frame_label.grid()

Entry_frame_details = Frame(root, bd=10,bg='black', width=1250, height=500, padx=250, relief=RIDGE)
Entry_frame_details.place(x=50,y=100)

# Using an image as a background
image = Image.open('school.PNG')
image = image.resize((1225, 475), Image.ANTIALIAS)
pic = ImageTk.PhotoImage(image)

img=Label(Entry_frame_details,image=pic).place(x=-252,y=0)


# Create text boxes

id = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=720,y=15)

first_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=-120,y=65)

Middle_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=320,y=65)

last_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=720,y=65)

Class = Entry(Entry_frame_details, font='Cambria 15 italic', width=13, borderwidth=5).place(x=-120,y=115)

age = Entry(Entry_frame_details, font='Cambria 15 italic', width=9, borderwidth=5).place(x=150,y=115)

address = Entry(Entry_frame_details, font='Cambria 15 italic', width=36, borderwidth=5).place(x=-120,y=170)

date_of_birth = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=720,y=115)

gender = Entry(Entry_frame_details, font='Cambria 15 italic', width=7, borderwidth=5).place(x=390,y=115)

father_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=325,y=220)

mother_name = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=-100,y=220)


Contact_number = Entry(Entry_frame_details, font='Cambria 15 italic', width=18, borderwidth=5).place(x=763,y=220)


Email_address = Entry(Entry_frame_details, font=('Cambria 15 italic', 14,), width=40, borderwidth=5).place(x=522,y=170)

Date_of_admission = Entry(Entry_frame_details, font='Cambria 15 italic', width=22, borderwidth=5).place(x=-80,y=270)



# create textLabels
label = Label(Entry_frame_details, text='ENTER STUDENT DETAILS', font=('Cambria 15 italic',17,'bold'), bg= 'Grey').place(x=-248,y=15)

id_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Student ID',bg='black', fg='white',relief=SUNKEN, bd=5).place(x=600,y=15)

first_name_label = Label(Entry_frame_details, text='First Name', font='Cambria 15 italic',bg='black', fg='white',relief=SUNKEN, bd=5).place(x=-248,y=65)

Middle_name_label = Label(Entry_frame_details, text='Middle Name', font='Cambria 15 italic',bg='black', fg='white',relief=SUNKEN, bd=5).place(x=190,y=65)

last_name_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Last Name',bg='black', fg='white',relief=SUNKEN, bd=5).place(x=600,y=65)

class_label = Label(Entry_frame_details, text='Class', font='Cambria 15 italic',bg='black', fg='white',relief=SUNKEN, bd=5).place(x=-248,y=115)

age_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Age',bg='black', fg='white',relief=SUNKEN, bd=5).place(x=90,y=115)

address_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Address',bg='black', fg='white',relief=SUNKEN, bd=5).place(x=-248,y=170)


date_of_birth_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Date Of Birth(*in AD)',bg='black', fg='white',relief=SUNKEN, bd=5).place(x=520,y=125)


gender_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Gender',bg='black', fg='white',relief=SUNKEN, bd=5).place(x=290,y=115)


father_name_label = Label(Entry_frame_details, font='Cambria 15 italic', text="Father's Name ",bg='black', fg='white',relief=SUNKEN, bd=5).place(x=185,y=220)


mother_name_label = Label(Entry_frame_details, font='Cambria 15 italic', text="Mother's Name ",bg='black', fg='white',relief=SUNKEN, bd=5).place(x=-248,y=220)


Contact_number_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Contact Number',bg='black', fg='white',relief=SUNKEN, bd=5).place(x=600,y=220)

Email_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Email address',bg='black', fg='white',relief=SUNKEN).place(x=365,y=170)

Date_of_admission_label = Label(Entry_frame_details, font='Cambria 15 italic', text='Date Of Admission',bg='black', fg='white', bd=5, relief=SUNKEN).place(x=-248,y=275)

# Creating space for records
def show_records():
    record = Toplevel()
    record.title("STUDENT RECORDS")
    record.geometry('1400x800')
    record.iconbitmap("icon.ico")
    Record_frame = Frame(record, bd=10, bg='Sky Blue', width=1250, height=500, padx=250, relief=RIDGE)
    Record_frame.place(x=50, y=100)

    record.mainloop()

submit_button = Button(Entry_frame_details, text='SUBMIT', font=('Cambria 15 italic',13,'bold'),width=10,bd=5)
submit_button.place(x=170,y=350)

show_button = Button(Entry_frame_details, text='SHOW RECORDS', font=('Cambria 15 italic',13,'bold'),width=15,bd=5,command = show_records)
show_button.place(x=450,y=350)

#conn.commit()
#conn.close()
mainloop()
