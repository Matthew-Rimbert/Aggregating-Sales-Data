import pandas as pd

# Define a list of tuples representing orders
orders = [
    (9423517, '2022-02-04', 9001),
    (4626232, '2022-02-04', 9003),
    (9423534, '2022-02-04', 9001),
    (9423679, '2022-02-05', 9002),
    (4626377, '2022-02-05', 9003),
    (4626412, '2022-02-05', 9004),
    (9423783, '2022-02-06', 9002),
    (4626490, '2022-02-06', 9004)
]

# Convert the list to a DataFrame with specified column names
df_orders = pd.DataFrame(orders, columns=['OrderNo', 'Date', 'Empno'])

# Define a list of tuples representing order details
details = [
    (9423517, 'Jeans', 'Rip Curl', 87.0, 1),
    (9423517, 'Jacket', 'The North Face', 112.0, 1),
    (4626232, 'Socks', 'Vans', 15.0, 1),
    (4626232, 'Jeans', 'Quiksilver', 82.0, 1),
    (9423534, 'Socks', 'DC', 10.0, 2),
    (9423534, 'Socks', 'Quiksilver', 12.0, 2),
    (9423679, 'T-shirt', 'Patagonia', 35.0, 1),
    (4626377, 'Hoody', 'Animal', 44.0, 1),
    (4626377, 'Cargo Shorts', 'Animal', 38.0, 1),
    (4626412, 'Shirt', 'Volcom', 78.0, 1),
    (9423783, 'Boxer Shorts', 'Superdry', 30.0, 2),
    (9423783, 'Shorts', 'Globe', 26.0, 1),
    (4626490, 'Cargo Shorts', 'Billabong', 54.0, 1),
    (4626490, 'Sweater', 'Dickies', 56.0, 1)
]

# Convert the list to a DataFrame with specified column names
df_details = pd.DataFrame(details, columns=['OrderNo', 'Item', 'Brand', 'Price', 'Quantity'])

# Define a list of tuples representing employees
emps = [
    (9001, 'Jeff Russell', 'LA'),
    (9002, 'Jane Boorman', 'San Francisco'),
    (9003, 'Tom Heints', 'NYC'),
    (9004, 'Maya Silver', 'Philadelphia')
]

# Convert the list to a DataFrame with specified column names
df_emps = pd.DataFrame(emps, columns=['Empno', 'Empname', 'Location'])

# Define a list of tuples representing locations
locations = [
    ('LA', 'West'),
    ('San Francisco', 'West'),
    ('NYC', 'East'),
    ('Philadelphia', 'East')
]

# Convert the list to a DataFrame with specified column names
df_locations = pd.DataFrame(locations, columns=['Location', 'Region'])

# Merge on 'OrderNo' to combine order and order detail information
df_sales = df_orders.merge(df_details)

# Create a new column 'Total' as the product of 'Price' and 'Quantity'
df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']

# Filter down to necessary columns for the next join
df_sales = df_sales[['Date', 'Empno', 'Total']]

# Merge with df_emps to add employee and location info
df_sales_emps = df_sales.merge(df_emps)

# Merge with df_locations to add region info
df_result = df_sales_emps.merge(df_locations)

# Filter to necessary columns for aggregation
df_result = df_result[['Date', 'Region', 'Total']]

# Group by Date and Region, then sum the totals
df_date_region = df_result.groupby(['Date', 'Region']).sum()

# Calculate the grand total
ps = df_date_region.sum(axis=0)
ps.name = ('All', 'All')

# Concatenate the grand total row to the DataFrame
df_date_region_total = pd.concat([df_date_region, pd.DataFrame([ps])])

# Adding subtotals for each date
df_totals = pd.DataFrame()
for date, date_df in df_date_region.groupby(level=0):
    df_totals = pd.concat([df_totals, date_df])
    ps = date_df.sum(axis=0)
    ps.name = (date, 'All')
    df_totals = pd.concat([df_totals, pd.DataFrame([ps])])

# Append the grand total row to the DataFrame
df_totals = pd.concat([df_totals, pd.DataFrame([df_date_region_total.loc[('All', 'All')]])])

# Exclude grand total and subtotal rows for further operations if needed
df_filtered = df_totals[~df_totals.index.isin([('All', 'All')] + [(date, 'All') for date in df_date_region.index.levels[0]])]

# Display the final filtered DataFrame
print(df_filtered)
