
import numpy as np
import pandas as pd


# Assuming df is already loaded with the Excel data
df = pd.read_excel('Employees.xlsx')

# Create the pivot table with sum, mean, and count
pivot = df.pivot_table(values='Annual Salary', index='Job Title',
                       aggfunc=[np.sum, np.mean, 'count']).sort_values(
    ('sum', 'Annual Salary'), ascending=False)

# Calculate the total salary cost
total_salary = pivot[('sum', 'Annual Salary')].sum()

# Add a column for the percentage of total salary cost
pivot[('%', 'Annual Salary')] = pivot[(
    'sum', 'Annual Salary')] / total_salary * 100

# Format the pivot table to have comma as thousand separator and percentage
c = pivot.applymap(lambda x: f"{x:,.0f}" if isinstance(x, (int, float)) else x)

c[('%', 'Annual Salary')] = pivot[('%', 'Annual Salary')].apply(
    lambda x: f"{x:.2f}%")

c
