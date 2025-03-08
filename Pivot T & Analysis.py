import numpy as np
import pandas as pd

# Load the Excel file
df = pd.read_excel('Employees.xlsx')

# Check for duplicate rows
duplicates = df[df.duplicated()]
print(f"Number of duplicate rows: {len(duplicates)}")
if len(duplicates) > 0:
    print("Duplicate rows:")
    print(duplicates)

# Remove duplicates (if any)
df = df.drop_duplicates()

# Salary Analysis by Job Title
pivot_job_title = df.pivot_table(values='Annual Salary', index='Job Title',
                                 aggfunc=[np.sum, np.mean, 'count']).sort_values(
    ('sum', 'Annual Salary'), ascending=False)

# Calculate total salary cost
total_salary = pivot_job_title[('sum', 'Annual Salary')].sum()

# Add percentage of total salary cost
pivot_job_title[('%', 'Annual Salary')] = pivot_job_title[('sum', 'Annual Salary')] / total_salary * 100

# Format the pivot table
pivot_job_title_formatted = pivot_job_title.applymap(lambda x: f"{x:,.0f}" if isinstance(x, (int, float)) else x)
pivot_job_title_formatted[('%', 'Annual Salary')] = pivot_job_title[('%', 'Annual Salary')].apply(lambda x: f"{x:.2f}%")

# Salary Analysis by Department
pivot_department = df.pivot_table(values='Annual Salary', index='Department',
                                  aggfunc=[np.sum, np.mean, 'count']).sort_values(
    ('sum', 'Annual Salary'), ascending=False)

# Add percentage of total salary cost
pivot_department[('%', 'Annual Salary')] = pivot_department[('sum', 'Annual Salary')] / total_salary * 100

# Format the pivot table
pivot_department_formatted = pivot_department.applymap(lambda x: f"{x:,.0f}" if isinstance(x, (int, float)) else x)
pivot_department_formatted[('%', 'Annual Salary')] = pivot_department[('%', 'Annual Salary')].apply(lambda x: f"{x:.2f}%")

# Salary Analysis by Country
pivot_country = df.pivot_table(values='Annual Salary', index='Country',
                               aggfunc=[np.sum, np.mean, 'count']).sort_values(
    ('sum', 'Annual Salary'), ascending=False)

# Add percentage of total salary cost
pivot_country[('%', 'Annual Salary')] = pivot_country[('sum', 'Annual Salary')] / total_salary * 100

# Format the pivot table
pivot_country_formatted = pivot_country.applymap(lambda x: f"{x:,.0f}" if isinstance(x, (int, float)) else x)
pivot_country_formatted[('%', 'Annual Salary')] = pivot_country[('%', 'Annual Salary')].apply(lambda x: f"{x:.2f}%")

# Age Distribution Analysis
pivot_age_job_title = df.pivot_table(values='Age', index='Job Title', aggfunc='mean').sort_values('Age', ascending=False)
pivot_age_department = df.pivot_table(values='Age', index='Department', aggfunc='mean').sort_values('Age', ascending=False)

# Hire Date Analysis
df['Hire Year'] = pd.to_datetime(df['Hire Date']).dt.year
pivot_hire_year = df.pivot_table(values='Full Name', index='Hire Year', aggfunc='count').rename(columns={'Full Name': 'Number of Hires'})

# Display Results
print("Salary Analysis by Job Title:")
print(pivot_job_title_formatted)
print("\nSalary Analysis by Department:")
print(pivot_department_formatted)
print("\nSalary Analysis by Country:")
print(pivot_country_formatted)
print("\nAverage Age by Job Title:")
print(pivot_age_job_title)
print("\nAverage Age by Department:")
print(pivot_age_department)
print("\nNumber of Hires by Year:")
print(pivot_hire_year)
