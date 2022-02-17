import os
import csv
from datetime import datetime

base_path = os.path.dirname(os.path.abspath("__file__"))
transformed_path = f"{base_path}/data/transformed/new_search_terms.csv"

def calculate_roas(conversion_value,cost):
    '''
    Return On Ad Spend (ROAS)    
    '''
    return conversion_value/cost

