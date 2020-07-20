# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask, render_template, request
from datetime import datetime
from similar_text import similar_text
import jeopardy
import os

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", time = datetime.now())

@app.route("/question", methods = ["GET", "POST"])
def question():
    if request.method == "POST":
        random_question = jeopardy.return_random_question()
        return render_template("question.html", random_question = random_question)
    else:
        return "Error"

@app.route("/answer", methods = ["GET","POST"])
def answer():
    if request.method == "POST":
        score = 0
        user_input = request.form["user_input"]
        answer = jeopardy.return_answer()
        if user_input.lower() == answer.lower():
            #score += value
            results_text = "Congrats!! you are correct!" #Your score is " + str(score)
        # elif 100> (similar_text(user_input.lower(),answer.lower())) >75:
        #     second_chance = input("Nope! you're close would you like a hint: yes or no: ")
        #     if second_chance.lower() == "yes":
        #         print(hint)
        #         second_response = input("What is your final guess: " )
        #         if second_response.lower() == answer.lower():
        #             #score += value
        #             results_text = "WOOHOO you got it! your score is " + str(score)
        #         else: 
        #             #score -= value
        #             results_text = "Sorry even with a hint you're still incorrect! The correct answer is: " + answer + "your score is " + str(score)
        #     else:
        #         #score -= value
        #         results_text = "ok suit yourself, the correct answer is: " + answer + "your score is " + str(score)
        else:
            #score -= value
            results_text = "That's inncorrect!- the answer is " + answer #+ " and your score is " + str(score)
        return render_template("answer.html", results_text = results_text)
    else:
        return "Error"