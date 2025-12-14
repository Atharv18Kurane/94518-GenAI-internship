"""1.
Upload a CSV file. Input a SQL query from user and execute it on the CSV
data (as dataframe ). Display result on the"""

import pandas as pd 
import pandasql as ps 

filepath="emp_hdr.csv"
df=pd.read_csv(filepath)
print("Dataframe Column Types:")
print(df.dtypes)
print("\nEmp Data:")
print(df)

query= "SELECT job,SUM(sal) total FROM data GROUP BY job"
result=ps.sqldf(query,{"data":df})
print("\nQuery result:")
print(result)