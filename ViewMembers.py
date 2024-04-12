from tkinter import *
import pymysql
from tkinter import ttk, messagebox

def viewMembersGUI():
    global membersInfo, Canvas1, con, cur, membersTable, root

    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("600x500")

    mypass = "6922"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    membersTable = "members"

    Canvas1 = Canvas(root)
    Canvas1.config(bg="#ff6e40")
    Canvas1.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(root, bg="#FFBB00", bd=5)
    headingFrame1.place(relx=0.25, rely=0.1, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="View Members", bg='black', fg='white', font=('Courier', 15))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    labelFrame = Frame(root, bg='black')
    labelFrame.place(relx=0.1, rely=0.4, relwidth=0.8, relheight=0.4)

    # Member ID
    lb2 = Label(labelFrame, text="Member ID : ", bg='black', fg='white')
    lb2.place(relx=0.05, rely=0.35, relheight=0.08)

    membersInfo = Entry(labelFrame)
    membersInfo.place(relx=0.3, rely=0.35, relwidth=0.62, relheight=0.08)

    # View All Members Button
    viewAllBtn = Button(root, text="VIEW ALL MEMBERS", bg='#d1ccc0', fg='black', command=viewAllMembers)
    viewAllBtn.place(relx=0.28, rely=0.75, relwidth=0.18, relheight=0.08)

    # View Specific Member Button
    viewMemberBtn = Button(root, text="VIEW MEMBER", bg='#d1ccc0', fg='black', command=viewMemberInfo)
    viewMemberBtn.place(relx=0.53, rely=0.75, relwidth=0.18, relheight=0.08)

    quitBtn = Button(root, text="Quit", bg='#f7f1e3', fg='black', command=root.destroy)
    quitBtn.place(relx=0.4, rely=0.9, relwidth=0.18, relheight=0.08)

    root.mainloop()

def viewAllMembers():
    global membersInfo, Canvas1, con, cur, membersTable, root

    # Query to retrieve all members
    query = f"SELECT * FROM {membersTable}"

    try:
        # Execute the query
        cur.execute(query)

        # Fetch all members
        members = cur.fetchall()

        if not members:
            messagebox.showinfo("No Members", "No members available.")
        else:
            members_info = "All Members:\n"
            for member in members:
                members_info += f"Name: {member[1]}\nEmail: {member[2]}\nPhone: {member[3]}\n\n"

            messagebox.showinfo("Members Information", members_info)

    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error: {e}")

def viewMemberInfo():
    global membersInfo, Canvas1, con, cur, membersTable, root

    member_id = membersInfo.get()

    # Query to find a member with a specific ID
    query = f"SELECT * FROM {membersTable} WHERE m_id = '{member_id}'"

    try:
        # Execute the query
        cur.execute(query)

        # Fetch the member with the specified ID
        member = cur.fetchone()

        if not member:
            messagebox.showinfo("No Member", f"No member found with ID {member_id}")
        else:
            member_info = f"Member with ID {member_id}:\nName: {member[1]}\nEmail: {member[2]}\nPhone: {member[3]}"
            messagebox.showinfo("Member Information", member_info)

    except pymysql.Error as e:
        messagebox.showerror("Error", f"Error: {e}")

