from fastapi import FastAPI
from models import Product
from database import sessionLocal, engine
import database_models

app = FastAPI()

database_models.Base.metadata.create_all(bind=engine)

products = [
    Product(id=1, name="Phone", description="Mobile Phone", price=195.90, quantity=5), 
    Product(id=2, name="Laptop", description="Normal Laptop", price=200.00, quantity=7),
    Product(id=3, name="Headset", description="Wireless Headset", price=24.49, quantity=15),
    Product(id=4, name="Charger", description="35W Charger", price=15.00, quantity=12),
]

def init_db():
    db = sessionLocal()

    # count = 0
    count = db.query(database_models.Product).count

    if count == 0:
        for product in products:
            db.add(database_models.Product(**product.model_dump()))

        db.commit()

init_db()

@app.get('/')
def greet():
    return "Hello World all"

@app.get('/products')
def get_all_products():
    # db = sessionLocal()


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