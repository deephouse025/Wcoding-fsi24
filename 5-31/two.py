
from flask import Flask, request
import sqlalchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/In-Class")

# **Exercise: Write Data**
@app.get("/three")
def phones():
  returnStr = ""
  
  with db.begin() as conn:
    returnStr = ""
    
    
    
# **1:** `insert` an entry **without** using a prepared query
# The phone is a Samsung S8 Plus owned by Alexis, weighs 173g, the comment is “Good for watching videos”, and the price is $80
    res = conn.execute(
        text("""
        INSERT INTO phones (model, brand, owner, price, weight, comment)
        VALUES ('S8+', "Samsung", "Alexis", 80, 173, "Good for watching videos")
        """),
    )
  
      
# **2 :** `insert` an entry using a **prepared** query

# The phone is an Apple iPhone 12 owned by Alex, weighs 164g, the comment is “My company provided a phone i don’t need this one anymore, brand new”, and the price is $700
    # res = conn.exectute(
    #     text("""
    #          insert into phones (model, brand, owner, price, weight, comment) values (:model, :brand, :owner, :price, :weight, :comment)
    #          """),
    #         {
    #             'brand': 'Apple'
    #             'model': 'iPhone 12'
    #             'owner': 'Alex'
                
    #         }
    # )


# **3 :** `update` **without** using a prepared query

# Reduce the price of Alex’s iPhone 12 to $690

# **4 :** `update` **using** a prepared query

# Change the comment on Alexis’s Phone by appending: “And listening to music!”

# **5 :** `delete` an entry

# Delete Alexis’ Samsung S8 from the table
    returnStr += f'<h3>Inserted: {res.rowcount}</h3>'       

    return returnStr

