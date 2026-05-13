from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    user_choice = request.form.get("choice")
    computer_choice = random.choice(["rock", "paper", "scissors"])

    if user_choice == computer_choice:
        result = "Tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "You win!"
    else:
        result = "Computer wins!"

    return render_template(
        "result.html",
        user=user_choice,
        computer=computer_choice,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)