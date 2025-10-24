# Goal: show how input works, type conversion, and basic math output.


print("Welcome! We'll do some math.\n")

# get user name

name = input("What's your name? ") #ask for their name
print(f"Hi, {name}! Let's do some math.\n")
print("Hi, " + name + "! Let's do some math.\n")
# is your output

# ask for your birthday
# ask for your favorite food
# ask for two numbers

# create output sentences using f strings
# using these three input variables

birthday = input("What is your birthday?")
favorite_food = input("What is your favorite food?")
two_numbers = input("Choose two numbers")
print(f"That's interesting.\n")
print(f"I also love {favorite_food}\n")
print(f"{two_numbers} are interesting numbers.\n")

# ask for two numbers
num1 = int(input("Enter a number: ")) # input is string
num2 = int(input("Enter another number: ")) # input is string

print(num1 + num2)

# Get two numbers from the user and ask for their name to personalize the experience
















# Student  notes (say out loud):

        # “input() is always text. That’s why we convert.”

        # “float() lets us do decimal math; int() is only whole numbers.”

        # “Division by zero crashes programs—so we check first.”

        # “{value:.2f} rounds to 2 decimals right in the f-string.”

# Common pitfalls to point out:

        # Forgetting to cast → "3" + "4" becomes "34" (string concatenation)

        # Using ^ for exponent (Python uses **)

        # Missing quotes around string literals

        # Forgetting the f in f-strings