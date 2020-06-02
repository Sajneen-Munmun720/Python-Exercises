def pascal_triangle(n):
    x=[1]
    y=[0]
    for items in range(max(n,0)):
        print(x)
        x=[a+b for a,b in zip(x+y,y+x)]
    return n>=1
row=int(input("Enter a number:"))
result=pascal_triangle(row)