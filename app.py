from flask import Flask, render_template, request

app = Flask(__name__)
habits = ["Walk the dog", "Walk with the dog"]

@app.route("/")
def index():
    return render_template("index.html", habits=habits, title="Habit Traker - Home")


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habits.append(request.form.get("habit"))
    return render_template("add_habit.html", title="Habit Traker - Add Habit")


if __name__ == '__main__':
    app.run(port=8080)