from flask import *
import mlab
from models.service import Service
from models.user import User
from models.order import Order
from models.admin import Admin
import datetime
from gmail import GMail, Message


app = Flask(__name__)

app.secret_key = 'a super secret key'

mlab.connect()


@app.route('/')
def index():
    return render_template('index.html')

##########################
@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender=gender)
    return render_template('search.html', all_service=all_service)

#########################
@app.route('/search')
def another_search():
    all_service = Service.objects()
    return render_template('search.html', all_service = all_service)
        

#########################
@app.route('/admin')
def admin():
    if 'admin' in session:
        all_service = Service.objects()
        return render_template('/admin.html', all_service=all_service)
    else:
        return redirect(url_for('admin_login'))

########################
@app.route('/admin-login', methods=["GET", "POST"])
def admin_login():
    if request.method == "GET":
        return render_template('admin_login.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        password = form['password']

        admin = Admin.objects(name=name, password=password)

        if len(admin) > 0:
            session['admin'] = True
            return redirect(url_for('admin'))
        else:
            return "Sai tên hoặc mk "

@app.route('/sign-out')
def sign_out():
    del session['admin']
    return redirect(url_for('index'))


#########################
@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        service.delete()
        return redirect(url_for('admin'))
    else:
        return "Not found"

##########################
@app.route('/new-service', methods=["GET", "POST"])
def new_service():
    if request.method == "GET":
        return render_template('new_service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        gender = form['gender']
        height = form['height']
        phone = form['phone']
        address = form['address']  
        status = form['status']


        new_service = Service(
            name=name,
            yob=yob,
            gender=gender,
            height=height,
            phone=phone,
            address=address,
            status=status
        )

        new_service.save()

        return redirect(url_for('admin'))

##########################
@app.route('/update-service/<service_id>', methods=["GET", "POST"])
def update(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:  
        if request.method == "GET":
            return render_template('update.html', service=service)
        elif request.method == "POST":
            form = request.form
            name = form['name']
            yob = form['yob']
            phone = form['phone']
            height = form['height']
            address = form['address']
            status = form['status']

            service.update(
                set__name=name,
                set__yob=yob,
                set__phone=phone,
                set__height=height,
                set__address=address,
                set__status=status  
            )

            service.reload()
            service.save()
            return redirect(url_for('admin'))
    else:
        return "Not found"

#######################
@app.route('/detail/<service_id>')
def detail(service_id):
    if 'logged_in' in session:
        service = Service.objects.with_id(service_id)
        return render_template('detail.html', service=service)
    else:
        return redirect(url_for('login'))


#######################
@app.route('/sign-in', methods=["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template('sign_in.html')
    elif request.method == "POST":
        form = request.form
        full_name = form['fullname']
        email = form['email']
        username = form['username']
        password = form['password']

        new_user = User(
            full_name=full_name,
            email=email,
            username=username,
            password=password
        )

        new_user.save()
        return "Welcome to Warm Winter Page"


#######################
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        form = request.form
        username = form['username']
        password = form['password']

        users = User.objects(username = username, password = password)

        if len(users) > 0:
            session['logged_in'] = True
            session['user_id'] = username
            return redirect (url_for('another_search'))
        else:
            return "Sai username hoặc password"

#########################
@app.route('/logout')
def logout():
    del session['logged_in']
    return redirect(url_for('another_search'))

##########################
@app.route('/order/<service_id>')
def order(service_id):
    new_order = Order(
            service_id = service_id,
            user_id = session['user_id'],
            time = datetime.datetime.now(),
            is_accepted = False
            )

    new_order.save()
    return "Đã gửi yêu cầu"

#########################
@app.route('/order-view')
def order_view():
    all_order = Order.objects()
    return render_template('order.html', all_order=all_order)

########################

if __name__ == '__main__':
  app.run(debug=True)
 