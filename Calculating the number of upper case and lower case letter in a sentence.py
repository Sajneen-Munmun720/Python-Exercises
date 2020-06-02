def case_testing(string):
    d={"Upper_case":0,"Lower_case":0}
    for items in string:
        if items.isupper():
            d["Upper_case"]+=1
        elif items.islower():
            d["Lower_case"]+=1
        else:
            pass
    print("Number of upper case is:",d["Upper_case"])
    print("Number of lower case is:", d["Lower_case"])
sentence=input("Enter a Sentence:")
case_letters=case_testing(sentence)