from fastapi import FastAPI
from models import Product

app = FastAPI()

products = [
    Product(id=1, name="Phone", description="Mobile Phone", price=195.90, quantity=5), 
    Product(id=2, name="Laptop", description="Normal Laptop", price=200.00, quantity=7),
    Product(id=3, name="Headset", description="Wireless Headset", price=24.49, quantity=15),
    Product(id=4, name="Charger", description="35W Charger", price=15.00, quantity=12)
]

@app.get('/')
def greet():
    return "Hello World all"

@app.get('/products')
def get_all_products():
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return "Product not found"


@app.post("/product")
def update_product(product: Product):
    products.append(product)
    return product


@app.put("/product")
def update_product(id: int, product: Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "Product updated successfully"
    return "Product not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "Product deleted successfully"
    return "Product not found"