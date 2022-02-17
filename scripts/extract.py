import os
import csv
from pprint import pprint

# Settings
base_path = os.path.dirname(os.path.abspath("__file__"))
adgroups_path = f"{base_path}/data/raw/adgroups.csv"
raw_path = f"{base_path}/data/raw_adgroups.csv"

# Create extraction method - may need to amend fields
def extract_raw_data():
    """
    Save data from the source
    """

    with open(adgroups_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)    
        # Print the first row
        row = next(reader)
        
        with open(raw_path, mode="w") as csv_file:
            fieldnames = {
                "ad_group_id":"ad_group_id",
                "campaign_id":"campaign_id",
                "alias":"alias",
                "status":"status"
            }
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            for row in reader:
                writer.writerow(row)


# Main function called inside the execute.py script
def main():
    print("[Extract] Start")
    print(f"[Extract] Saving data from '{adgroups_path}' to '{raw_path}'")
    extract_raw_data()
    print(f"[Extract] End")