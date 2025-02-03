# Function 1: Write a simple Hello World program
# This function should print "Hello, World!" to the screen.
def hello_world():
    print (f"Hello, World! ")

# Function 2: Get input and output with different variable types
# This function should prompt the user for their name (string), age (int), and height (float),
# and then print them back in a formatted message.
def input_output():
    # TODO: Implement this function
    name= input ("Enter your name: ")
    age= int(input ("Enter your age: "))
    height= float(input ("Enter your height: "))
    print (f"Hello, {name}!\nYou are {age} years old.\nYour height is {height} meters.")