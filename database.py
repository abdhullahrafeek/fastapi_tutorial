from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url = "postgresql://postgres:abc123@localhost:5432/fastapi_demo_db"
engine = create_engine(db_url)
sessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)