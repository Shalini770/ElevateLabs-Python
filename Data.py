# -----------------------------------------
# SALES DATA ANALYSIS USING PANDAS & MATPLOTLIB
# -----------------------------------------

# Step 1: Import Libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the CSV File (update the filename if needed)
df = pd.read_csv("sales.csv")

# Step 3: Display first few rows and summary
print("----- Dataset Preview -----")
print(df.head())
print("\n----- Dataset Info -----")
print(df.info())
print("\n----- Statistical Summary -----")
print(df.describe())

# Step 4: Create Sales column if not available (Quantity × Price)
if "Sales" not in df.columns:
    df["Sales"] = df["Quantity"] * df["Price"]

# Step 5: Convert Date column to datetime format (if exists)
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    df["Month"] = df["Date"].dt.to_period("M")

# -----------------------------------------
# INSIGHT 1: Total Sales by Category
# -----------------------------------------
category_sales = df.groupby("Category")["Sales"].sum()
print("\n----- Total Sales by Category -----")
print(category_sales)

plt.figure()
category_sales.plot(kind="bar")
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# -----------------------------------------
# INSIGHT 2: Total Sales by Month (if Date column exists)
# -----------------------------------------
if "Date" in df.columns:
    monthly_sales = df.groupby("Month")["Sales"].sum()
    print("\n----- Total Sales by Month -----")
    print(monthly_sales)

    plt.figure()
    monthly_sales.plot(kind="line", marker="o")
    plt.title("Total Sales by Month")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()

# -----------------------------------------
# INSIGHT 3: Top 10 Best-Selling Products
# -----------------------------------------
top_products = df.groupby("Product")["Sales"].sum().sort_values(ascending=False).head(10)
print("\n----- Top 10 Best-Selling Products -----")
print(top_products)

plt.figure()
top_products.plot(kind="bar")
plt.title("Top 10 Best-Selling Products")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.tight_layout()
plt.show()

# -----------------------------------------
# INSIGHT 4: Optional — Export results to new CSV files
# -----------------------------------------
category_sales.to_csv("category_sales_summary.csv")
top_products.to_csv("top_products_summary.csv")
if "Date" in df.columns:
    monthly_sales.to_csv("monthly_sales_summary.csv")

print("\nAnalysis Completed Successfully!")