# Visualizing.Average.Salaries.in.Poland.a.Data-Exploration.with.Pandas.and.Matplotlib

## Monthly Salary Analysis
This Python script is designed to load data from a CSV file containing information about monthly salaries over a range of years and create three separate bar charts to visualize the data for different time ranges.

## Prerequisites
Before running the script, ensure that you have the following dependencies installed:

Python 3.x
Pandas library
Matplotlib library
You can install these libraries using pip:

```bash
pip install pandas matplotlib
```
## Usage
Clone this repository or download the script.
Place your CSV data file (replace "zus-data.csv" in the script) in the same directory as the script or provide the correct file path.
Run the script using Python:
```bash
python Monthly Salary.py
```
The script will generate three bar charts showing the monthly salary data for the specified time ranges.

### Script Explanation
### Loading Data
The script uses the Pandas library to load data from the specified CSV file into a DataFrame.

file_name = "zus-data.csv"  # Replace with the actual file name and path if needed
data = pd.read_csv(file_name)

Monthly Salary Analysis
This Python script is designed to load data from a CSV file containing information about monthly salaries over a range of years and create three separate bar charts to visualize the data for different time ranges.

Prerequisites
Before running the script, ensure that you have the following dependencies installed:

Python 3.x
Pandas library
Matplotlib library
You can install these libraries using pip:

bash
Copy code
pip install pandas matplotlib
Usage
Clone this repository or download the script.
Place your CSV data file (replace "zus-data.csv" in the script) in the same directory as the script or provide the correct file path.
Run the script using Python:
bash
Copy code
python your_script_name.py
The script will generate three bar charts showing the monthly salary data for the specified time ranges.

Script Explanation
Loading Data
The script uses the Pandas library to load data from the specified CSV file into a DataFrame.

python
Copy code
file_name = "zus-data.csv"  # Replace with the actual file name and path if needed
data = pd.read_csv(file_name)
Data Splitting
The data is split into three time ranges based on the 'Year' column:

1950-1989
1990-1994
1995-2022
data_1950_1989 = data[data['Year'].between(1950, 1987)]
data_1990_1994 = data[data['Year'].between(1988, 1994)]
data_1995_2022 = data[data['Year'].between(1995, 2022)]

### Creating Bar Charts
Three separate bar charts are created to visualize the monthly salary data for each time range.

1950-1989

The first chart is for the years 1950 to 1989.
The figure size is adjusted for this chart.
Value labels are added to the bars.
1990-1994

The second chart is for the years 1990 to 1994.
The y-axis limit and tick labels are customized for this chart.
Value labels are added to the bars.
1995-2022

The third chart is for the years 1995 to 2022.
Value labels are added to the bars.
Displaying Charts
The plt.tight_layout() function ensures proper spacing between subplots, and plt.show() displays the charts.

## Customize the Script
Replace "zus-data.csv" with the path to your own CSV file if it's located in a different directory.
Customize the chart titles, axis labels, colors, and other parameters as needed.
Feel free to modify the script to suit your specific data and visualization requirements.