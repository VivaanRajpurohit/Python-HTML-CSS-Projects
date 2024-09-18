import pandas as pd

data = {
    "Month": ["2024-01-15", "2024-06-20", "2024-07-10", "2024-08-05", "2024-09-15", "2024-06-22", "2024-07-25", "2024-08-18"],
    "product": ["A", "B", "A", "C", "B", "C", "A", "B"],
    "sales": [150, 200, 180, 220, 210, 230, 190, 250]
}

sales_data = pd.DataFrame(data)

print(sales_data)

# Convert the "Month" column to datetime
sales_data["Month"] = pd.to_datetime(sales_data["Month"])

# Set "Month" as the index
sales_data.set_index("Month", inplace=True)

# Filter for summer months (June, July, August)
summer_sales = sales_data.loc[sales_data.index.month.isin([6, 7, 8])]
average_summer_sales = summer_sales.groupby("product")["sales"].mean()

# Find the product with the highest average sales in the summer
top_product = average_summer_sales.idxmax()
print(f"The product with the highest average sales in the summer is: {top_product}")
