# content management system
# database (video - link,title, views, thumbnail, yuotube_id)
# admin page, trand chu, 

from flask import *
import mlab
from models.video import Video
from models.login import Login
from youtube_dl import YoutubeDL

app = Flask(__name__)
# dùng trong session, để dùng được session thì phả truyền cho n 1 secret key
# có thể dùng để chứa thông tin mang đi mang lại nhiều vì session là đường ngầm giữa client & server
app.secret_key = 'a super secret key'

mlab.connect()


@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos=videos)


# create admin page to add video to collection into mlab
# use youtube_dl (lab02) to extract information of video
@app.route('/admin', methods=["GET", "POST"])
def admin():
    if 'logged in' in session:
        if request.method == "GET":
            videos = Video.objects()
            return render_template('admin.html', videos=videos)
        elif request.method == "POST":
            form = request.form
            link = form['link']
            
            ydl = YoutubeDL()
            data = ydl.extract_info(link, download=False)
            # download=False ==> not download video 

            title = data['title']
            thumbnail = data['thumbnail']
            views = data['view_count']
            youtube_id = data['id']

            new_video = Video(
                title=title,
                link=link,
                thumbnail=thumbnail,
                views=views,
                youtube_id=youtube_id
            )
            new_video.save()
            return redirect(url_for('admin'))
    else:
        return "Đăng nhập sai"

# route detail giúp người dùng xem chi tiết video khi mà người dùng click vào view
# trong trương hợp chưa để link ở ảnh
# (vì nếu để link ở ảnh thì chỉ cần click vào ảnh là có thể xem)
@app.route('/detail/<youtube_id>')
def detail(youtube_id):
    return render_template('detail.html', youtube_id=youtube_id)

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']


        # có thể lấy username và password ở database
        user = Login.objects(username=username,
                            password=password
                            )

        if username == username and password == password:
            session['logged in'] = True
            return redirect(url_for('admin'))
        else:
            return "Wrong username or password"

@app.route('/logout')
def logout():
    del session['logged in']
    return redirect(url_for('index'))

if __name__ == '__main__':
  app.run(debug=True)
 