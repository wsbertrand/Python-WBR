# %% Clients per Nationality

import pandas as pd

df = pd.read_excel(r'C:\Users\Williams\Desktop\Python-WBR\Telco_and_job_data.xlsx', sheet_name="Telco")
nationality = df.value_counts("Nationality")
print(nationality)

# %%  Candidates per Nationality
import pandas as pd

df = pd.read_excel(r'C:\Users\Williams\Desktop\Python-WBR\Telco_and_job_data.xlsx', sheet_name="Job")
nationality = df.value_counts("Nationality")
print(nationality)

# %% Challenge RWD1 Script where a Excel File with several sheets is created as follow
# First sheet names "numeric" is printed a numerical summary of the numerical variables
# One sheet is created for each factor variable showing the frequency for each value
import pandas as pd

df = pd.read_csv(r'/Chipo data 2_Usar.csv')
des = df.describe()
order_id = df.value_counts("order_id")
quantity = df.value_counts("quantity")
turnover = df.value_counts("item_price")
print(order_id,quantity,turnover)

#df.to_excel(r'C:\Users\Williams\Desktop\Python-WBR\numeric.xlsx')

#%%Correction
df = pd.read_csv(r'/Chipo data 2_Usar.csv')
sol1 = df.describe()
sol2 = df.item_name.value_counts()

sol1.to.excel('Numerical analysis.xlsx')
sol2.to.excel('Item name frequencies.xlsx')


