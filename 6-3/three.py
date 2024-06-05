
from flask import Flask, request
import sqlalchemy
from sqlalchemy.sql import text

app = Flask(__name__)

db = sqlalchemy.create_engine("mariadb+pymysql://root:@127.0.0.1:3306/In-Class")

@app.get("/three")
# def q1():
#   with db.begin() as conn:
#     returnStr = ""
#     response = conn.execute(text("SELECT upper(brand) as brand, lower(model) as model FROM phones"))
#     for phone in response:
#       returnStr += f"""
#         <tr>
#           <td>{ phone.brand }</td>
#           <td>{ phone.model }</td>
#         </tr>
#         """
#     return f"""
# <table border=1>
# <tr>
#     <td>Brand</td>
#     <td>Model</td>
# </tr>
# """ + returnStr + "</table>"

@app.get("/three")  
def q2():
    with db.begin() as conn:
        returnStr = ""
        response = conn.execute(text("SELECT CONCAT(owner, '---', '(', model, ')', price) as PhoneList FROM phones"))
        
        for phone in response: 
            returnStr += f"""
            <tr>
            <td>{phone.PhoneList}</td>
            </tr>
            """
        return f"""
            <table border=1>
            {returnStr}
            </table>
        """
            
            

def q3():
    with db.begin() as conn:
        returnStr = ""
        
        # q3
        # response = conn.execute(text("SELECT model, length(comment) as comment as FROM phones"))
        # for row in response: 
        #     returnStr += (row.model + "\t" + row.comment)
           
           
        #q4 
        response = conn.execute(text("select average(weight) from phones where owner='Brad'"))
        
        return results