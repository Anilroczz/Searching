def linear_search_v1(l,val) :
    for ele in l :
        if val == ele :
            return True
    else :
        return False

def linear_search_v2(l,val,ind) :
    if ind >= len(l) :
        return False
    elif val == l[ind] :
        return True
    else :
        ind += 1
        return linear_search_v2(l,val,ind)

lst = [3,9,7,0,55,19,87,-100,89]
ele1 = int(input("Enter the element 1 to search: "))
ele2 = int(input("Enter the element 2 to search: "))
print(linear_search_v1(lst,ele1))
print(linear_search_v2(lst,ele2,0))