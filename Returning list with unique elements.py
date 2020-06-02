def unique_list(list):
    n=[]
    for items in list:
        if items not in n:
            n.append(items)
    return n
print(unique_list([11,2,3,11,5,5,9,40,40]))







































