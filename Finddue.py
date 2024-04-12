from tkinter import *
import pymysql
from tkinter import messagebox


def viewDuesGUI():
    global duesInfo, Canvas1, con, cur, duesTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mypass = "6922"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    duesTable = "due"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Dues", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Member ID
    lb2 = Label(labelFrame, text="Member ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    duesInfo = Entry(labelFrame)
    duesInfo.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="VIEW DUES", bg='#d1ccc0', fg='black', command=viewDuesInfo)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def viewDuesInfo():
    global duesInfo, Canvas1, con, cur, duesTable, root

    member_id = duesInfo.get()

    # Query to find dues for a specific member
    query = f"SELECT * FROM {duesTable} WHERE m_id = '{member_id}'"

    try:
        # Execute the query
        cur.execute(query)

        # Fetch all the dues for the member
        dues = cur.fetchall()

        if not dues:
            messagebox.showinfo("No Dues", f"No dues found for member with ID {member_id}")
        else:
            dues_info = f"Dues for member with ID {member_id}:\n"
            for due in dues:
                dues_info += f"{due}\n"

            messagebox.showinfo("Dues Information", dues_info)

    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error: {e}")


