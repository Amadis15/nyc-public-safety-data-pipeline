# First start by importing the requests library and other libraries that we will use
import requests
from datetime import datetime, timedelta, timezone
from google.cloud import bigquery

# This is the API and we are going to intialize it to the BASE_URL variable
BASE_URL = "https://data.cityofnewyork.us/resource/n2zq-pubd.json"

# ALL BigQuery Information for
Project_ID = "real-time-public-safety"
Dataset = "Main_Dataset"
Table = "raw_calls_for_service"
Table_ID = f"{Project_ID}.{Dataset}.{Table}"

client = bigquery.Client(project=Project_ID)

# Add the since timestamp of when we will be pulling data
# This is the last date that the dataset refreshed
max_date_str = "2025-12-31T00:00:00.000" 
max_dt = datetime.fromisoformat(max_date_str)
since_dt = max_dt - timedelta(days=90) 
since_ts = since_dt.strftime("%Y-%m-%dT%H:%M:%S.000")


# Lets set API parameters
params = {"$select": "CAD_EVNT_ID,INCIDENT_DATE,INCIDENT_TIME,BORO_NM,PATRL_BORO_NM,TYP_DESC,ADD_TS,DISP_TS,ARRIVD_TS,CLOSNG_TS",
          "$where": f"INCIDENT_DATE > '{since_ts}'",
          "$order": "INCIDENT_DATE ASC,INCIDENT_TIME ASC,CAD_EVNT_ID ASC",
          "$limit": 1000}


# THIS IS WHERE WE ARE GOING TO START PULLING THE API(Pagination)


# initialize an offset variable that tells an API where to start from
offset = 0

# This will tell you how many rows the API will return per request
limit = 1000

pages = 0
total_inserted = 0
max_pages = 250

# Create a while loop that will tell the API to keep looping until it returns nothing
while True:
    params["$offset"] = offset

# Call API
    r = requests.get(BASE_URL, params=params, timeout=30)

# Raise status error(IF Applicable)
    r.raise_for_status()

    # Convert the API Response into Python objects
    batch = r.json()

    # Send an empty list when the API has no more data to return
    if not batch:
        break

    # Add ingested_at since its in my BigQuery Schema
    ingested_at = datetime.now(timezone.utc).isoformat()
    for row in batch:
        row["ingested_at"] = ingested_at

    # Insert rows into Big Query
    errors = client.insert_rows_json(Table_ID, batch)

    if errors:
        print("BigQuery insert errors (first 3):", errors[:3])
        break

    pages += 1

    total_inserted += len(batch)
    print(f"Inserted page={pages} rows={len(batch)} total={total_inserted} last_id={batch[-1].get('CAD_EVNT_ID')}")

    offset += limit

    if pages >= max_pages:
        print("Hit max_pages cap (testing). Stopping.")
        break

print("Total inserted:", total_inserted)
