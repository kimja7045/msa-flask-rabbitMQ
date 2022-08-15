from flask import Flask
from flask_sqlalchemy import SQLALCHEMY
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@db/main'
CORS(app)

db = SQLALCHEMY(app)

class Shop():
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    shop_name = db.Column(db.String(32))
    shop_address = db.Column(db.String(100))

# class Shop(models.Model):
#     shop_name = models.CharField(max_length=32)
#     shop_address = models.CharField(max_length=100)
#     address_detail = models.TextField()

class Order():
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    shop = db.Column(db.Integer)
    address = db.Column(db.String(100))

# class Order(models.Model):
#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
#     address = models.CharField(max_length=100)


@app.route('/')
def index():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')