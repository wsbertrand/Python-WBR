#%% create a window with sum, susbtraction and multiplication and the results will be shown for the selected options in the window

from tkinter import Tk

main = tk.Tk()
a = 10
b = 15
Var1 = tk.IntVar()
Var2 = tk.IntVar()
Var3 = tk.IntVar()
B1 = tk.Checkbutton(top, text = "Sum", variable = Var1)
B2 = tk.Checkbutton(top, text = "Multiply", variable = Var2)
B3 = tk.Checkbutton(top, text = "Substract", variable = Var3)
B1.pack()
B2.pack()
B3.pack()
main.mainloop

if Var1.get() == 1:
    print(a+b)

if Var2.get() == 1:
    print(a*b)

if Var3.get() == 1:
    print(a-b)

#%% program that convert EUR/RUB or RUB/EUR
#Ask user what kind of exchange he is looking and the amount
#Print the received amount
import tkinter as tk
R = 88
E = 0.11
top = tk.Tk()
amount = tk.IntVar()
option = tk.IntVar()

#Entry and Label
F = tk.Label(top, text="Please enter the amount you want to convert", justify="left").pack()
A = tk.Entry(top, textvariable = amount).pack()
L = tk.Label(top, text="What is the currency you want to convert?", justify="left").pack()



#Radio Button
B1 = tk.Radiobutton (top, text = "EUR", variable=option, value=1).pack()
B2 = tk.Radiobutton (top, text = "RUB", variable=option, value=2).pack()

#Button to calculate and close window
C = tk.Button(top,text = "Calculate", bg="green", command= top.destroy).pack()


#Closing the first window with the saved variables
top.mainloop()

#Calculation
if option.get()==1:
    result = tk.Tk()
    L = tk.Label(result, text=str(amount.get()*R), justify="left").pack()
    result.mainloop()
elif option.get() ==2:
    result = tk.Tk()
    L = tk.Label(result, text=str(amount.get()*E), justify="left").pack()
    result.mainloop()

#Oreal, show to the user which country I want to select / + radiobutton
#Then open a new windows with all the region / + Check Button to pick




