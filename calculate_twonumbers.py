# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# Creating function 
def product_or_sum():
    first = (int(input("Enter first number: "))) # Letting user input the first number 
    second = (int(input("Enter second number: "))) # Letting user input the second number 

    product = first * second # Multiplying the two numbers 
    total_sum = first + second # Adding the two numbers 
    
    # Condition Statement 
    if product <= 1000: 
        print("The result is ", product) # The result will return the product if the product is equal or lower than 1000. 
    else: 
        print("The result is ", total_sum) # The result will return the sum of the product exceeded 1000. 

product_or_sum()
