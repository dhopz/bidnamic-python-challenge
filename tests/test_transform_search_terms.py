#from transform_search_terms import calculate_roas
from src.etl_pipeline.scripts.csv_transform.transform_search_terms import calculate_roas
import pytest
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from sqlalchemy import create_engine
##from dotenv import load_dotenv
import os



# load_dotenv()

# # PostgreSQL Database credentials loaded from the .env file
# DATABASE = os.getenv('DATABASE')
# DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
# DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

# # Create the engine
# engine = create_engine("postgresql+psycopg2://"+DATABASE_USERNAME+":postgres@localhost/bidnamic")
# Session = sessionmaker()

# @pytest.fixture(scope='module')
# def connection():
#     connection = engine.connect()
#     yield connection
#     connection.close()

# @pytest.fixture(scope='function')
# def session(connection):
#     transaction = connection.begin()
#     session = Session(bind=connection)
#     yield session
#     session.close()
#     transaction.rollback()

def test_calculate_roas():
    assert calculate_roas(100,5) == 20, "return something"
