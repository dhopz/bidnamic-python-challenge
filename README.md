# Python Software Engineering Challenge

### Task

1. Some CSVs have been given (campaigns.csv, adgroups.csv and search_terms.csv), load them into a database.


2. Create some private end points to return the Top 10 Search Terms by ROAS for a campaign `structure_value` or adgroup `alias`.

### My Results

Navigate to src/etl_pipeline/scripts and run Python3 execute.py inside a Virtual Environment.

![Alt text](/src/etl_pipeline/assets/server.png?raw=true)

![Alt text](/src/etl_pipeline/assets/alias.png?raw=true)

![Alt text](/src/etl_pipeline/assets/structure_value.png?raw=true)

### My Notes
I followed an ETL Pipeline because I saw that part of the Stack was SQLAlchemy.
- I created an Extract method, it wasn't required but I thought it would be best practice.
- I didn't do a Load method, normally I would so that the database is only populated with new data.
- I did the Tests retrospectively. Not best practice, I have only used PyTest for simple methods.