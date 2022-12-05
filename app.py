import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from datetime import datetime
from datetime import date

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///word-tracker.db")

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

        db.execute("INSERT INTO words (word,months) VALUES (?,?)", word, months)

        return redirect("/")

    else:

        #Query for all words
        words = db.execute("SELECT * FROM words ORDER BY months DESC")
        total = db.execute("SELECT COUNT(word) FROM words")
        total = total[0]['COUNT(word)']
        return render_template("index.html", words=words, total=total, age=age, name=name)


