from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://ascse:JEZwPXpiGWeYsrmGO6ysYOzwb9yHgd3p@dpg-cersrjun6mphf4uqlrkg-a.singapore-postgres.render.com/ascse"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'sslmode':'require'},
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

