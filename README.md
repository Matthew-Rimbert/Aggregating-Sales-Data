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

![Total Sales by Region](https://github.com/Matthew-Rimbert/Aggregating-Sales-Data/assets/5c5007db-026a-4f74-aa62-3626fdafe14f)

### Average Sales per Employee:
This table shows the average sales per employee.

| Empname      | Total |
|--------------|-------|
| Jane Boorman | 60.5  |
| Jeff Russell | 243.0 |
| Maya Silver  | 94.0  |
| Tom Heints   | 89.5  |

![Average Sales per Employee](https://github.com/Matthew-Rimbert/Aggregating-Sales-Data/assets/943f8d24-acdb-4074-88b2-8ecafcab89d8)

### Sales Trends Over Time:
This table shows the total sales over time, helping to identify trends in sales.

| Date       | Total |
|------------|-------|
| 2022-02-04 | 340.0 |
| 2022-02-05 | 195.0 |
| 2022-02-06 | 196.0 |

![Sales Trends Over Time](https://github.com/Matthew-Rimbert/Aggregating-Sales-Data/assets/274b30bb-00f9-47c7-8ac4-706a5259fc2d)

## 📈 Summary
This project provides a comprehensive analysis of sales data. By merging multiple datasets, it offers insights into sales performance by region, average sales per employee, and sales trends over time. The visualizations created using matplotlib and seaborn help in understanding the data better and making informed decisions based on the analysis.

