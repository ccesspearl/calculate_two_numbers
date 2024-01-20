# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

def product_or_sum():
    first = (int(input("Enter first number: ")))
    second = (int(input("Enter second number: ")))

    product = first * second 
    total_sum = first + second 
    
    if product <= 1000:
        print("The result is ", product) 
    else: 
        print("The result is ",total_sum) 

product_or_sum()
