from flask import Blueprint,render_template,request
from dotenv import load_dotenv
import os

main = Blueprint("main",__name__)
load_dotenv()
for_test = os.getenv("EXAMPLE_SECRET")

@main.route("/")
def home ():
    return render_template("index.html",for_test=for_test,requ=request.headers)


import time

@main.route("/slow")
def slow ():
    time.sleep(20)
    return "done"
