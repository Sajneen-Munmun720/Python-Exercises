def sum_list(numbers):
    sum_numbers=0
    for items in numbers:
        sum_numbers += items
    return sum_numbers
print("Sum of list is:",sum_list((2,3,4,6,7)))