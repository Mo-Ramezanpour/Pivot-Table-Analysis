# Pivot-Table-Analysis
# This code snippet utilizes the pandas and numpy libraries to analyze employee salary data from an Excel file named 'Employees.xlsx' #
1. Initially, it reads the data into a DataFrame named df using pd.read_excel.
2. Then, it creates a pivot table to aggregate the 'Annual Salary' by 'Job Title' using three aggregation functions: sum, mean, and count.
The pivot table is sorted in descending order based on the total annual salary sum for each job title.
3. Following the creation of the pivot table, the code calculates the total salary cost by summing the 'Annual Salary' column.
4. It then adds a new column to the pivot table, representing each job title's percentage contribution to the total salary cost. This percentage is computed by dividing the sum of each job title's annual salary by the total salary cost and multiplying by 100.
5. The final step formats the pivot table, ensuring numerical values have commas as thousand separators and percentages are displayed with two decimal places. The resulting table provides a comprehensive view of salary distribution and the relative financial impact of each job title within the organization.






