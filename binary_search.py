def binary_search(ar,s,e,item):
    if s <= e: 
        middle=(s+e)//2
        m=ar[middle]
        if m == item:
            return middle
        elif m > item:
            return binary_search(ar,s,middle-1,item)
        else:
            return binary_search(ar,middle+1,e,item)
    return -1
arr=[230,1,309,892,985,3928,83]
arr.sort()
print(*arr)
print(binary_search(arr,0,len(arr),int(input("Enter item value-"))))
