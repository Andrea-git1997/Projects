import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

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
db = SQL("sqlite:///finance.db")



@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    #GET USERS STOCK
    stocks = db.execute("SELECT symbol, SUM(shares) as total_shares FROM buy WHERE user_id = :user_id GROUP BY symbol HAVING total_shares > 0", user_id = session["user_id"] )
    #GET USERS CASH
    cash = db.execute("SELECT cash FROM users WHERE id = :user_id", user_id = session["user_id"])[0]["cash"]
    #INITIALIZE VARIABLES FOR TOTAL VALUES
    total_value = cash
    grand_tot = cash
    #ITERATE OVER STOCKS AND ADD PRICE TOTAl VALUE
    for stock in stocks:
        # via quote symbol I'm going to receive the quote of stocks,as I done in def quote
        # I'm going to create a dictionary
        quote = lookup(stock["symbol"])
        #After that I'm going to store into variables dictionary the quote dictionary valueas, the update YAOHH finance infromation
        #Es if value of stocks change, i WILL HAVE that and * shares I will have my total values
        stock["name"]= quote["name"]
        stock["price"]= quote["price"]
        stock["value"]= stock["price"]  * stock["total_shares"]
        total_value += stock["value"]
        grand_tot += stock["value"]

    return render_template ("index.html" , stocks = stocks , cash = cash, total_value = total_value , grand_tot = grand_tot )




@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    # I'm going to save in variables the input of html and I'm going to indicate the errors
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        if not symbol:
            return("You have to put a stock symbol es TSLA" , 400)
        elif not shares  or not shares.isdigit() or int(shares) <= 0:
            return("Shares should be => 0 , integer and positive and not a fraction", 400)
        # I have to find the way to have the acces to quote via symbol to find price via look up
        quote = lookup(symbol)
        if not quote:
            return ("Symbol not fund, be sure to digit Yahhooo Finance symbol es TSLA", 400)
        # I want to define price that in the list of dictionary
        price = quote["price"]
        #I want to calculate total costs that is, I want that shares is an integer
        tot_cost = price *int(shares)
        #In SQL every users have differents ammount of cash via id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = :user_id ",  user_id = session["user_id"])[0]["cash"]
        # If cash is less then tot_cost
        if cash < int(tot_cost):
            return(f"You don't have enought cash . Cost={tot_cost}$  Cash={cash}$ " , 400)
        # I'm going to calculate new cash
        db.execute("UPDATE users SET cash = cash - :tot_cost WHERE id = :user_id  ", tot_cost = tot_cost , user_id = session["user_id"])
        # i want to save the update in my new SQL buy
        db.execute("INSERT INTO buy (user_id ,symbol ,shares,price ) VALUES (:user_id ,:symbol,:shares,:price)", user_id = session["user_id"] , symbol = symbol , shares = shares , price = price)
        flash(f"Bought {symbol} in shares of {shares} for a total cost of {usd(tot_cost)}. Search other")
        return redirect("/")

    else:
        return render_template ("buy.html")
    """Buy shares of stock"""




@app.route("/history")
@login_required
# i want to save all buy SQL inside a variable that is buy too
def history():
    buys = db.execute("SELECT * FROM buy WHERE user_id = :user_id ORDER BY time_of_buy DESC", user_id = session["user_id"])

    return render_template("history.html", buys= buys)



    """Show history of transactions"""
    return apology("TODO")


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
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")



@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")





@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    if request.method == "POST":
        """Get stock quote."""
        # I want to define the variable quote
        symbol = request.form.get("symbol")
        # I'm going to calculate quote from the simbol in input bar
        quote = lookup(symbol)
        #If ther's no quote
        if not quote:
            return apology("ther's no quote for this digit, please try another", 400)
            # When someone digit, I want that program start to show quote results
        return render_template("quote.html", quote = quote)
    else:
        return render_template("quote.html")



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
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")








@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        # I'm going to storage into variables symbol that I want sell
        symbol_sell = request.form.get("symbol")
        # I'm going to storage how many shares i want to sell
        shares_sell = request.form.get("shares")


        # errors handle
        if not symbol_sell or not shares_sell:
            return apology("You have to complete both folder")
        # Storage into a variable symbol and shares_sell
        time_of_buy = db.execute("SELECT time_of_buy  FROM buy WHERE symbol =:symbol_sell AND user_id = :user_id ", symbol_sell = symbol_sell , user_id = session["user_id"])
        # If ther's not coicidence with id_sellers to the actual one or is null ERROR
        if not time_of_buy:
            return apology(f"You don't have this {symbol_sell} stock in portfolio")
        # I'm going to save in a variable the numbers of shares
       # I'm going to save in a variable the total number of shares
        shares_portfolio = db.execute("SELECT SUM(shares) as total_sell FROM buy WHERE symbol = :symbol_sell AND user_id = :user_id", symbol_sell=symbol_sell, user_id=session["user_id"])
        actual_shares = shares_portfolio[0]["total_sell"] if shares_portfolio else 0

        # Check the quantityy to handle the sell
        if actual_shares < int(shares_sell):
            return apology(f"You don't have enough shares : actual shares {actual_shares } for symbol{symbol_sell}")

        # When sell actions go okay Update cash
        quote = lookup(symbol_sell)
        price_sell = quote["price"]
        #HANDLE NEW CASH UPDATE
        db.execute("UPDATE users SET cash = cash + (:price_sell * :shares_sell)  WHERE id = :user_id " , price_sell = price_sell , shares_sell = shares_sell , user_id = session["user_id"])
        #HANDLE DIMINUITIO OF SHARES
        # HANDLE DIMINUTION OF SHARES
        db.execute("UPDATE buy SET shares = shares - :shares_sell WHERE user_id = :user_id AND symbol = :symbol_sell", shares_sell=int(shares_sell), user_id=session["user_id"], symbol_sell=symbol_sell)
        flash(f"Sold {symbol_sell} in shares of {shares_sell}")
        return redirect("/")



    else:
        return render_template("sell.html")




    return apology("TODO")
