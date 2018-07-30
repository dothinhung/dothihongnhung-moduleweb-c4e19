from flask import Flask, render_template
import mlab
from models.service import Service
from models.customer import Customer

app = Flask(__name__)

# connect database
mlab.connect()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
    all_service = Service.objects(gender=gender, 
                                yob__lte = 1998,
                                )
    return render_template('search.html', all_service = all_service)

@app.route('/customer')
def customer(gender):
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer = all_customer)


@app.route('/customermale')
def customer_male():
    ten_first_cus = Customer.objects(gender=1), limit(10)
    return render_template('customer.html', all_customer=ten_first_cus)

if __name__ == '__main__':
  app.run(debug=True)
 