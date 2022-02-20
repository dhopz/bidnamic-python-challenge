from csv_transform.transform_adgroups import main as adgroups_main
from csv_transform.transform_campaigns import main as campaigns_main
from csv_transform.transform_search_terms import main as search_terms_main  

def main():
    print("[Transform All Files] Start")    
    adgroups_main()
    campaigns_main()
    search_terms_main()
    print("[Transform All Files] End")

