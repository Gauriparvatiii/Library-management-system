from tkinter import *
from tkinter import messagebox
import pymysql
from datetime import date, timedelta

def generate_issue_id():
    # Fetch the last issue ID from the database and increment it
    cur.execute("SELECT MAX(is_id) FROM issue")
    result = cur.fetchone()
    last_issue_id = result[0]
    if last_issue_id is not None:
        new_issue_id = int(last_issue_id) + 1
    else:
        new_issue_id = 1
    return str(new_issue_id)

def issueBook():
    def issueBookInfo():
        m_id = memberInfo1.get()
        b_id = bookInfo1.get()

        # Check if the book has available copies
        cur.execute(f"SELECT available_copies FROM books WHERE b_id = '{b_id}'")
        available_copies = cur.fetchone()[0]

        if available_copies > 0:
            date_of_issue = date.today()
            return_date = date_of_issue + timedelta(days=14)  # Assuming a 14-day return policy
            is_id = generate_issue_id()

            # Decrement available copies in the books table
            cur.execute(f"UPDATE books SET available_copies = available_copies - 1 WHERE b_id = '{b_id}'")

            # Insert into the issue table
            insertIssue = f"INSERT INTO issue (is_id, m_id, b_id, date_of_issue, return_date) VALUES " \
                          f"('{is_id}', '{m_id}', '{b_id}', '{date_of_issue}', '{return_date}')"

            try:
                cur.execute(insertIssue)
                con.commit()
                messagebox.showinfo('Success', "Book issued successfully")
            except Exception as e:
                messagebox.showinfo("Error", f"Can't add data into Database: {e}")
        else:
            messagebox.showinfo("Error", "No available copies for the selected book.")

    global memberInfo1, bookInfo1, Canvas1, con, cur, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mypass = "6922"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Issue Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Member ID
    lb1 = Label(labelFrame, text="Member ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    memberInfo1 = Entry(labelFrame)
    memberInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Book ID
    lb2 = Label(labelFrame, text="Book ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Issue Button
    issueBtn = Button(root, text="ISSUE BOOK", bg='#d1ccc0', fg='black', command=issueBookInfo)
    issueBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

