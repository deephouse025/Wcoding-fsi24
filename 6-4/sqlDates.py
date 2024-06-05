from flask import Flask, request
import sqlalchemy
from sqlalchemy.sql import text
import datetime

app = Flask(__name__)

db = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/In-Class")

@app.get("/time")
def times():
    with db.begin() as chats:    
    # # testing
        returnStr = ""
        all = chats.execute(text("SELECT id, user, message, created_at FROM chat_messages"))
        for 
        returnStr += 
        
        # return returnStr
    # **1**: Get all the messages sent today.
        today = datetime.now
        print(today)
        response = chats.execute(text("SELECT message FROM chat_messages WHERE created_at=CURDATE()"))


    # **2:** Get messages from a specific time today.
        specific_time = "10:30"
        response = chats.execute(text(f"select created_at where created_at = :specific_time"))

    # **3:** Get messages from a date that has messages, that were sent between two specific hours.
        "SELECT id, user, message, created_at From chat_messages WHERE created_at >= :start_time AND created_at <= :end_time"

    # **4:** Put some messages into the table that are dated as 2 days ago.
       "SELECT id, user, message, created_at FROM chat_messages WHERE "

    # **5:** Get the messages from 2 days ago.

    # **6:** Get the messages from 2 days ago with a specific time.

    # **7:** Get the date as “dd/mm/yyyy” (common European format) and get the first 20 messages — do this **without the DATE_FORMAT function**
        "SELECT *, DAY(created_at) AS day, MONTH(created_at) AS day, MONTH(created_at) AS month, YEAR(created)"
    # **8:**  Get the date as “mm/dd/yyyy” (common US format) and display the first 15 messages — do this **with the DATE_FORMAT function**
        "SELECT username, message, DATE_FORMAT(date_created, '%m/%d/%y') AS us_date FROM chat ORDER BY us_date LIMIT 15"
    # **9:** Add an expiration date field to your table and update every row so that it is 2 months after the created_at value for each row — update all the rows in the database with a single query
