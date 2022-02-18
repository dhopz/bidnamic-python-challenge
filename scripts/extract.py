import os
import csv
from pprint import pprint

# Settings
#base_path = os.path.dirname(os.path.abspath("__file__"))
base_path = os.path.abspath(__file__ + "/../../")
data_path = f"{base_path}/data/raw/search_terms.csv"
transformed_path = f"{base_path}/data/transformed/new_search_terms.csv"

# Create extraction method - may need to amend fields
def extract_raw_data():
    """
    Save data from the source
    """

    with open(data_path, mode="r") as csv_file:
        reader = csv.DictReader(csv_file)    
        # Print the first row
        #row = next(reader)
        
        with open(transformed_path, mode="w") as csv_file:
            fieldnames = {
                "date":"date_of_search",
                "ad_group_id":"ad_group_id",
                "campaign_id":"campaign_id",
                "clicks":"clicks",
                "cost":"cost",
                "conversion_value":"conversion_value",
                "conversions":"conversions",
                "search_term":"search_term"
                
            }
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow(fieldnames)
            for row in reader:
                writer.writerow(row)


# Main function called inside the execute.py script
def main():
    print("[Extract] Start")
    print(f"[Extract] Saving data from '{data_path}' to '{transformed_path}'")
    extract_raw_data()
    print(f"[Extract] End")