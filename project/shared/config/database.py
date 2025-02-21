from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from dotenv import load_dotenv
import os

load_dotenv()


SQL_ALCHEMY_DATABASE_URL = "mysql+pymysql://{}:{}@{}:{}/{}".format(
    os.getenv("DB_USERNAME"),
    os.getenv("DB_PASSWORD"),
    os.getenv("DB_HOST"),
    os.getenv("DB_PORT"),
    os.getenv("DB_DATABASE")
)

DB_SSL_PEM_CA = os.getenv("DB_SSL_PEM_CA", "mysql-ssl-ca.crt.pem")
if os.path.exists(DB_SSL_PEM_CA):
    SQL_ALCHEMY_DATABASE_URL += f"?ssl_ca={DB_SSL_PEM_CA}"

engine = create_engine(
    SQL_ALCHEMY_DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()
SessionFactory = scoped_session(SessionLocal, scopefunc="")