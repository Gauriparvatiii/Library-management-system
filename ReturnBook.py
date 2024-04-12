from tkinter import *
from tkinter import messagebox
import pymysql
from datetime import date, timedelta

def returnBook():
    is_id = returnInfo1.get()

    # Fetch record from the issue table using is_id
    cur.execute(f"SELECT * FROM issue WHERE is_id = '{is_id}'")
    record = cur.fetchone()

    if record:
        m_id, _, b_id, _, return_date = record
        no_days_due, fine_amt = calculate_fine(return_date)

        # Check if there are dues in the due table
        cur.execute(f"SELECT * FROM due WHERE is_id = '{is_id}'")
        due_record = cur.fetchone()

        # Remove record from the issue table
        cur.execute(f"DELETE FROM issue WHERE is_id = '{is_id}'")
        con.commit()

        # If there are dues, remove record from the due table
        if due_record:
            cur.execute(f"DELETE FROM due WHERE is_id = '{is_id}'")
            con.commit()

        # Increment available copies in the books table
        cur.execute(f"UPDATE books SET available_copies = available_copies + 1 WHERE b_id = '{b_id}'")
        con.commit()

        messagebox.showinfo('Success', "Book returned successfully")
    else:
        messagebox.showinfo('Error', "No record found with the provided Issue ID")

def calculate_fine(return_date):
    today = date.today()
    no_days_due = max(0, (today - return_date).days)  # Calculate overdue days
    fine_amt = no_days_due * 5  # 5 rupees per day
    return no_days_due, fine_amt

def returnBookGUI():
    global returnInfo1, Canvas1, con, cur, root

    
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

    headingLabel = Label(headingFrame1, text="Return Book", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Issue ID
    lb1 = Label(labelFrame, text="Issue ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    returnInfo1 = Entry(labelFrame)
    returnInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Return Button
    returnBtn = Button(root, text="RETURN BOOK", bg='#d1ccc0', fg='black', command=returnBook)
    returnBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

