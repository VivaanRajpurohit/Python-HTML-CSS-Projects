import pandas as pd

# Creating a dictionary with data
data = {
    "product category": ["Electronics", "Clothing", "Furniture", "Electronics", "Clothing", "Furniture", "Electronics", "Furniture", "Clothing"],
    "sales": [1000, 500, 2000, 1500, 1200, 800, 1300, 2200, 700]
}

# Creating a DataFrame from the dictionary
sales_data = pd.DataFrame(data)

# Displaying the dataset
print(sales_data)


total_sales_by_category = sales_data.groupby("product category")["sales"].sum()
sorted_sales = total_sales_by_category.sort_values(ascending=False)
print(sorted_sales.head(3))
