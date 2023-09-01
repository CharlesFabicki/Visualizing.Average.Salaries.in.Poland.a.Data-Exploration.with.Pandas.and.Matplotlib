import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the file into a Pandas DataFrame
file_name = "zus-data.csv"  # Replace with the actual file name and path if needed
data = pd.read_csv(file_name)

# Split the data into three time ranges
data_1950_1989 = data[data['Year'].between(1950, 1987)]
data_1990_1994 = data[data['Year'].between(1988, 1994)]
data_1995_2022 = data[data['Year'].between(1995, 2022)]

# Create three separate bar charts for different time ranges
plt.figure(figsize=(18, 10))  # Adjust the figure width for the first chart

# Chart 1: Year from 1950 to 1989
plt.subplot(3, 1, 1)
bars1 = plt.bar(data_1950_1989['Year'], data_1950_1989['Monthly Salary'], color='blue')
plt.title('Monthly Salary: 1950-1989')

# Add value labels to bars1 with increased spacing
for bar in bars1:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 200, str(int(bar.get_height())),
             ha='center', va='bottom', fontsize=8, color='black')

# Adjust subplot spacing to make the first chart wider
plt.subplots_adjust(top=0.88, hspace=0.4)

# Chart 2: Year from 1990 to 1994
plt.subplot(3, 1, 2)
bars2 = plt.bar(data_1990_1994['Year'], data_1990_1994['Monthly Salary'], color='green')
plt.title('Monthly Salary: 1990-1994')

# Add value labels to bars2
for bar in bars2:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 100, str(int(bar.get_height())),
             ha='center', va='bottom', fontsize=8, color='black')

plt.ylim(0, 6000000)  # Set the upper limit to 8 million
plt.yticks([0, 1000000, 2000000, 3000000, 4000000, 5000000, 6000000],
           ['0', '1M', '2M', '3M', '4M', '5M', '6M'])

# Chart 3: Year from 1995 to 2022
plt.subplot(3, 1, 3)
bars3 = plt.bar(data_1995_2022['Year'], data_1995_2022['Monthly Salary'], color='orange')
plt.title('Monthly Salary: 1995-2022')
plt.xlabel('Year')

# Set y-axis limits for the third chart
plt.ylim(0, 7000)

# Add value labels to bars3
for bar in bars3:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 100, str(int(bar.get_height())),
             ha='center', va='bottom', fontsize=8, color='black')


plt.tight_layout()
plt.show()

