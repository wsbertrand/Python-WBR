#%% program that writes after the name of each one member of your team
# "is the best" if more than 6, "second best"
import urllib.request

for name in ["Williams", "Blanca", "Aladin", "John", "Charles"]:
    if len(name) > 6:
        print(name + " is the best")
    else:
        print(name + " is the second best")

#%% Program that open 4 important European newspapers in your broswer with a for loop
import webbrowser
newspaper = ["https://www.ft.com", "https://www.bbc.com", "https://www.nytimes.com", "https://www.washingtonpost.com"]
for link in newspaper:
    webbrowser.open(link)

#%% Program yo get the fibonacci series between 0 and 100
X = int(input("How many element do you want to have in the list?"))
start = [0,1]
if X > 2:
    for i in range(2,X):
        nextone = start [i-1] + start [i-2]
        start.append(nextone)
print(start)

#%% Program which ask for a number and show multiplication table
N = int(input("What number table would you like to see?"))
for i in range(0, 11, 1):
    print(N, 'x', i, '=', N*i)

#%% The age of a dog in human's year 2 hum
youth = 10.5
old = 4
N = int(input("What is the age of the human you want to put in dog years?"))
if N > 2:
    age = youth * 2 + old * (N-2)
    print(age)
else:
    print(N*youth)









