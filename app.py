import datetime
from flask import Flask, render_template, request

app = Flask(__name__)
habits = ["Walk the dog", "Walk with the dog"]

@app.context_processor
def add_call_date_range():
    def date_range(start: datetime.date):
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3, 4)]
        return dates

    return {"date_range": date_range}


@app.route("/")
def index():
    date_str = request.args.get("date")
    if date_str:
        selected_date = datetime.date.fromisoformat(date_str)
    else:
        selected_date = datetime.date.today()
    return render_template(
        "index.html",
        habits=habits,
        title="Habit Traker - Home",
        selected_date=selected_date,
    )


@app.route("/add", methods=["GET", "POST"])
def add_habit():
    if request.method == "POST":
        habits.append(request.form.get("habit"))
    return render_template(
        "add_habit.html",
        title="Habit Traker - Add Habit",
        selected_date=datetime.date.today()
    )


if __name__ == '__main__':
    app.run(port=5003)
