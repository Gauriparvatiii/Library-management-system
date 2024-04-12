from tkinter import *
from tkinter import messagebox
import pymysql
from datetime import date, timedelta

def generate_due_id():
    # Fetch the last due ID from the database and increment it
    cur.execute("SELECT MAX(due_id) FROM due")
    result = cur.fetchone()
    last_due_id = result[0]
    if last_due_id is not None:
        new_due_id = int(last_due_id) + 1
    else:
        new_due_id = 1
    return str(new_due_id)

def calculate_fine(return_date):
    today = date.today()
    no_days_due = (today - return_date).days
    fine_amt = max(0, no_days_due * 5)  # 5 rupees per day, fine cannot be negative
    return no_days_due, fine_amt

def check_due_books():
    # Fetch records from the issue table where return_date is due
    cur.execute("SELECT * FROM issue WHERE return_date < CURDATE()")
    due_books = cur.fetchall()

    for record in due_books:
        m_id, is_id, b_id, _, return_date = record
        no_days_due, fine_amt = calculate_fine(return_date)

        # Insert into the due table
        due_id = generate_due_id()
        insertDue = f"INSERT INTO due (due_id, m_id, is_id, b_id, no_days_due, fine_amt) " \
                    f"VALUES ('{due_id}', '{m_id}', '{is_id}', '{b_id}', {no_days_due}, {fine_amt})"
        
        try:
            cur.execute(insertDue)
            con.commit()
            messagebox.showinfo('Success', f"Due record added successfully for Member ID: {m_id}")
        except Exception as e:
            messagebox.showinfo("Error", f"Can't add data into Due table: {e}")

def checkDueBooksGUI():
    global con, cur
    
    mypass = "6922"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    check_due_books()

checkDueBooksGUI()
