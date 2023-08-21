# Passing and Returning different data structures like list
def Read_list_values():
    print("Enter how many elements in the list you want")
    n=int(input("Enter value  "))
    l=[]
    for i in range(n):
        l.append(int(input("Enter {} value ".format(i))))

    return (l)
def max_list(l):
    max=l[0]
    for i in l:
        if max<i:
            max=i
    return max

def min_list(l):
    min=l[0]
    for i in l:
        if min>i:
            min=i
    return min

def sum_list(l):
    s=0
    for i in l:
        s=s+i
    return s
