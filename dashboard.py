import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data (correct path)
df = pd.read_csv('sales_data.csv' )

# Convert date
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

st.title("📊 Sales Dashboard")

# Metrics
st.write("Total Revenue:", df['Revenue'].sum())
st.write("Total Quantity:", df['Quantity'].sum())
st.write("Average Order Value:", df['Revenue'].mean())

# Monthly trend
st.subheader("Monthly Revenue")
monthly_sales = df['Revenue'].resample('M').sum()
st.line_chart(monthly_sales)

# Top products
st.subheader("Top Products")
top_products = df.groupby('Product')['Revenue'].sum().sort_values(ascending=False).head(10)
st.bar_chart(top_products)

# Region sales
st.subheader("Region Sales")
region_sales = df.groupby('Region')['Revenue'].sum()
st.bar_chart(region_sales)