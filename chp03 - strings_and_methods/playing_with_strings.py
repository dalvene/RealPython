#  This is a comment

phrase = "Hello, world"

print(phrase) # this line displays "Hello, world"


long_string = """This is a long
string that spans over multiple lines"""

print(long_string)


# string length code
my_string = 'birthday'
string_length = len(my_string)
print(string_length)

# Concatenate some strings
string1 = "Hello,"
string2 = "world!"
print(string1, string2)

# index strings
mystring = "bazinga"
print(mystring[2:6])

# string method
loud_voice = "Can you hear me yet?"
print(loud_voice.upper())

# Text input
user_input = input("Hey, what's up? ")
print("You said: ", user_input)

# Testing object methods
my_string = "kerfuffle"
my_string.upper()

# format strings
name = "Zaphod"
num_heads = 2
num_arms = 3
print("{} has {} heads and {} arms".format(name, num_heads, num_arms))

print(f"{name} has {num_heads} heads and {num_heads+1} arms")
