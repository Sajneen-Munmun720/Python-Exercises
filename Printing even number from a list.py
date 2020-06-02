def even_list(list):
    even_number=[]
    for items in list:
        if items%2==0:
            even_number.append(items)
    return even_number
print(even_list([1,2,3,4,5,6,10,20,49,50]))