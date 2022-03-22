from glob import escape
from sqlite3 import Cursor
from flask import Flask, request, url_for, request, render_template, redirect
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="root",
  database="python"
)

cursor = db.cursor(dictionary=True)

app=Flask(__name__)

@app.route('/')
def Home():         
    sql = "SELECT * FROM posts " \
          "INNER JOIN users ON users.user_id = posts.post_user_id " \
          "INNER JOIN categories ON categories.category_id = posts.post_category_id " \
          "ORDER BY post_id DESC"
    cursor.execute(sql)
    posts = cursor.fetchall()
    return render_template('index.html', posts=posts)


@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)
    return 'current user %5' % escape(username)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('not-found.html'), 404

@app.route('/Hakkımda')
def Hakkımda():
    return render_template('Hakkımda.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/post/<url>')
def post(url):
    sql = "SELECT * FROM posts " \
          "INNER JOIN users ON users.user_id = posts.post_user_id " \
          "INNER JOIN categories ON categories.category_id = posts.post_category_id " \
          "WHERE post_url = %s"
    cursor.execute(sql, (url,))
    post = cursor.fetchone()
    if post:
        return render_template('post.html', post=post)
    else:
        return redirect(url_for('Home'))


if __name__=='__main__':
    app.run(debug=True)


