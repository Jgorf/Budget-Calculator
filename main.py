from flask import Flask, render_template, request
from model import taxes

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")


@app.route('/index', methods=["POST"])
def goBack():
    return render_template("index.html")


@app.route('/update', methods=["POST"])
def update():
    myForm = request.form
    income = float(myForm["income"])
    state = myForm['state']
    needs = float(myForm['housing']) + float(myForm['utilities']) + float(
        myForm["groceries"]) + float(myForm["transportation"]) + float(
            myForm["healthcare"])
    wants = float(myForm["entertainment"]) + float(myForm["dining"]) + float(
        myForm["hobbies"]) + float(myForm["personal"])
    savings = float(myForm["emergency"]) + float(myForm["retirement"]) + float(
        myForm["vacation"])

    socialSec = income * 0.062
    federalTax = 0

    if income >= 0 and income <= 11000:
        federalTax = income * .10
    elif income >= 11001 and income <= 44725:
        federalTax = income * .12
    elif income >= 44726 and income <= 95375:
        federalTax = income * .22
    elif income >= 95376 and income <= 182100:
        federalTax = income * .24
    elif income >= 182101 and income <= 231250:
        federalTax = income * .32
    elif income >= 231251 and income <= 578125:
        federalTax = income * .35
    elif income >= 578126:
        federalTax = income * .37

    state_tax = taxes[state] * income

    print(socialSec)
    print(federalTax)
    print(state_tax)
    
    taxed_amnt = socialSec + federalTax + state_tax

    taxedIncome = income - (taxed_amnt)
    remaining = taxedIncome - (needs + wants + savings)

    # Calculating percentages and rounding for display purposes
    needs_percentage = round((needs / taxedIncome) * 100, 2)
    wants_percentage = round((wants / taxedIncome) * 100, 2)
    savings_percentage = round((savings / taxedIncome) * 100, 2)

    results = {
        "remaining": round(remaining, 2),  # Rounding remaining amount
        "taxedIncome": round(taxedIncome, 2),  # Rounding taxed income
        "needs": needs,
        "wants": wants,
        "savings": savings,
        "needAdvice": "",
        "wantAdvice": "",
        "savingAdvice": ""
    }

    if needs_percentage > 50:
        results[
            'needAdvice'] = "Your needs section is over 50% of your income. Consider reducing your spending on needs."
    elif needs_percentage == 50:
        results[
            'needAdvice'] = "Your needs section is exactly 50% of your income. Good job!"
    else:
        results[
            'needAdvice'] = "Your needs section is below 50% of your income. You might allocate more to your needs."

    if wants_percentage > 30:
        results[
            'wantAdvice'] = "Your wants section is over 30% of your income. Consider reducing your spending on wants."
    elif wants_percentage == 30:
        results[
            'wantAdvice'] = "Your wants section is 30% of your income. Well done!"
    else:
        results[
            'wantAdvice'] = "Your wants section is below 30% of your income. You might allocate more to your wants."

    if savings_percentage > 20:
        results[
            'savingAdvice'] = "Your savings section is over 20% of your income. You are saving well!"
    elif savings_percentage == 20:
        results[
            'savingAdvice'] = "Your savings section is 20% of your income. Good job!"
    else:
        results[
            'savingAdvice'] = "Your savings section is below 20% of your income. Consider saving more."

    return render_template('update.html', results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
