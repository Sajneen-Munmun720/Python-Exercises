def testing_number(number):
        if number in range(10,20):
            print("Number is in the range")
        else:
            print("Number is not in the range")
        return testing_number
Number=int(input("Enter a number:"))
result=testing_number((Number))