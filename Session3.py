#%% Get this text "elloBbH"
text = "Hello Bob"
text[1:5] + text[4:9:2] + text[0]

#%% Exercice 1 Program that calculate the lenght of a string
text_variable = "magic"
len(text_variable)

#%% Exercise 2 Program to replace the first letter by $ in the remaining text
def replace(s):
    first = s[0]
    modify = s[1:].replace(first, "$")
    print(first + modify)
replace('expenses')

#%% Exercise 3 Program to lower case the first 6 characters
text_variable = "TodaY is very sunny"
text_variable = text_variable[:6].lower() + text_variable[6:]
print(text_variable)

#%% DTV7 Program that reverse the following wrong text
sentence = "sihT si ym esrever esicrexe" #Reversed String
stringlenght = len(sentence) #Compute lenght of the string
slicedstring = sentence[stringlenght::-1] #Slice

#Now that the words are in order we need to
#reverse the list to have the sentence in order

word_list = slicedstring.split()  #new variable to store the split
reversed_list = reversed(word_list) #new variable to store the reverse list
reversed_sentence = " ".join(reversed_list) #new variable to store the join reverse list
print(reversed_sentence) #Here is the result

#%% Exercise 5 Find the plane from Madrid
f1 = "MAD-BCN"
f2 = "MAD-SEV"
f3 = "MAD-LIS"
f4 = "LON-MAD"

def find(s):
    first = s[:3]
        if first == "MAD":
            print("Plane from Madrid")
        else:
            print("Plane from somewhere else")
find(f1)

#Solution less complicated
flights = f1 + f2 + f3 + f4
flights.count("MAD")







