from tkinter import *
from tkinter import messagebox
import pymysql

def viewIssuedBooks():
    def viewIssuedBooksInfo():
        member_id = memberInfo.get()

        # Query to retrieve details of books issued by the member
        query = f"SELECT issue.is_id, issue.m_id, books.title, books.author " \
                f"FROM books, issue " \
                f"WHERE books.b_id = issue.b_id AND issue.m_id = '{member_id}'"

        try:
            # Execute the query
            cur.execute(query)

            # Fetch all the details of books issued by the member
            issued_books = cur.fetchall()

            if not issued_books:
                messagebox.showinfo("No Issued Books", f"No books issued for member with ID {member_id}")
            else:
                books_info = f"Details of books issued by member with ID {member_id}:\n"
                for book in issued_books:
                    book_info = f"Issue ID: {book[0]}, Member ID: {book[1]}, Book Title: {book[2]}, Author: {book[3]}"
                    books_info += f"{book_info}\n"

                messagebox.showinfo("Issued Books Information", books_info)

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}")

    def listAllIssuedBooks():
        # Query to retrieve details of all issued books
        query = f"SELECT issue.is_id, issue.m_id, books.title, books.author " \
                f"FROM books, issue " \
                f"WHERE books.b_id = issue.b_id"

        try:
            # Execute the query
            cur.execute(query)

            # Fetch all the details of all issued books
            all_issued_books = cur.fetchall()

            if not all_issued_books:
                messagebox.showinfo("No Issued Books", "No books have been issued.")
            else:
                books_info = "Details of all issued books:\n"
                for book in all_issued_books:
                    book_info = f"Issue ID: {book[0]}, Member ID: {book[1]}, Book Title: {book[2]}, Author: {book[3]}"
                    books_info += f"{book_info}\n"

                messagebox.showinfo("Issued Books Information", books_info)

        except pymysql.Error as e:
            messagebox.showerror("Error", f"Error: {e}")

    global memberInfo, Canvas1, con, cur, issueTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mypass = "6922"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    issueTable = "issue"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Issued Books", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Member ID
    lb2 = Label(labelFrame, text="Member ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    memberInfo = Entry(labelFrame)
    memberInfo.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # View Issued Books Button
    viewIssuedBtn = Button(root, text="VIEW ISSUED BOOKS", bg='#d1ccc0', fg='black', command=viewIssuedBooksInfo)
    viewIssuedBtn.place(relx=0.25, rely=0.7, relwidth=0.4, relheight=0.08)

    # List All Issued Books Button
    listAllIssuedBtn = Button(root, text="LIST ALL ISSUED BOOKS", bg='#d1ccc0', fg='black', command=listAllIssuedBooks)
    listAllIssuedBtn.place(relx=0.25, rely=0.8, relwidth=0.4, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


