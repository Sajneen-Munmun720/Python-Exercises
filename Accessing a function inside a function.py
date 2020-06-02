def outer():
    a=10
    def inner():
        b=11
        result=a*b
        return result
    return inner
s=outer()
print(s())