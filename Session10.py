#%% Program which multiplies all the items in a list
mylist = [1,2,4,5]
multi = 1
for i in mylist:
    multi = i * multi
print(multi)

#%% Program to remove duplicates values from a list
mylist = [1,1,2,2,3,3,4,4,5,5]
list2 = []
for i in mylist:
    if i not in list2:
    list2.append(i)
print((list2))

#%% set delete duplicate
mylist = [1,1,2,2,3,3,4,4,5,5]
solution = set(mylist)
print(solution)

#%% Program to get the total income for your top 20% of clients when you receive a list with all sales
sales = [140,200,160,300,300,20,5,10,1000,100]
sales.sort(reverse=True)
taille = len(sales)
position = taille * 0.2
top = sales[:int(position)]
final = sum(top)
print(final)

#%% Rewrite with a function with two arguments: sales & percentages of top sales
sales = [140,200,160,300,300,20,5,10,1000,100]
def functop (sales,percentage):
    sales.sort(reverse=True)
    newper = percentage // 10
    percentage = sales[:newper]
    final = sum(percentage)
    print(final)
functop(sales,30)

#%% Program to check if there is negative value in a given list
mylist = [-1, 2, 3, -4]
for number in mylist:
    if number > 1:
        print("There is a negative number in my list")
        break

#%% Program to find maximum and mini in a set
my_set = {1,2,3,4,5}
minimum = min(my_set)
maximum = max(my_set)
print("The min of my set is ", minimum)
print("The max of my set is ", maximum)

#%% Program to remove a concrete item from a set if it is present in the set
my_set = {"Tom","Paul","Tom","Will","John"}
def kill (delete,my_set):
    if delete in my_set:
        my_set.remove(delete)
    print(my_set)
kill("Tom",my_set)

#%%
a = {1,2,3,4}
b = {8,0,2,4}
c = {3,4,"John", 1000}

aux = a.union(b)
aux.intersection(c)
