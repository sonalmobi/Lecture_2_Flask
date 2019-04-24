from flask import Flask, render_template

ap = Flask(__name__)

@ap.route("/")
def sonal():
    return "Hello, world!"


@ap.route("/swap")
def swap():
    return "Hello, swap!"

@ap.route("/<string:naw>")
def namaskar(naw):
    naw = naw.capitalize()
    return f"<li>namaskar, {naw}. \n Baray Ka!</li>"

@ap.route("/home")
def home():
    return render_template("My_Blog_With_Css.html")

@ap.route("/variable1")
def variable1():
    swapnil="I love you Sona"
    return render_template("variable.html",x=swapnil)

@ap.route("/variable2")
def variable2():
    swapnil="I love you Sopu"
    return render_template("variable.html",x=swapnil)

@ap.route("/forloop")
def myloop():
    myloop=["sona","sopu","vicky","dhanya"]
    return render_template("forloop.html",x=myloop)

@ap.route("/pn")
def mypune():
    return render_template("pune.html")

@ap.route("/nn")
def mynandurbar():
    return render_template("nandurbar.html")
