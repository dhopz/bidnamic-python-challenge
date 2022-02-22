from hashlib import new
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from src.etl_pipeline.scripts.common.tables import CampaignsAll,AdGroupsAll,SearchTermsAll
import pytest
from sqlalchemy import text
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
# Initialize the session
engine = create_engine("postgresql+psycopg2://"+DATABASE_USERNAME+":postgres@localhost/bidnamic_test")
session = Session(engine)
Base = declarative_base()

@pytest.fixture
def dbsession():
    seed_database()
    yield engine
    engine.dispose()
    clear_tables()

def seed_database():
    campaigns =[
        {
            "campaign_id":"1578411797",
            "structure_value":"nike",
            "status":"enabled"
        }
    ]
    search_terms = [
        {
            "date_of_search": "22/12/2020",
            "ad_group_id":"80860031197",
            "campaign_id":"1578411797",
            "clicks":1,
            "cost":0.19,
            "conversion_value":21.98,
            "conversions":1,
            "search_term":"nike gloves hyperwarm",
        }
    ]
    adgroups = [
        {
            "ad_group_id":"80860031197",
            "campaign_id":"1578411797",
            "alias":"Shift - Shopping - GB - nike - MEDIUM - steak-venus-robert-whiskey - 244259ebff754f2e8dc306f2832b217a",
            "status":"ENABLED",
        }
    ]
    new_objects = []

    for ads in adgroups:
        new_objects.append(
            AdGroupsAll(
                ad_group_id = ads["ad_group_id"],
                campaign_id = ads["campaign_id"],
                alias = ads["alias"],
                status = ads["status"],
            )
        )

    for campaign in campaigns:
        # Apply transformations and save as object
        new_objects.append(
            CampaignsAll(
                campaign_id = campaign["campaign_id"],
                structure_value = campaign["structure_value"],
                status = campaign["status"],               
            )
        )

    for search in search_terms:
        new_objects.append(
            SearchTermsAll(
                date_of_search = search["date_of_search"],
                ad_group_id = search["ad_group_id"],
                campaign_id = search["campaign_id"],
                clicks = search["clicks"],
                cost = search["cost"],
                conversion_value = search["conversion_value"], 
                conversions = search["conversions"],
                search_term = search["search_term"],
                roas = float(search["conversion_value"])/float(search["cost"])
            )
        )
    # Save all new processed objects and commit
    session.bulk_save_objects(new_objects)
    session.commit()
    print("---???---")

def clear_tables():
    session.execute(
        text("TRUNCATE TABLE campaigns;ALTER SEQUENCE campaigns_id_seq RESTART;")
    )
    session.commit()
    session.execute(
        text("TRUNCATE TABLE adgroups;ALTER SEQUENCE adgroups_id_seq RESTART;")
    )
    session.commit()
    session.execute(
        text("TRUNCATE TABLE search_terms_all;ALTER SEQUENCE search_terms_all_id_seq RESTART;")
    )
    session.commit()
    print("clearing")

def test_campaigns(dbsession):
    data = session.execute("SELECT * FROM campaigns;").all()
    assert data == [(1, '1578411797', 'nike', 'enabled')], "campaigns data format in database"

def test_adgroups(dbsession):
    data = session.execute("SELECT * FROM adgroups;").all()
    assert data == [(1, '80860031197', '1578411797', 'Shift - Shopping - GB - nike - MEDIUM - steak-venus-robert-whiskey - 244259ebff754f2e8dc306f2832b217a', 'ENABLED')], "adgroups data format in database"

def test_searchterms(dbsession):
    data = session.execute("SELECT ad_group_id, campaign_id FROM search_terms_all;").all()
    assert data == [('80860031197', '1578411797')], "search terms data format in database"

    
