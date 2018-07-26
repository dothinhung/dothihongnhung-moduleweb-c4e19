import os
from flask import Flask, redirect
app = Flask(__name__)

@app.route('/school')
def hello():
    return redirect("http://techkids.vn")

if __name__ == '__main__':
    app.run(debug=True)