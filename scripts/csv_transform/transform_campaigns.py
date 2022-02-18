import os
import csv
from datetime import datetime

from scripts.common.tables import CampaignsAll
from scripts.common.base import session
from sqlalchemy import text


base_path = os.path.dirname(os.path.abspath("__file__"))
transformed_path = f"{base_path}/data/raw/campaigns.csv"

def truncate_table():
    """
    Ensure that the tables are in an empty state before running any transformations.
    And primary key (id) restarts from 1.
    """
    session.execute(
        text("TRUNCATE TABLE campaigns;ALTER SEQUENCE campaigns_id_seq RESTART;")
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
                CampaignsAll(                    
                    campaign_id = row["campaign_id"],
                    structure_value = row["structure_value"],
                    status = row["status"],
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
