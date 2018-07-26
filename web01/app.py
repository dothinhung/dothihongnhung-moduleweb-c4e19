from flask import Flask, render_template
# tạo ra 1 server or 1 app
app = Flask(__name__)


@app.route('/')
def index():
    posts = [ 
        {
        "title": "Thơ Con Cóc",
        "content": "Hôm nay trăng lên cáo quá  Anh muốn hôm em vào má",
        "author": "Tuấn Anh",
        "gender": 1
        },

        {
        "title": "Thơ xàm",
        "content": "Ngồi buồn cắn ngón tay chơi .....",
        "author": "Liên",
        "gender": 0
        },

        {
        "title": "Vội Vàng",
        "content": "Tôi muốn tắt nắng đi cho màu đừng nhạt mất  Tôi muốn buộc gió lại cho hương đừng bay đi",
        "author": "Xuân Diệu",
        "gender": 0
        }

    ]
    
    return render_template(
        "index.html", 
        posts = posts
        )

# khi vào route chạy function ngay dưới 

@app.route('/hello')
def hello():
    return "Hello C4E19"

# request parameter /// name is a parameter
# route has parameter ==> def has argument the same name with parameter and inside < >
@app.route('/say-hi/<name>/<age>')
def hi(name, age):
    return "Hi {0} you're {1} years old".format(name, age)

@app.route('/sum/<int:x>/<int:y>')
def calc(x, y):
    # return "{0} + {1} = {2}".format(x, y, int(x) + int(y))
    return str(x+y)


if __name__ == '__main__':
  app.run(debug=True)
#   debug = True là cập nhập code mới 
 