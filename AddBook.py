from tkinter import *
from tkinter import messagebox
import pymysql

def bookRegister():
    title = bookInfo2.get()
    author = bookInfo3.get()
    no_copies = int(bookInfo4.get())
    
    # Automatically generate book ID
    bid = generate_book_id()
    available_copies = no_copies

    insertBooks = f"INSERT INTO books (b_id, title, author, no_copies, available_copies) VALUES ('{bid}', '{title}', '{author}', {no_copies}, {available_copies})"
    
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', "Book added successfully")
    except Exception as e:
        messagebox.showinfo("Error", f"Can't add data into Database: {e}")
    
    root.destroy()

def generate_book_id():
    # Fetch the last book ID from the database and increment it
    cur.execute("SELECT MAX(b_id) FROM books")
    result = cur.fetchone()
    last_book_id = result[0]
    if last_book_id is not None:
        new_book_id = int(last_book_id) + 1
    else:
        new_book_id = 1
    return str(new_book_id)

def addBookGUI():
    global bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mypass = "6922"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    bookTable = "books"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Title
    lb2 = Label(labelFrame, text="Title : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Book Author
    lb3 = Label(labelFrame, text="Author : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Number of Copies
    lb4 = Label(labelFrame, text="Number of Copies : ", bg='black', fg='white')
    lb4.place(relx=0.05, rely=0.65, relheight=0.08)

    bookInfo4 = Entry(labelFrame)
    bookInfo4.place(relx=0.3, rely=0.65, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=bookRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


