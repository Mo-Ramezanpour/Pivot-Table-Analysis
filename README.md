# Analysis With Pivot Table

**This code snippet utilizes the pandas and numpy libraries to analyze employee salary data**

**1. Data Loading and Duplicate Handling**
The code begins by loading the employee data from an Excel file (Employees.xlsx) into a Pandas DataFrame. This is done using the pd.read_excel() function, which reads the data into a tabular format for easy manipulation. After loading the data, the code checks for duplicate rows using the df.duplicated() method. Duplicates are identified and printed to the console, and then removed using df.drop_duplicates(). This step ensures the dataset is clean and free from redundant entries, which is crucial for accurate analysis. Handling duplicates is particularly important in datasets like this, where repeated entries (e.g., the same employee listed twice) could skew results.

**2. Pivot Table Creation and Salary Analysis**
The core functionality of the code revolves around creating pivot tables to analyze employee salaries. Using the df.pivot_table() method, the code groups the data by specific columns (e.g., Job Title, Department, Country) and calculates aggregate statistics such as the sum, mean, and count of salaries. For example, the pivot table for Job Title shows the total salary, average salary, and number of employees for each role. Additionally, the code calculates the percentage contribution of each group (e.g., job title, department, country) to the total salary cost. This is done by dividing the sum of salaries for each group by the total salary cost and multiplying by 100. These pivot tables provide a comprehensive view of how salaries are distributed across different dimensions, enabling insights into cost allocation and organizational structure.

**3. Formatting and Output**
The final part of the code focuses on formatting the results for better readability and usability. The applymap() function is used to format numeric values with commas as thousand separators (e.g., 100000 becomes 100,000). For the percentage column, the apply() function is used to format the values as percentages with two decimal places (e.g., 23.64 becomes 23.64%). The formatted results are then displayed in the console. To handle large outputs that might be truncated, the code includes options to export the results to text or CSV files. This ensures that the full analysis can be reviewed in a more accessible format, such as a spreadsheet or text editor. The code also includes a pagination option to print the results in smaller chunks, making it easier to navigate through large datasets.

**Summary**
In summary, this code performs a comprehensive analysis of employee salary data by cleaning the dataset, creating pivot tables to summarize key metrics, and formatting the results for easy interpretation. It provides valuable insights into salary distribution across job titles, departments, and countries, while also ensuring the output is user-friendly and accessible.

**Happy Coding!**






