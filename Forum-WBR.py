#%% DTV5 Program to replace the first letter by $ in the remaining text
def replace(s):
    first = s[0] #Select the first letter
    modify = s[1:].replace(first, "$") #replace everything corresponding to the first except the first
    print(first + modify)
replace('management')


#%%

variable1 = "test"
print("This is a", variable1)