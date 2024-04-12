from tkinter import *
from tkinter import messagebox
import pymysql

def memberRegister():
    name = memberInfo1.get()
    email = memberInfo2.get()
    phone = memberInfo3.get()
    
    insertMembers = f"INSERT INTO members (name, email, phone) VALUES ('{name}', '{email}', '{phone}')"
    
    try:
        cur.execute(insertMembers)
        con.commit()
        messagebox.showinfo('Success', "Member added successfully")
    except Exception as e:
        messagebox.showinfo("Error", f"Can't add data into Database: {e}")
    
    root.destroy()

def generate_member_id():
    # Fetch the last member ID from the database and increment it
    cur.execute("SELECT MAX(m_id) FROM members")
    result = cur.fetchone()
    last_member_id = result[0]
    if last_member_id is not None:
        new_member_id = int(last_member_id) + 1
    else:
        new_member_id = 1
    return str(new_member_id)

def addMember():
    global memberInfo1, memberInfo2, memberInfo3, Canvas1, con, cur, memberTable, root
    
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mypass = "6922"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    memberTable = "members"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Members", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Member Name
    lb1 = Label(labelFrame, text="Member Name : ", bg='black', fg='white')
    lb1.place(relx=0.05, rely=0.2, relheight=0.08)

    memberInfo1 = Entry(labelFrame)
    memberInfo1.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Email
    lb2 = Label(labelFrame, text="Email : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    memberInfo2 = Entry(labelFrame)
    memberInfo2.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # Phone
    lb3 = Label(labelFrame, text="Phone : ", bg='black', fg='white')
    lb3.place(relx=0.05, rely=0.50, relheight=0.08)

    memberInfo3 = Entry(labelFrame)
    memberInfo3.place(relx=0.3, rely=0.50, relwidth=0.62, relheight=0.08)

    # Submit Button
    SubmitBtn = Button(root, text="SUBMIT", bg='#d1ccc0', fg='black', command=memberRegister)
    SubmitBtn.place(relx=0.28, rely=0.9, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.53, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()


