#%% Program that asks for the name to the user. If the name is your name, congrats. If not let him know that is not your name.
name = "pablo"
question = input("What is my name?").lower()
if question == name:
    print("Congratulations")
else:
    print("This is not my name")

#%%
brand_list = ["APPLE", "HP", "DELL", "ACER", "ASUS", "MICROSOFT", "LENOVO"]

while True:
    laptop_brand = input("What type of laptop brand are you looking for? ")
    laptop_brand = laptop_brand.upper()
    if laptop_brand not in brand_list:
        print("This is not a valid laptop provider")
        continue
    else:
        print(laptop_brand,"is a good choice!")
        break
#%% The age of a dog in human's year 2 hum
youth = 10.5
old = 4
N = int(input("What is the age of the human you want to put in dog years?"))
if N > 2:
    age = youth * 2 + old * (N-2)
    print(age)
else:
    print(N*youth)

#%% Program which ask for a number and show multiplication table
N = int(input("What number table would you like to see?"))
for i in range(0, 11, 1):
    print(N, 'x', i, '=', N*i)

#%% Amount of ingredients per meal
pizza_recipe = "You will need 100gr of floors, 80gr of cheese and 100gr of tomato sauce"
pasta_recipe = "You'll need 100gr of pasta, 50gr of tomato sauce, 50gr of minced meat and 20gr of cheese"
salad_recipe = "You'll need 200gr of lettuce, 100gr of chicken and 30ml of dressing"
error = "Sorry mate,this recipe is not in the book"

question = input("What do you want to cook today ? Pizza, Pasta or Salad?").lower()
if question == "pizza":
    print(pizza_recipe)
elif question == "pasta":
    print(pasta_recipe)
elif question == "salad":
    print(salad_recipe)
else:
    print(error)






