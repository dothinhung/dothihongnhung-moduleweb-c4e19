from flask import Flask, render_template
app = Flask(__name__)


@app.route('/about-me')
def profile():
    posts = {
        "name" : "Do Thi Hong Nhung",
        "work": "Student",
        "school": "Hanoi University",
    }

    return render_template('inform_yourself.html', posts= posts)

if __name__ == '__main__':
  app.run(debug=True)
 