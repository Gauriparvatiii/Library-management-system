from tkinter import *
from PIL import Image,ImageTk
from AddBook import addBookGUI, bookRegister, generate_book_id
from ViewBooks import viewBooks
from Issue import issueBook
from ReturnBook import returnBookGUI
from RenewBook import renewBookGUI
from AddMember import addMember, memberRegister, generate_member_id
from Blacklist import add_to_blacklist
from Due import generate_due_id, calculate_fine, check_due_books, checkDueBooksGUI
from Finddue import viewDuesGUI, viewDuesInfo
from Viewbookissued import viewIssuedBooks
from ViewMembers import viewMembersGUI
from tkinter import messagebox
import pymysql
from datetime import date, timedelta

def mainGUI():
    root = Tk()
    root.title("Library Management System")
    root.minsize(width=800, height=600)
    root.geometry("600x500")

    img_path = r"C:\Users\LENOVO\Python\dbms\lib.jpg"
    img = Image.open(img_path)
    img = img.resize((800, 600), Image.BICUBIC)


    
    background_image = ImageTk.PhotoImage(img)

    # Create a label to display the background image
    background_label = Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)


    mypass = "6922"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(headingFrame1, text="Library Management System", bg='black', fg='white', font=('Courier', 20))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Add Member Button
    addMemberBtn = Button(root, text="Add Member", bg='#d1ccc0', fg='black', command=addMember)
    addMemberBtn.place(relx=0.28, rely=0.3, relwidth=0.45, relheight=0.1)

    # Add Book Button
    addBookBtn = Button(root, text="Add Book", bg='#d1ccc0', fg='black', command=addBookGUI)
    addBookBtn.place(relx=0.28, rely=0.45, relwidth=0.45, relheight=0.1)

    # Issue Book Button
    issueBookBtn = Button(root, text="Issue Book", bg='#d1ccc0', fg='black', command=issueBook)
    issueBookBtn.place(relx=0.28, rely=0.6, relwidth=0.45, relheight=0.1)

    # Return Book Button
    returnBookBtn = Button(root, text="Return Book", bg='#d1ccc0', fg='black', command=returnBookGUI)
    returnBookBtn.place(relx=0.28, rely=0.75, relwidth=0.45, relheight=0.1)

    # View Issued Books Button
    viewIssuedBooksBtn = Button(root, text="View Issued Books", bg='#d1ccc0', fg='black', command=viewIssuedBooks)
    viewIssuedBooksBtn.place(relx=0.28, rely=0.9, relwidth=0.45, relheight=0.1)

    # Find Dues Button
    findDuesBtn = Button(root, text="Find Dues", bg='#d1ccc0', fg='black', command=viewDuesGUI)
    findDuesBtn.place(relx=0.75, rely=0.75, relwidth=0.2, relheight=0.1)

    # Renew Book Button
    renewBookBtn = Button(root, text="Renew Book", bg='#d1ccc0', fg='black', command=renewBookGUI)
    renewBookBtn.place(relx=0.75, rely=0.6, relwidth=0.2, relheight=0.1)

    # View Members Button
    viewMembersBtn = Button(root, text="View Members", bg='#d1ccc0', fg='black', command=viewMembersGUI)
    viewMembersBtn.place(relx=0.75, rely=0.45, relwidth=0.2, relheight=0.1)

    # View Available Books Button
    viewBooksBtn = Button(root, text="View Available Books", bg='#d1ccc0', fg='black', command=viewBooks)
    viewBooksBtn.place(relx=0.75, rely=0.3, relwidth=0.2, relheight=0.1)

    add_to_blacklist()
    checkDueBooksGUI()

    root.mainloop()

mainGUI()
