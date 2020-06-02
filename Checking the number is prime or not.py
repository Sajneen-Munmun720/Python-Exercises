def testing_prime(number):
    if number==1:
        return("Not prime")
    elif number==2:
        return("2 is a prime number")
    else:
        for items in range(2,number):
            if (number % items==0):
                return("The number is not a prime number")
            else:
                return("The number is a prime number")
Number=int(input("Enter a number:"))
result=testing_prime(Number)
print(result)
