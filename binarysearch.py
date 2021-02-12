def binary_search_v1(l,val) :
    (is_found,left,right,mid) = (False,0,len(l),0)
    while not is_found and left < right :
        mid = (left+right)//2
        if val == l[mid] :
            is_found = True
            break
        elif val < l[mid] :
            right = mid
        else :
            left = mid + 1
    return is_found

def binary_search_v2(l,val,left,right) :
    mid = (left + right) // 2
    if right <= left :
        return False
    elif val == l[mid] :
        return True
    elif val < l[mid] :
        return binary_search_v2(l,val,left,mid)
    else :
        return binary_search_v2(l,val,mid+1,right)

lst = [3,9,7,0,55,19,87,-100,89]
lst.sort()
ele1 = int(input("Enter the element 1 to search: "))
ele2 = int(input("Enter the element 2 to search: "))
print(binary_search_v1(lst,ele1))
print(binary_search_v2(lst,ele2,0,len(lst)))