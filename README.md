# AI-SQL Driven Sales Dashboard (PostgreSQL)

This is a starter project that demonstrates a Python → PostgreSQL → Power BI analytics pipeline.

## Contents
- `data/raw_sales.csv` - sample raw dataset
- `data/cleaned_sales.csv` - generated after ETL
- `src/etl_pipeline.py` - Python ETL script (uses SQLAlchemy)
- `src/db_config.py` - PostgreSQL DB URI template
- `src/queries.sql` - SQL views for Power BI
- `dashboards/Sales_Dashboard.pbix` - **placeholder** Power BI file (replace with your .pbix)
- `requirements.txt` - Python dependencies

## Setup (local)
1. Install Python deps:
   ```
   pip install -r requirements.txt
   ```

2. Install PostgreSQL and create database `sales_db`:
   - On Ubuntu:
     ```
     sudo apt update
     sudo apt install postgresql postgresql-contrib
     sudo -u postgres psql
     CREATE DATABASE sales_db;
     \q
     ```
   - On Windows/Mac: install from https://www.postgresql.org/download/

3. Edit `src/db_config.py` and set the correct DB_URI:
   ```
   DB_URI = "postgresql+psycopg2://<user>:<password>@<host>:5432/sales_db"
   ```

4. Run the ETL:
   ```
   python src/etl_pipeline.py
   ```

5. Load SQL views:
   ```
   psql -U postgres -d sales_db -f src/queries.sql
   ```

6. Power BI:
   - Connect Power BI Desktop → PostgreSQL (use the same connection details).
   - Import `monthly_sales` and `top_customers` views.
   - Build visuals: line chart (monthly sales by region), bar chart (top customers), category trends.

## Note about the Power BI file
`dashboards/Sales_Dashboard.pbix` is a placeholder text file included so you have the filename in the repo.
To create your actual `.pbix` file:
- Open Power BI Desktop
- Get Data → PostgreSQL
- Load the two views and design your report
- Save as `dashboards/Sales_Dashboard.pbix`

Enjoy! 🚀
