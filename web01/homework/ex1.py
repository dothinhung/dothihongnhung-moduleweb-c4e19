from flask import Flask
app = Flask(__name__)


@app.route('/bmi/<float:weight>/<float:height>')
def bmi(weight, height):
    height = height / 100
    bmi = weight / (height ** 2)
    
    if bmi < 16:
        return "Your BMI is {0} ==> Severely underweight".format(bmi)
    elif 16 <= bmi <= 18.5:
        return "Your BMI is {0} ==> Underweight".format(bmi)
    elif 18.5 <= bmi < 25:
        return "Your BMI is {0} ==> Normal".format(bmi)
    elif 25 <= bmi < 30:
        return "Your BMI is {0} ==> Overweight".format(bmi)
    elif bmi > 30:
        return "Your BMI is {0} ==> Obese".format(bmi)

if __name__ == '__main__':
  app.run(debug=True)
 