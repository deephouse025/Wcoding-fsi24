from flask import Flask, request
import sqlalchemy
from sqlalchemy.sql import text
import datetime

app = Flask(__name__)

db = sqlalchemy.create_engine(
	"mariadb+pymysql://root:@localhost:3306/In-Class",
	echo=True
	)


@app.post("/bloginputs")
def stuff():
    title_key = request.json.get("title", "")
    tag_key = request.json.get("tag", "")
    author_key = request.json.get("author", "")
    content_key = request.json.get("content", "")
    

    print("ONTWO:", title_key.value)
    return "DONE"

# example changes made !

# inserting new blog post
# using variables to insert entry into db
# @app.post("/submit")
# def submitEntry():
#     with db.begin() as conn:
#         if request.form.get("activity_action") == "writearticle":
#             res = conn.execute(text("""
#                 INSERT INTO articles (title, tag, author, content, created_at)
#                 VALUES (:title, :tag, :author, :content, :created_at)
#                 """),
#                         {
#                             'title': request.form.get("title"),
#                             'tag': request.form.get("tag"),
#                             'author': request.form.get("author"),
#                             'content': request.form.get("content"),
#                             'created_at': datetime.datetime.now()
#                         }
#             )


# if __name__ == "__main__":
#     app.run(debug=True)
        # returnStr += f'<h3>Inserted: {res.rowcount}</h3>'

# @app.get("/blog")
# def getEntry():
#   returnStr = ""
  
#   with db.begin() as conn:
#     response = conn.execute(text("SELECT * FROM blogTable ORDERED BY created_at DESC LIMIT 1;"))
#     for phone in response:
#       returnStr += f"""
#         <p>
#           <strong>Phone</strong>: { phone.model } <br />
#           The owner of this phone is: { phone.owner }, and sells the phone at the price of { phone.price } dollars! <br />
#           This phone brand is { phone.brand } and weight { phone.weight }g at maximum.<br />
#           { phone.owner } had given this comment { phone.model}: <em>{ phone.comment }</em>
#         </p>
#         """
  
#   return returnStr