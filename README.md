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
- **Orders**
- **Order Details**
- **Employees**
- **Locations**

## 🖼️ Example Outputs

### Aggregated Sales Data:
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
| Region | Total |
|--------|-------|
| East   | 367.0 |
| West   | 364.0 |

![Total Sales by Region](https://github.com/user-attachments/assets/5c5007db-026a-4f74-aa62-3626fdafe14f)
)

### Average Sales per Employee:
| Empname      | Total |
|--------------|-------|
| Jane Boorman | 60.5  |
| Jeff Russell | 243.0 |
| Maya Silver  | 94.0  |
| Tom Heints   | 89.5  |

![Average Sales per Employee](https://github.com/user-attachments/assets/943f8d24-acdb-4074-88b2-8ecafcab89d8)


### Sales Trends Over Time:
| Date       | Total |
|------------|-------|
| 2022-02-04 | 340.0 |
| 2022-02-05 | 195.0 |
| 2022-02-06 | 196.0 |

![Sales Trends Over Time](https://github.com/user-attachments/assets/274b30bb-00f9-47c7-8ac4-706a5259fc2d)


## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## 📜 License
This project is licensed under the MIT License.
