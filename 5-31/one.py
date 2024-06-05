from flask import Flask, request
import sqlalchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/In-Class")

@app.get("/phones")
def phones():
  returnStr = ""
  
  with db.begin() as conn:
    returnStr = ""
    response = conn.execute(text("SELECT * FROM phones"))
    for phone in response:
      returnStr += f"""
        <p>
          <strong>Phone</strong>: { phone.model } <br />
          The owner of this phone is: { phone.owner }, and sells the phone at the price of { phone.price } dollars! <br />
          This phone brand is { phone.brand } and weight { phone.weight }g at maximum.<br />
          { phone.owner } had given this comment { phone.model}: <em>{ phone.comment }</em>
        </p>
        """
  
  # return returnStr

# @app.get("/question2")
# def phones():
#   returnStr2 = ""

#   with db.begin() as conn:
#     response = conn.execute(text("Select * from phones where OWNER = stacey"))



