from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import session

import sqlite3


app=Flask(__name__)

app.secret_key="smart_health"


def init_db():

    con=sqlite3.connect(
        "database.db"
    )

    cur=con.cursor()

    cur.execute("""

    CREATE TABLE IF NOT EXISTS users(

    id INTEGER PRIMARY KEY,

    email TEXT,

    phone TEXT,

    password TEXT

    )

    """)

    con.commit()

    con.close()


init_db()


@app.route("/")

def login():

    return render_template(
        "login.html"
    )


@app.route(
"/register",
methods=["POST"]
)

def register():

    email=request.form["email"]

    phone=request.form["phone"]

    password=request.form["password"]

    con=sqlite3.connect(
        "database.db"
    )

    cur=con.cursor()

    cur.execute(

    """

    INSERT INTO users

    (
    email,
    phone,
    password

    )

    VALUES

    (?,?,?)

    """,

    (
    email,
    phone,
    password
    )

    )

    con.commit()

    con.close()

    return render_template(

    "login.html",

    success=

    "Registration Successful"

    )


@app.route(
"/login",
methods=["POST"]
)

def authenticate():

    email=request.form["email"]

    password=request.form["password"]

    con=sqlite3.connect(
        "database.db"
    )

    cur=con.cursor()

    cur.execute(

    """

    SELECT *

    FROM users

    WHERE

    email=?

    AND

    password=?

    """,

    (
    email,
    password
    )

    )

    user=cur.fetchone()

    con.close()

    if user:

        session["user"]=email

        return redirect(
            "/dashboard"
        )

    return render_template(

    "login.html",

    error=

    "Invalid Credentials"

    )


@app.route(
"/dashboard"
)

def dashboard():

    if "user" not in session:

        return redirect("/")

    return render_template(
        "dashboard.html"
    )


@app.route("/logout")

def logout():

    session.clear()

    return redirect("/")


import os

if __name__ == "__main__":

    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=False
    )