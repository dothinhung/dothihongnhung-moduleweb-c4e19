from flask import *
import mlab
from models.service import Service
from models.customer import Customer

app = Flask(__name__)

# connect database
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/search/<gender>')
# def search(gender):
#     all_service = Service.objects(gender=gender, 
#                                 yob__lte = 1998,
#                                 )
#     return render_template('search.html', all_service = all_service)

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer = all_customer)

# @app.route('/customermale')
# def customermale():
#     ten_customer = Customer.objects(gender=1) [:10]
#     return render_template('customer.html', all_customer = ten_customer)


@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service = all_service)

@app.route('/new_service', methods=["GET", "POST"])
def create():
    if request.method == "GET":
        return render_template('new_service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']

        new_service = Service(
            name=name,
            yob=yob,
            phone=phone
        )

        new_service.save()

        return redirect('admin')


@app.route('/delete/<service_id>')
def delete(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        service.delete()
        # chạy lại route admin
        return redirect(url_for('admin'))
    else:
        return "Not found"

@app.route('/update/<service_id>', methods=["GET", "POST"])
def update(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        if request.method == "GET":
            return render_template("update_service.html", service= service)
        elif request.method == "POST":
            service.update(set__name= request.form['name'],
            set__yob= request.form['yob'],
            set__phone= request.form['phone'],
            set__height= request.form['height'],
            set__address= request.form['address'],
        )
        return redirect(url_for('admin'))
    else:
        return "Not found"


@app.route('/search')
def search():
    all_service = Service.objects()
    return render_template('search.html', all_service = all_service)


@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)
    if service is not None:
        return render_template('detail.html', service = service)
    else:
        return "Not found"


if __name__ == '__main__':
    app.run(debug=True)
 
 