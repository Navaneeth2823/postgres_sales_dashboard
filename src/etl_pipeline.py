"""
ETL pipeline script: loads data/data/raw_sales.csv, cleans it, writes cleaned CSV and loads into PostgreSQL.
Usage:
  pip install -r requirements.txt
  # set DB_URI in src/db_config.py
  python src/etl_pipeline.py
"""
import os
import pandas as pd
from sqlalchemy import create_engine
from src.db_config import DB_URI

def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = df.columns.str.lower()
    # basic cleaning steps
    df = df.copy()
    # parse dates
    if "Order Date" in df.columns:
        df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
    # drop rows with null order date or order id
    df = df.dropna(subset=["Order ID","Order Date"])
    # coerce numeric columns
    for col in ["Sales","Quantity","Discount","Profit"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    # fill missing textual fields
    df["Region"] = df["Region"].fillna("Unknown")
    return df

def main():
    # Get base project directory (where ai_sql_sales_dashboard_postgres is located)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Point to data/raw_sales.csv
    raw_path = os.path.join(BASE_DIR, "data", "raw_sales.csv")

    print("Loading:", raw_path)
    df = pd.read_csv(raw_path)

    # Simple cleaning
    df = df.dropna()

    # Save cleaned file back into data/
    cleaned_path = os.path.join(BASE_DIR, "data", "cleaned_sales.csv")
    df.to_csv(cleaned_path, index=False)
    print("Saved cleaned data to", cleaned_path)

    print("Loading into PostgreSQL:", DB_URI)
    engine = create_engine(DB_URI)
    # write to table 'sales' (replace existing)
    df.to_sql("sales", engine, if_exists="replace", index=False)
    print("✅ ETL Completed: Data loaded into PostgreSQL.")

if __name__ == "__main__":
    main()
