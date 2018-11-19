def binarySearch(l, data, start, end):
    midpoint = (start+end)//2
    if l[midpoint] == data:
        return True
    if midpoint == len(l) - 2:
        return l[midpoint + 1] == data
    if midpoint == 0:
        return False
    else:
        if l[midpoint] < data:
            return binarySearch(l, data, midpoint, end)
        elif l[midpoint] > data:
            return binarySearch(l, data, start, midpoint)

list = [1,2,4,5,7,10, 11, 15, 17, 24]
print(binarySearch(list, 25, 0, 9))