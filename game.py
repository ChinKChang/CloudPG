from flask import Flask, request, render_template
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def rps():
    if request.method == "POST":
        user_choice = request.form["choice"]
        options = ["rock", "paper", "scissors"]
        ai_choice = random.choice(options)

        if user_choice == ai_choice:
            result = "It's a tie!"
        elif (
            (user_choice == "rock" and ai_choice == "scissors") or
            (user_choice == "paper" and ai_choice == "rock") or
            (user_choice == "scissors" and ai_choice == "paper")
        ):
            result = "You win!"
        else:
            result = "You lose!"

        return render_template("index.html", result=result, user=user_choice, ai=ai_choice)

    return render_template("index.html")