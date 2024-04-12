from tkinter import *
from tkinter import messagebox
import pymysql
from datetime import date, timedelta

def renewBook():
    is_id = renewInfo1.get()

    # Fetch record from the issue table using is_id
    cur.execute(f"SELECT * FROM issue WHERE is_id = '{is_id}'")
    record = cur.fetchone()

    if record:
        m_id, _, b_id, _, return_date = record

        # Calculate the new return date (extend by 15 days)
        new_return_date = return_date + timedelta(days=15)

        # Update the return_date in the issue table
        cur.execute(f"UPDATE issue SET return_date = '{new_return_date}' WHERE is_id = '{is_id}'")
        con.commit()

        messagebox.showinfo('Success', f"Book renewed successfully. New return date: {new_return_date}")
    else:
        messagebox.showinfo('Error', "No record found with the provided Issue ID")

def renewBookGUI():
    global renewInfo1, Canvas1, con, cur, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mypass = "6922"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    
    if 'renewFrame' in globals():
        renewFrame.destroy()

    renewFrame = Frame(root, bg="#FFBB00", bd=5)
    renewFrame.place(relx=0.2, rely=0.3, relwidth=0.6, relheight=0.16)

    renewLabel = Label(renewFrame, text="Renew Book", bg='black', fg='white', font=('Courier', 15))
    renewLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.5, relwidth=0.8, relheight=0.4)

    # Issue ID
    lb1 = Label(labelFrame, text="Issue ID : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    renewInfo1 = Entry(labelFrame)
    renewInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Renew Button
    renewBtn = Button(root, text="RENEW BOOK", bg='#d1ccc0', fg='black', command=renewBook)
    renewBtn.place(relx=0.28, rely=0.8, relwidth=0.18, relheight=0.08)


