import pymysql
from datetime import date, timedelta

def add_to_blacklist():
    mypass = "6922"
    mydatabase = "db"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()
    # Fetch records from the issue table where return_date is overdue by more than 30 days
    cur.execute("SELECT * FROM issue WHERE return_date < (CURDATE() - INTERVAL 30 DAY)")
    overdue_records = cur.fetchall()

    for record in overdue_records:
        m_id, is_id, b_id, _, return_date = record
        no_days_due = (date.today() - return_date).days

        # Insert into the blacklist table
        insertBlacklist = f"INSERT INTO blacklist (m_id, is_id, b_id, no_days_due) " \
                           f"VALUES ('{m_id}', '{is_id}', '{b_id}', {no_days_due})"
        
        try:
            cur.execute(insertBlacklist)
            con.commit()
            print(f"Member ID {m_id} added to the blacklist.")
        except Exception as e:
            print(f"Error adding member to the blacklist: {e}")


add_to_blacklist()
