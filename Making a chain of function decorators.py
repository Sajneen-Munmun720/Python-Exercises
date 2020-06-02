def division(x,y):
    print(x/y)

def new_division(function):
    def inner(x,y):
        if x<y:
            x,y=y,x
        return function(x,y)
    return inner
x=int(input("Enter a number:"))
y=int(input("Enter another number:"))
div=new_division(division)
div(x,y)