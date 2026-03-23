import sqlite3 as sq3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
import QueryData as qd

sns.set(style="whitegrid")

def plot_total_quantity_bar(conn):

    df = qd.total_quantity_per_product_monthly(conn)
    tot_quan_bar_df = df.sort_values(by='TotalQuantity', ascending = False)
    sns.barplot(data=df.head(12), x='StockCode', y='TotalQuantity', errorbar = None)
    plt.title("Top 12 products by quantity sold")
    plt.xlabel("Product")
    plt.ylabel("Total Quantity")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_sales_trends_line(conn):
    
    df = qd.sales_trends_per_product(conn)
    top_products = df.groupby('Description')['MonthlySales'].sum().nlargest(10).index
    top5_df = df[df['Description'].isin(top_products)]
    sns.lineplot(x='Month', y='MonthlySales', hue = 'Description' ,data=top5_df, marker = "o")
    plt.title("Monthly sales trends per product")
    plt.xlabel("Month")
    plt.ylabel("Total Sales")
    plt.xticks(rotation=45) 
    plt.tight_layout()
    plt.show()

def plot_top_customers_barh(conn):

    df = qd.top_5_customers_by_sales(conn)
    df['CustomerID'] = df['CustomerID'].astype(str)
    sns.barplot(x='TotalSales', y='CustomerID', data=df)
    plt.title("Top 5 customers by total sales")
    plt.xlabel("Total Sales")
    plt.ylabel("Customer ID")
    plt.tight_layout()
    plt.show()

def plot_revenue_pie_chart(conn):
    df = qd.revenue_by_product(conn)
    
    top_df = df.head(5).copy()
    top_df = top_df.rename(columns={'TotalRevenue': 'Revenue'}) 
    others_total = df['TotalRevenue'].iloc[5:].sum()
    other_row = pd.DataFrame([{'Description': 'Other', 'Revenue': others_total}])

    pie_df = pd.concat([top_df, other_row], ignore_index=True)

    plt.pie(pie_df['Revenue'], labels=pie_df['Description'], autopct='%1.1f%%', startangle=180)
    plt.title("Revenue contribution of each product")
    plt.tight_layout()
    plt.show()


    