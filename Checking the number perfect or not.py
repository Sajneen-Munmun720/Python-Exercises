def perfect_number(number):
    total=0
    for items in range(1,number):
        if number%items==0:
            total +=items
    return total==number
Number=int(input("Enter a number:" ))
result=perfect_number(Number)
print(result)