from fastapi import FastAPI
from models import Product

app = FastAPI()

products = [
    Product(id=1, name="Phone", description="New", price=77, quantity=5), 
    Product(id=2, name="PC", description="New", price=150.50, quantity=7)
]

@app.get('/')
def greet():
    return "Hello World all"

@app.get('/products')
def get_all_products():
    return products