# with render_template
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/bmi/<float:weight>/<float:height>')
def bmi(weight, height):
    height = height / 100
    bmi = weight / (height ** 2)

    return render_template(
        'bmi.html',
        bmi = bmi,
        )

if __name__ == '__main__':
  app.run(debug=True)
 