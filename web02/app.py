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

@app.route('/update_service/<service_id>', methods=["GET", "POST"])
def update(service_id):
    service = Service.objects.with_id(service_id)
    all_service = Service.objects()
    if service is not None:
        if request.method == "GET":
            return render_template('update_service.html', all_service=all_service)
        elif request.method == "POST":
            form = request.form
            name=form['name'],
            yob=form['yob'],
            gender=form['gender'],
            height=form['height'],
            phone=form['phone'],
            address=form['address'],
            status=form['status']

            Service.update(
                set__name= name,
                set__yob=yob,
                set__gender=gender,
                set__height=height,
                set__phone= phone,
                set__address = address,
                set__status = status
            )
            service.reload()
            
        return redirect(url_for('admin'))
    else:
        return "Not Found"

@app.route('/search')
def search():
    all_service = Service.objects()
    return render_template('search.html', all_service = all_service)


@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)
    all_service = Service.objects()
    if service is not None:
        return render_template('detail.html', all_service = all_service)
    else:
        return "Not found"

if __name__ == '__main__':
  app.run(debug=True)
 