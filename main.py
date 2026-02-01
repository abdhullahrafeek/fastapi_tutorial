from fastapi import Depends, FastAPI
from models import Product
from database import sessionLocal, engine
import database_models
from sqlalchemy.orm import Session

app = FastAPI()

@app.on_event("startup")
def startup():
    database_models.Base.metadata.create_all(bind=engine)

products = [
    Product(id=1, name="Phone", description="Mobile Phone", price=195.90, quantity=5), 
    Product(id=2, name="Laptop", description="Normal Laptop", price=200.00, quantity=7),
    Product(id=3, name="Headset", description="Wireless Headset", price=24.49, quantity=15),
    Product(id=4, name="Charger", description="35W Charger", price=15.00, quantity=12),
]

def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()

# def init_db():
#     db = sessionLocal()

#     # count = 0
#     count = db.query(database_models.Product).count

#     if count == 0:
#         for product in products:
#             db.add(database_models.Product(**product.model_dump()))

#         db.commit()

# init_db()

@app.get('/')
def greet():
    return "Hello World all"

@app.get('/products')
def get_all_products(db: Session = Depends(get_db)):
    db_products = db.query(database_models.Product).all()
    
    return db_products
    # return products

@app.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
        return db_product
    return "Product not found"


@app.post("/product")
def update_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_models.Product(**product.model_dump()))
    db.commit()
    return product


@app.put("/product")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
            db_product.description = product.description
            db_product.name = product.name
            db_product.price = product.price
            db_product.quantity = product.quantity
            db.commit()
            return "Product updated successfully"
    return "Product not found"

@app.delete("/product")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_models.Product).filter(database_models.Product.id == id).first()
    if db_product:
            db.delete(db_product)
            db.commit()
            return "Product deleted successfully"
    return "Product not found"