def multiply_list(numbers):
    multiply_numbers=1
    for items in numbers:
        multiply_numbers *= items
    return multiply_numbers
print("Multiplication of list is:",multiply_list((2,3,4,6,7)))