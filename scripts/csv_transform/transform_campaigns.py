import os
import csv
from datetime import datetime

from scripts.common.tables import SearchTermsAll
from scripts.common.base import session
from sqlalchemy import text


base_path = os.path.dirname(os.path.abspath("__file__"))
transformed_path = f"{base_path}/data/transformed/new_search_terms.csv"

def calculate_roas(conversion_value,cost):
    '''
    Return On Ad Spend (ROAS)    
    '''
    try:
        return conversion_value/cost
    except ZeroDivisionError:
        return 0

def truncate_table():
    """
    Ensure that the tables are in an empty state before running any transformations.
    And primary key (id) restarts from 1.
    """
    session.execute(
        text("TRUNCATE TABLE search_terms_all;ALTER SEQUENCE search_terms_all_id_seq RESTART;")
    )
    session.commit()

def transform_new_data():
    """
    Apply all transformations for each row in the .csv file before saving it into database
    """
    with open(transformed_path, mode="r", encoding="utf-8") as csv_file:
        # Read the new CSV snapshot ready to be processed
        reader = csv.DictReader(csv_file)
        # Initialize an empty list 
        new_objects = []
        for row in reader:
            # Apply transformations and save as object
            new_objects.append(
                SearchTermsAll(
                    date_of_search = row["date_of_search"],
                    ad_group_id = row["ad_group_id"],
                    campaign_id = row["campaign_id"],
                    clicks = row["clicks"],
                    cost = row["cost"],
                    conversion_value = row["conversion_value"], 
                    conversions = row["conversions"],
                    search_term = row["search_term"],
                    roas = calculate_roas(float(row["conversion_value"]),float(row["cost"]))                 
                )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(new_objects)
        session.commit()

def main():
    print("[Transform] Start")
    print("[Transform] Remove any old data from search_terms_all table")
    truncate_table()
    print("[Transform] Transform new data available in search_terms_all table")
    transform_new_data()
    print("[Transform] End")
