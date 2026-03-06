# NYC Public Safety Data Pipeline

## Overview

This project builds an end-to-end analytics pipeline that ingests real-time public safety incident data from the NYC Open Data API, stores it in Google BigQuery, and visualizes insights using Power BI.

The objective of this project is to demonstrate how modern data workflows integrate APIs, cloud data warehouses, and business intelligence tools to generate insights from real-world public safety data.

---

## Architecture

NYC Open Data API  
↓  
Python ETL Script  
↓  
Google BigQuery Data Warehouse  
↓  
Power BI Dashboard  

The pipeline retrieves incident records from the NYC Open Data platform, loads them into BigQuery for storage and analysis, and connects Power BI for interactive reporting and visualization.

---

## Technologies Used

- Python
- Requests (API ingestion)
- Google BigQuery
- SQL
- Power BI
- NYC Open Data API

---

## Data Source

NYC Open Data – Calls for Service Dataset

This dataset contains records of public safety incidents including:

- Incident type
- Borough
- Incident time
- Event identifiers
- Emergency response categories

---

## Data Pipeline

The Python ETL script performs the following tasks:

1. Connects to the NYC Open Data API
2. Retrieves incident records using pagination
3. Processes the API response into structured data
4. Loads records into a BigQuery table
5. Enables Power BI to query the warehouse for reporting

This architecture follows a modern analytics workflow where data is ingested from external APIs, stored in a cloud data warehouse, and visualized using BI tools.

---

## Dashboard Features

The Power BI dashboard provides an interactive view of NYC public safety incidents and includes the following analyses:

- Total incidents by borough
- Geographic distribution of incidents across NYC
- Incident activity by hour of day
- Breakdown of the most common incident types
- Interactive borough filtering

---

## Key Insights

Example insights from the analysis include:

• Brooklyn reports the highest number of incidents, followed by Manhattan.

• Incident activity peaks between 4 PM and 9 PM, suggesting increased emergency service demand during evening hours.

• "Investigation of a Possible Crime" represents the most frequent incident category.

---

## Repository Structure
