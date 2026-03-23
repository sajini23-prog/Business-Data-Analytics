import pandas as pd
import sqlite3 as sq3

def running_query(query_string, conn):
    return pd.read_sql_query(query_string, conn)

def total_quantity_per_product_monthly(conn):

    query = '''
    SELECT StockCode, strftime('%Y-%m', InvoiceDate) AS Month, SUM(Quantity) AS TotalQuantity
    FROM Transactions
    GROUP BY StockCode, Month
    ORDER BY Month, StockCode;
    '''
    return running_query(query, conn)

def sales_trends_per_product(conn):
    
    query = '''
    SELECT p.Description, strftime('%Y-%m', t.InvoiceDate) AS Month, SUM(t.TotalAmount_GBP) AS MonthlySales
    FROM Transactions t
    JOIN Products p ON t.StockCode = p.StockCode
    GROUP BY p.Description, Month
    ORDER BY Month, p.Description;
    '''
    return running_query(query, conn)

def top_5_customers_by_sales(conn):
    
    query = '''
    SELECT c.CustomerID, SUM(t.TotalAmount_GBP) AS TotalSales 
    FROM Transactions t
    JOIN Customers c ON t.CustomerID = c.CustomerID
    GROUP BY c.CustomerID
    ORDER BY TotalSales DESC
    LIMIT 5;
    '''
    return running_query(query, conn)

def revenue_by_product(conn):
    query = '''
    SELECT p.Description, SUM(t.TotalAmount_GBP) AS TotalRevenue
    FROM Transactions t
    JOIN Products p ON t.StockCode = p.StockCode
    GROUP BY p.Description
    ORDER BY TotalRevenue DESC;
    '''
    return running_query(query, conn)
