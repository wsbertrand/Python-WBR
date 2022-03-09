#%% Create a report and store it in an Excel
#First tab: the product distribution for the Telco Client
#Second tab: product distribution per nationality for the Client

import pandas as pd
telco = pd.read_excel("Telco_and_job_data.xlsx", sheet_name= "Telco")
job = pd.read_excel("Telco_and_job_data.xlsx", sheet_name= "Job")

#Number of clients by products
telco.shape
telco.Product.value_counts()

#Number of clients by products and nationality
pd.crosstab(telco.Product, telco.Nationality)

#Average ARPU per product and nationality for the Telco CLients
a = telco.groupby(by= ["Product","Nationality"], as_index=False).mean()
a.sort_values(by = "ARPU", ascending=False)

#Average GMAT score of the candidates
# Per Gender and studies
job.groupby(by= ["Gender","Degree"], as_index=False).mean()

#Best GMAT score of the candidates
# Per Gender and studies
job.groupby(by= ["Gender","Degree"], as_index=False).max()


#Best candidates in term og GMAT score per gender
job.groupby(by= ["Gender"], as_index=False).max()




