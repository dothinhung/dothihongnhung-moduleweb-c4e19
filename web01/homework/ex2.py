from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def index(username):
    users = {
        "quan":{
            "name": "Nguyen Anh Quan",
            "age": 22
        },
        "tuananh":{
            "name": "Huynh Tuan Anh",
            "age": 23
        },
        "nhung":{
            "name": "Do Thi Hong Nhung",
            "age": 21
        },
        "huyen":{
            "name": "Hoang Thanh Huyen",
            "age": 20
        }
    }
    
    if username in users:
        return "My name is {0}, I'm {1} years old".format(users[username]["name"], users[username]["age"])
    else:
        return("User not found")

if __name__ == '__main__':
  app.run(debug=True)
 