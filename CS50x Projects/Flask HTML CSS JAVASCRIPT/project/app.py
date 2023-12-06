import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, make_response , request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

import csv
from io import StringIO
from helpers import apology, login_required, lookup, usd


# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///manage.db")



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response





@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/home")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")






@app.route("/register", methods=["GET", "POST"])
def register():
     # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure username was submitted
        if not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("pwd is not equal to check", 400)


        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 0 :
            return apology("username already used", 400)

        # I WANT to add pwdhash and username inSQL
        db.execute("INSERT INTO users (username , hash) VALUES (?,?)", request.form.get("username") , generate_password_hash(request.form.get("password")))

        # I'm going to call the rows that I have already submit via SQL in order to save the id after
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/home",methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        redirect("/")
    else:
        return render_template("homepage.html")

@app.route("/upload",methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # I'm going to safe the input in variables
        barcode = request.form.get("barcode")
        materials = request.form.get("materials")
        quantities = request.form.get("quantities")
        price = request.form.get("price")
        upload = request.form.get("action")

        #Checking possible errors
        # EMPTY
        if not barcode or not materials or not quantities or not price or not upload:
            return apology("fill in all upload fields", 400)
        #BARCODE
        if len(barcode) != 8 or not barcode.isdigit():
            return apology("barcode must have 8 numeric digit", 400)
        #Quantites has to be integer
        if not quantities or not quantities.isdigit() or int(quantities) < 0:
            return("Quantities should be => 0 , integer and positive and not a fraction", 400)
        if float(price) <= 0:
            return("Price must be > 0 and != 0", 400)

        # I wanto charge this values in SQL database
        tot_value = float(price) * int(quantities)*1.0
        db.execute ("INSERT INTO data1 (user_id, barcode, materials, quantities , price ,tot_value) VALUES(:user_id, :barcode, :materials, :quantities , :price ,:tot_value)", user_id = session["user_id"], barcode = barcode , materials = materials, quantities = quantities , price = price, tot_value = tot_value)
        flash(f"Coorect update bar code= {barcode} , materials = {materials}, quantities= {quantities}, price = {price}")
        return redirect("/home")


    else:
        return render_template("upload.html")

@app.route("/allocation", methods=["GET", "POST"])
def allocation():
    # I want save variables of input for every canstruction sytes
    if request.method == "POST":
        barcode = request.form.get("barcode")
        materials = db.execute("SELECT materials FROM (SELECT barcode, materials, SUM(quantities) as total_quantities, AVG(price) as average_price, SUM(tot_value) as TOTAL_value , MAX(time_of_buy) as latest_time_of_buy FROM data1 GROUP BY barcode ORDER BY latest_time_of_buy DESC) AS subquery WHERE barcode =:barcode  ;" , barcode = barcode)[0]["materials"]
        quantities_string = request.form.get("quantities")
        #This I want to convert a string into an integer
        quantities = int(quantities_string)
        # i WANT TO SEARCH THE AVARAGE_PRICE OF BOUGHT
        avarage_value = db.execute("SELECT average_price FROM (SELECT barcode, materials, SUM(quantities) as total_quantities, AVG(price) as average_price, SUM(tot_value) as TOTAL_value , MAX(time_of_buy) as latest_time_of_buy FROM data1 GROUP BY barcode ORDER BY latest_time_of_buy DESC) AS subquery WHERE barcode =:barcode  ;" , barcode = barcode)[0]["average_price"]
        #I want to update new quantities because when I put quantities in a sites, I have to subtract from database of central company
        quantities_of_database_string = db.execute("SELECT total_quantities FROM (SELECT barcode, materials, SUM(quantities) as total_quantities, AVG(price) as average_price, SUM(tot_value) as TOTAL_value , MAX(time_of_buy) as latest_time_of_buy FROM data1 GROUP BY barcode ORDER BY latest_time_of_buy DESC) AS subquery WHERE barcode =:barcode ;" , barcode = barcode)[0]["total_quantities"]
        quantities_of_database = int(quantities_of_database_string)
        # I WANT to calculate a possiblePrice of "sell" that is markup * avarage_value
        mark_up = request.form.get("markup")
        cantiere = request.form.get("cantiere")

        #Checking possible errors
        # EMPTY
        if not barcode or not materials or not quantities or not mark_up or not cantiere:
            return apology("fill in all allocation fields", 400)
        #BARCODE
        if len(barcode) != 8 or not barcode.isdigit():
            return apology("barcode must have 8 numeric digit", 400)
        #Quantites has to be integer
        if not quantities or int(quantities) < 0:
            return("Quantities should be => 0 , integer and positive and not a fraction", 400)
        if float(mark_up) < 0:
            return("Mark_up must be > 0 or =", 400)
        if quantities_of_database < quantities:
            return("Quantities sent to construction sites can not be > then all quantities of company", 400)



        # I'm going to calculate the price_of_sell
        price_sell = float(avarage_value) * (float(mark_up)+1) * 1.0
        # Tot value
        tot_value_cantiere = float(avarage_value) * quantities * 1

        # I want to insert in a new SQL table call cantieri these date
        db.execute ("INSERT INTO cantieri (user_id , barcode, materials , quantities , price_to_sell,tot_value ,cantiere) VALUES (:user_id , :barcode ,:materials , :quantities , :price_sell ,:tot_value_cantiere ,:cantiere);",user_id = session["user_id"], barcode = barcode, materials = materials , quantities = quantities , price_sell = price_sell, tot_value_cantiere = tot_value_cantiere ,cantiere = cantiere )
        # I have to update quantities in main company
        quantities_update = int(quantities_of_database) - int(quantities)
        # I have to update the quantities of materials in central database of company
        db.execute("UPDATE data1 SET quantities =:quantities_update WHERE barcode =:barcode ;  ", quantities_update = quantities_update , barcode = barcode)
        flash(f"Coorect allocation at construction site of {cantiere}. INFO bar code= {barcode} , materials = {materials}, quantities= {quantities}, price = {price_sell}$ , tot_value ={tot_value_cantiere}$")
        return redirect("/home")
    else:
        return render_template("allocation.html")

@app.route("/balance")
def balance():
    dati_split = db.execute("SELECT * FROM  cantieri JOIN users ON users.id = cantieri.user_id ORDER BY cantiere DESC;")
    return render_template("balance.html", dati_split = dati_split)


# I'm going to sum the uplode stocks in company, calcultate total_value and avarage peices from supplyers
@app.route("/")
def database():
    dati = db.execute("SELECT barcode, materials, SUM(quantities) as total_quantities, AVG(price) as average_price, SUM(tot_value) as TOTAL_value ,MAX(time_of_buy) as latest_time_of_buy FROM data1 GROUP BY barcode ORDER BY latest_time_of_buy DESC;")
    return render_template("database.html", dati = dati)

@app.route("/history", methods=["GET", "POST"])
def history():
        # I want to save SQL in a variables of dictionary
        transactions =db.execute("SELECT * FROM data1 JOIN users ON users.id = data1.user_id;" )
        return render_template("history.html", transactions = transactions)

#That is a function that allow users to download file of database as a csv
@app.route("/download_csv")
def download_csv():
    query = "SELECT barcode, materials, SUM(quantities) as total_quantities, AVG(price) as average_price, SUM(tot_value) as TOTAL_value ,MAX(time_of_buy) as latest_time_of_buy FROM data1 GROUP BY barcode ORDER BY latest_time_of_buy DESC;"
    csv_database = query_to_csv(query)

    response = make_response(csv_database)
    response.headers["Content-Disposition"] = "attachment; filename=database.csv"
    response.headers["Content-type"] = "text/csv"

    return response

# I'm define the funcrion to compleate download
def query_to_csv(query):

    # Usa db.execute per ottenere i dati dalla query
    rows = db.execute(query)

    # I want to create a variable in wich storage the SQL data as strin of input
    csv_buffer = StringIO()

    #I want to storage the write string data from SQL in csv_writer variables via csv_buffer space of stock data
    csv_writer = csv.writer(csv_buffer)

    #I'm going to write the first row of intestation using the methon .keys to have the intestation
    csv_writer.writerow(rows[0].keys())

    #I want to write every row in csv and so
    for row in rows:
        csv_writer.writerow(row.values())

    # I'm going to convert csv fileI/0 in string, befor i
    csv_data = csv_buffer.getvalue()

    return csv_data
















##DOWLOAD CSV ##


@app.route("/download_csv_split")
def download_csv_split():
    query = "SELECT * FROM  cantieri JOIN users ON users.id = cantieri.user_id ORDER BY cantiere DESC;"
    csv_database = query_to_csv(query)

    response = make_response(csv_database)
    response.headers["Content-Disposition"] = "attachment; filename=split.csv"
    response.headers["Content-type"] = "text/csv"

    return response






 #dati = db.execute("SELECT barcode, materials, SUM(quantities) as total_quantities, AVG(price) as average_price, SUM(tot_value) as total_value, MAX(time_of_buy) as latest_time_of_buy FROM data1 GROUP BY barcode, materials ORDER BY latest_time_of_buy DESC;")
#SELECT barcode, materials, SUM(quantities) as total_quantities, AVG(price) as average_price, SUM(tot_value) as TOTAL_value ,MAX(time_of_buy) as latest_time_of_buy FROM data1 GROUP BY barcode ORDER BY latest_time_of_buy DESC;")

# @app.route("/")
#def database():
#    dati = db.execute("SELECT * FROM data1 ORDER by time_of_buy DESC;")
#    return render_template("database.html", dati = dati)

#pagina HTML di history
