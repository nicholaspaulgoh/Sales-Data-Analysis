
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df=pd.read_csv('sales_data.csv')
print(f"Loaded: {len(df)} rows , {len(df.columns)} columns")
print(df)

#The revenue categorised by region
df["Revenue"] = df["Quantity"] * df["Price"]
region_revenue = df.groupby('Region')["Revenue"].sum().reset_index()
print(f"\n\nRevenue organised by Region\n{region_revenue}")

plt.bar(region_revenue["Region"], region_revenue["Revenue"])
plt.title("Revenue Performance by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.show()

#Every ProductID and their Revenue
product_revenue =df.groupby('ProductID')["Revenue"].sum().reset_index()
print(f"\n\nRevenue organised by product ID\n{product_revenue}")

plt.bar(product_revenue["ProductID"], product_revenue["Revenue"])
plt.title("Revenue Performance by ProductID")
plt.xlabel("Product ID")
plt.ylabel("Total Revenue")
plt.show()



#Every month and their revenue
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.month_name()


month_order = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]

df["Month"] = pd.Categorical(df["Month"], categories=month_order)
monthly_revenue= df.groupby(df["Month"])["Revenue"].sum().reset_index()
print(f"\n\nRevenue organised by month names\n{monthly_revenue.sort_values(by='Month')}")


plt.bar(monthly_revenue["Month"], monthly_revenue["Revenue"])

plt.title("Monthly Revenue Performance")
plt.xlabel("Month")
plt.ylabel("Total Revenue")

plt.show()

#The month with the highest revenue
max_monthly_revenue_id = monthly_revenue["Revenue"].idxmax()
highest_revenue_month =monthly_revenue.loc[max_monthly_revenue_id]
print(f"\n\nThe month with the highest revenue is\n{highest_revenue_month}")

















