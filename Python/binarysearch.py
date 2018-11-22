def binarySearch(l, data, start, end):
    midpoint = start + (end-start)//2
    if len(l) < 1 or start > end:
        return False
    if l[midpoint] == data:
        return True
    else:
        if l[midpoint] < data:
            return binarySearch(l, data, midpoint + 1, end)
        elif l[midpoint] > data:
            return binarySearch(l, data, start, midpoint - 1)


list = [1,2,4,5,7,10, 11, 15, 17, 24, 25]
print(binarySearch(list, 25, 0, 10))