import math

math.factorial(5)

#%% Exercice 1
a = input("Give me a number")
a = float(a)
b = input("Give me another number")
b = float(b)

sum1 = a + b
multiply = a * b
print(sum1, multiply)



#%% Exercise 2
#We take a loan in a bank office to buy a Mercedes Benz with a simple
#interest ratio of 4% for 1 year.


time = 8/12
interest = 0.04
price = input("What's the amount of your car?")
price = float(price)
future_value = time * interest * price + price
print(future_value)

#%% Exercise 3
#Your company has a debt of € 50k. You compare different deposits and the
#most profitable one is a deposit at Santander Bank with a 6% annual
#compound interest . How much money should you invest in that deposit today
#to get € 50k in N years?

i = 0.06
fv = 50000
n = input("In how many years do you want to get the money?")
n = float(n)
p = (fv/(1 + i)**n)

print("If you want to obtain", fv, "euros in", n, "years, you should invest today", p, "euros")



