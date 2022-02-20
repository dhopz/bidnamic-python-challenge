import os
import csv
from datetime import datetime

from common.tables import AdGroupsAll
from common.base import session
from sqlalchemy import text

#base_path = os.path.dirname(os.path.abspath("__file__"))
base_path = os.path.abspath(__file__ + "/../../../")
#print(base_path)
transformed_path = f"{base_path}/data/raw/adgroups.csv"

def truncate_table():
    """
    Ensure that the tables are in an empty state before running any transformations.
    And primary key (id) restarts from 1.
    """
    session.execute(
        text("TRUNCATE TABLE adgroups;ALTER SEQUENCE adgroups_id_seq RESTART;")
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
                AdGroupsAll(
                    ad_group_id = row["ad_group_id"],
                    campaign_id = row["campaign_id"],
                    alias = row["alias"],
                    status = row["status"],               
                )
            )
        # Save all new processed objects and commit
        session.bulk_save_objects(new_objects)
        session.commit()

def main():
    print("[Transform] Start")
    print("[Transform] Remove any old data from adgroups table")
    truncate_table()
    print("[Transform] Transform new data available in adgroups table")
    transform_new_data()
    print("[Transform] End")
