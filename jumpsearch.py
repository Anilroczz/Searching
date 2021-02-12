def jump_search(l,val) :
    shift = int(len(l) ** 0.5)
    ind = shift
    while ind < len(l) and val > l[ind] :
        ind += shift
    for i in range(ind-shift,ind) :
        if val == l[i] :
            return True
    else :
        return False

lst = [3,9,7,0,55,19,87,-100,89]
lst.sort()
ele- = int(input("Enter the element to search: "))
print(jump_search(lst,ele))
