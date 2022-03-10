from plotnine.data import diamonds
from plotnine import *

ggplot(aes(x = "carat", y = "price"), diamonds) + geom_point() + ggtitle("Carat VS Price")
ggplot(aes(x = "price"), diamonds) + geom_histogram() + ggtitle("Carat VS Price")
diamonds.head(5)

#%%
import seaborn as sns
from plotnine import *
tips = sns.load_dataset("tips")
tips.head(5)
#Create a scatterplot showing bill & tips
ggplot(aes(x = "total_bill", y = "tip"), tips) + geom_point() + ggtitle("Bills VS Tips")

#%%Same Graph showing also info about the gender
import seaborn as sns
from plotnine import *
tips = sns.load_dataset("tips")
ggplot(aes(x = "total_bill", y = "tip", color = "sex"), tips) + geom_point() + ggtitle("Bills VS Tips")

#Create a barplot with the number of dinners and lunches per day
ggplot(aes(x = "time", tips) + geom_bar() + ggtitle("Diner and Lunch Per Day") + facet_wrap("day")





