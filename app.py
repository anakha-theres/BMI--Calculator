from flask import Flask, render_template, request

app = Flask(__name__)

# Function to calculate BMI and category
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return round(bmi, 2), category

@app.route("/", methods=["GET", "POST"])
def index():
    bmi = None
    category = None
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            bmi, category = calculate_bmi(weight, height)
        except ValueError:
            bmi = "Invalid input"
            category = ""
    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(debug=True)
