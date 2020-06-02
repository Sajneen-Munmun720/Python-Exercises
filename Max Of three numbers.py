def max(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z

first_number=int(input("Enter first number: "))
second_number=int(input("Enter second number: "))
third_number=int(input("Enter third number: "))
result=max(first_number,second_number,third_number)
print("Maximum number is: ",result)