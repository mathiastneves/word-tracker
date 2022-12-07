import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from datetime import datetime
from datetime import date

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Connect with database
con = sqlite3.connect("word-tracker.db", check_same_thread=False)
db = con.cursor()

#SET DOB
dob = '2020-05-12'
today = date.today()
new_dob = datetime.strptime(dob, '%Y-%m-%d').date()
age = (today.year - new_dob.year) * 12 + (today.month - new_dob.month)

#SET NAME
name = 'David'


@app.route("/", methods=["GET", "POST"])
def index():


    if request.method == "POST":

        word = request.form.get("word")
        date = request.form.get("months")

        new_date = datetime.strptime(date, '%Y-%m-%d').date()
        months = (new_date.year - new_dob.year) * 12 + (new_date.month - new_dob.month)

        #Using placeholders help avoid SQL injection attacks
        data = [(word, months)]

        db.executemany("INSERT INTO words (word,months) VALUES (?,?)", data)
        con.commit()

        return redirect("/")

    else:

        #Query for all words
        db.execute("SELECT * FROM words ORDER BY months DESC")
        words = db.fetchall()
        
        total = db.execute("SELECT COUNT(word) FROM words")
        total = total.fetchall()[0][0]
        return render_template("index.html", words=words, total=total, age=age, name=name)


