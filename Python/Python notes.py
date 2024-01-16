"Comments"
# + words (Explanations, will not be executed)
EX: # i am nonsense



"Variables"
variable = number
EX: age = 10
    age, gender, height = 10, "male", 190 # strict order
    age, gender = gender = age # change the value of variables



"Constants"
variable = value # variables all uppercase letters or with underscores
EX: AGE = 10
    MY_AGE = 10



"Strings"
variable = "text" # immutable
EX: age = "guess"



"String methods" # change string forms



"Combinging numbers and strings"
EX: age = 10
    name = "Alex"
    Sentence = f"My name is {name}. I am {age} years old."



"Escape characters" # insert special characters into the string
\\ # blackslash
\" # quote
\n # new line
\t # horizental tab

raw string = r"a\b\c\d" # use "r" to tell the computer do not deal with escape character



"Numbers"
EX: 
5 + 2 # 7
5 - 2 # 3
5 * 2 # 25
5 / 2 # 2.5
5 // 2 # 2   return the largest number not greater than the result
5 ** 2 # 25
5 % 2 # 1    return the remainder of a division

round = round(3.1415926, 2)   # 3.14
integer = int(5.7)            # 5
float = float(7)              # 7.0
absolute = abs(-5.5)          # 5.5



"Booleans"
==  # equal
!=  # not equal
>   # greater than
<   # less than
>=  # greater than or equal to 
<=  # less than or equal to

and # all must be true
or  # one true is true



"Loops"
format:
# use "for" whrn you know how many times
for i in range(x)  # x is the repeat times
    print("Hello") # start with tab for all the lines that needed to be repeated
# use "while" when you do not know how many times
ticket = 10
while tickets > 0
    print("Sold!")
    ticket -= 1    # this is the condition that stops an infinite loop
print("Sold out!") # this line is the expected result that should not be in a loop



"Conditions"
format:
age = 14

if age >= 65:
    print("Senior")
elif age >= 18:
    print("Adult")
elif age >= 4:
    print("Children")
else;
    print("Infant")



"Lists"
EX:
number = [1, 2, 3, 4, 5]
me = ["Alex", "tall", "glasses"] # [] is in order and mutable

EX(Slicing):
number = [1, 2, 3, 4, 5]
my_number = number[1:4]  # start with index 1 and ends with index 4 but not include index 4
                         # result: 2, 3, 4



"Dictionary"
EX:
my_phone = {"brand": "Apple", "model": "13 pro max", "year": 2021}
