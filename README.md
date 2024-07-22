# 📊 Aggregating Sales Data

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-1.3.0+-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.4.2+-red.svg)
![Seaborn](https://img.shields.io/badge/Seaborn-0.11.1+-orange.svg)

## 📋 Purpose
This project aggregates sales data to provide insights and summary statistics. It demonstrates the use of pandas for data manipulation and aggregation, as well as matplotlib and seaborn for data visualization.

## 🛠️ Scope
- Load data into pandas DataFrames
- Merge multiple DataFrames
- Group data and apply aggregate functions
- Generate subtotals and grand totals
- Visualize data using matplotlib and seaborn

## 🚀 Installation
1. **Clone the repository:**
    ```bash
    git clone https://github.com/Matthew-Rimbert/Aggregating-Sales-Data.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd Aggregating-Sales-Data
    ```
3. **Install required Python packages:**
    ```bash
    pip install pandas matplotlib seaborn
    ```

## ▶️ Usage
1. **Run the script:**
    ```bash
    python aggregating_sales_data.py
    ```

2. **View the outputs** in the terminal and generated plots.

## 📊 Data
The dataset used in this project includes:

- **Orders**: This data represents the individual orders placed by customers, including the order number, date, and employee number responsible for the order.
- **Order Details**: This data provides detailed information about each item in the orders, including the order number, item description, brand, price, and quantity.
- **Employees**: This dataset includes information about the employees handling the orders, such as employee number, name, and location.
- **Locations**: This dataset categorizes locations into regions, which helps in regional analysis of sales.

## 🖼️ Example Outputs

### Aggregated Sales Data:
This table shows the aggregated sales data combining information from orders, order details, employees, and locations.

| Date       | Region | Empname      | Total |
|------------|--------|--------------|-------|
| 2022-02-04 | East   | Tom Heints   | 97.0  |
| 2022-02-04 | West   | Jeff Russell | 243.0 |
| 2022-02-05 | East   | Maya Silver  | 78.0  |
| 2022-02-05 | East   | Tom Heints   | 82.0  |
| 2022-02-05 | West   | Jane Boorman | 35.0  |
| 2022-02-06 | East   | Maya Silver  | 110.0 |
| 2022-02-06 | West   | Jane Boorman | 86.0  |

### Total Sales by Region:
This table shows the total sales grouped by region.

| Region | Total |
|--------|-------|
| East   | 367.0 |
| West   | 364.0 |

![Total Sales by Region](https://github.com/user-attachments/assets/d3c95838-5bf1-4d89-97cd-54b75758cdd9)


**Insight:** The total sales by region showcase that sales are evenly distributed between both regions. This even split suggests that both regions have equal potential for sales. This balanced distribution could imply that the sales strategies are uniformly effective across regions, but further analysis might be required to understand the underlying factors contributing to this balance.

### Average Sales per Employee:
This table shows the average sales per employee.

| Empname      | Total |
|--------------|-------|
| Jane Boorman | 60.5  |
| Jeff Russell | 243.0 |
| Maya Silver  | 94.0  |
| Tom Heints   | 89.5  |

![Average Sales per Employee](https://github.com/user-attachments/assets/2eb2a0ef-ff4c-4669-ae68-87c6bec79ec0)


**Insight:** The average sales per employee provide valuable insights into the performance of the sales team. Notably, Jeff Russell has a significantly higher average sales amount. This discrepancy suggests that Jeff Russell may have particularly effective sales tactics or a higher level of experience. To improve overall sales performance, it might be beneficial to analyze Jeff's methods and consider implementing training programs to help other employees achieve similar results. Additionally, introducing incentives could motivate the sales team to enhance their performance.

### Sales Trends Over Time:
This table shows the total sales over time, helping to identify trends in sales.

| Date       | Total |
|------------|-------|
| 2022-02-04 | 340.0 |
| 2022-02-05 | 195.0 |
| 2022-02-06 | 196.0 |

![Sales Trends Over Time](https://github.com/user-attachments/assets/08daf27a-f485-492d-80f8-9dd09f485f64)


**Insight:** The sales trends over time highlight fluctuations in sales performance. February 4th shows a peak in sales, which could be due to specific marketing efforts, promotions, or external factors influencing customer behavior. The following days show a decline, suggesting a need for consistent strategies to maintain high sales levels. Further analysis could help identify the causes of these fluctuations and assist in developing strategies to achieve more stable sales growth.

## 🧩 Code Snippets

### Loading and Merging Data
```python
import pandas as pd

# Load Orders data
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

df_orders = pd.DataFrame(orders, columns=['OrderNo', 'Date', 'Empno'])
```
### Load Order Details data
```python
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

df_details = pd.DataFrame(details, columns=['OrderNo', 'Item', 'Brand', 'Price', 'Quantity'])
```
### Merge Orders and Order Details
```python
df_sales = df_orders.merge(df_details)
df_sales['Total'] = df_sales['Price'] * df_sales['Quantity']
```
## 📈 Summary
This project provides a comprehensive analysis of sales data. By merging multiple fictional datasets, it offers insights into sales performance by region, average sales per employee, and sales trends over time. The visualizations created using matplotlib and seaborn help in understanding the data better and making informed decisions based on the analysis. 

**Total Sales by Region:** The total sales by region showcase that sales are evenly distributed between both regions. This even split suggests that both regions have equal potential for sales. This balanced distribution could imply that the sales strategies are uniformly effective across regions, but further analysis might be required to understand the underlying factors contributing to this balance.

**Average Sales per Employee:** The average sales per employee provide valuable insights into the performance of the sales team. Notably, Jeff Russell has a significantly higher average sales amount. This discrepancy suggests that Jeff Russell may have particularly effective sales tactics or a higher level of experience. To improve overall sales performance, it might be beneficial to analyze Jeff's methods and consider implementing training programs to help other employees achieve similar results. Additionally, introducing incentives could motivate the sales team to enhance their performance.

**Sales Trends Over Time:** The sales trends over time highlight fluctuations in sales performance. February 4th shows a peak in sales, which could be due to specific marketing efforts, promotions, or external factors influencing customer behavior. The following days show a decline, suggesting a need for consistent strategies to maintain high sales levels. Further analysis could help identify the causes of these fluctuations and assist in developing strategies to achieve more stable sales growth.

