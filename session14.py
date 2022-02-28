# df.columns show all columns names
# df.weight show a column
# df["Q"] = [130,135] add a column
# df.shape gives dimensions
# df.data.head(7) 7 first rows
# df.data.tail(7) 7 last rows
# df.describe() numerical analysis of the data set
# df.loc[:,["row", "columns"]] used to extract rows and columns when we use name
# : means all
# df.iloc["row, "columns"] used to extract rows and columns when we use the position
# df.iloc[:,5,8] extracting all the rows and the column for 5 to 7
# df.rename(columns = {"old name":"new name"}, inplace = True)
# df.drop_duplicates(subset = columns list, keep = "first") erase the duplicated rows
# df.drop(list with column names, axis = 1) erase column
# df.dropna() rows with NaN values will be erased
# df.dropna(how = "all") only rows with all the elements Na will be erased
# df.dropna(axis = 1) #axis = 1 (columns) or 0  (rows) / how = "any" or "all"

#%%
import pandas as pd
df = pd.read_csv('Chipo.csv')
#Q1 First 10 entries
df.head(10)
#Q2 dimensensions
df.shape
#Q3 Number of columns
df.columns
#Q4 most repeated value
df.item_name.value_counts()
#Q5 how many time is appearing
df.describe
