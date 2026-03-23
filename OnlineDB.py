import pandas as pd 
import sqlite3 as sq3
import os

def create_sqlite_connection(location_path, db_name):
    full_path = os.path.join(location_path, db_name)
    conn = sq3.connect(full_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    print(f"Database created successfully at {full_path}")
    return conn
def create_tables(conn):
    cursor = conn.cursor()
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID INTEGER PRIMARY KEY,
            Country TEXT NOT NULL 
        );
    ''')

    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS Products (
            StockCode TEXT PRIMARY KEY,
            Description TEXT NOT NULL,
            UnitPrice REAL NOT NULL
        );
    ''')

 
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS Transactions (
            TransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
            InvoiceNo TEXT NOT NULL,
            CustomerID INTEGER,
            StockCode TEXT,
            Quantity INTEGER NOT NULL,
            InvoiceDate TEXT NOT NULL,
            UnitPrice REAL,
            TotalAmount_GBP REAL NOT NULL,
            FOREIGN KEY(CustomerID) REFERENCES Customers(CustomerID),
            FOREIGN KEY(StockCode) REFERENCES Products(StockCode)
        );
    ''')
    print('Tables created successfully')
    

import os

def dataframe(folder, filename):
    locatefile = os.path.join(folder, filename)
    df = pd.read_csv(locatefile)
    return df

def clean_df(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def inserting_df__db(df, table_name,conn):
    df.to_sql(table_name,conn, if_exists = 'replace', index= False)
    print(f'{table_name} table populated successfully.')

   
    conn.commit()
    conn.close()

   
