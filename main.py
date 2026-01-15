from flask import Flask, render_template
from db import getTaskList
app = Flask(__name__)
tasklist = [["Walk Dog",True],["Wash Dishes",False]]
#askList = getTaskList
@app.route("/")
def home():     
    return render_template("tasklist.html",TaskList = tasklist) # r_t -->to read html file and then to load data from python, to run on browser
                                                                # 
app.run()