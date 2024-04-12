from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

def viewBooks():
    mypass = "6922"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    data = cur.fetchall()

    if not data:
        messagebox.showinfo('Error', 'No books available in the library.')
        return

    global root

    root = Tk()
    root.title("Library - View Books")
    root.geometry("800x500")

    tree = ttk.Treeview(root)
    tree["columns"] = ("1", "2", "3", "4", "5")
    tree.heading("#0", text="ID")
    tree.column("#0", anchor="center", width=40)
    tree.heading("1", text="Book ID")
    tree.column("1", anchor="center", width=100)
    tree.heading("2", text="Title")
    tree.column("2", anchor="center", width=200)
    tree.heading("3", text="Author")
    tree.column("3", anchor="center", width=150)
    tree.heading("4", text="No. of Copies")
    tree.column("4", anchor="center", width=100)
    tree.heading("5", text="Available Copies")
    tree.column("5", anchor="center", width=120)

    for record in data:
        tree.insert("", "end", values=record)

    tree.pack(expand=True, fill="both")

    root.mainloop()


