import pandas as pd
df = pd.read_csv('Chipo.csv')

#Price of each item when only 1 item is bought
aux =df.loc[df.quantity == 1,:].loc[:,["item_name", "item_price"]]
sol1 = aux.drop_duplicates(subset = ["item_name"])

#Sort by the name of the item
sol1.sort_values(by=["item_price"], ascending = 0)

#%%How many time Veggie salad as been ordered
import pandas as pd
df = pd.read_csv('Chipo.csv')
df.loc[df.item_name == "Veggie Salad Bowl",:]


#%%How many time ppl ordered more than one Canned Soda
import pandas as pd
df = pd.read_csv('Chipo.csv')
a = df.loc[df.quantity > 1,:]
a.loc[df.item_name == "Canned Soda",:]

#%% Show the 5 most expensive dishes
import pandas as pd
df = pd.read_csv('Chipo.csv')
a = df.sort_values(by=["item_price"], ascending = 0)
a.head(5)

#%% Show the total number of unit sold
import pandas as pd
df = pd.read_csv('Chipo.csv')
df.quantity.sum()


#%% Show the total income for the canned soda
import pandas as pd
df = pd.read_csv('Chipo.csv')
a = df.loc[df.item_name == "Canned Soda",:]