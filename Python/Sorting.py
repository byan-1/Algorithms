from random import randint

def bubbleSort(l):
    for i in range(0, len(l) - 1):
        for j in range(0, len(l)-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l

def selectionSort(l):
    index = 0
    for i in range(0, len(l) - 1):
        min = l[index]
        minindex = index
        for k in range(index,len(l)):
            if l[k] < min:
                min = l[k]
                minindex = k
        l[minindex], l[index] = l[index], l[minindex]
        index += 1
    return l

def selectionRecursive(l, start, end):
    if start >= end:
        return
    b = start
    r = end
    min = l[start]
    minindex = start
    while(b <= end):
        if min > l[b]:
            min = l[b]
            minindex = b
        b += 1
    l[start], l[minindex] = l[minindex], l[start]
    selectionRecursive(l, start + 1, end)

def insertionSort(l):
    for i in range(1, len(l) - 1):
        current =  l[i]
        j = i
        while(j > 0 and current < l[j] and current < l[j - 1]):
            l[j], l[j-1] = l[j+1], l[j]
            j -= 1
        l[j] = current
    return l
# recursion: create a correct base case; create a correct function for n; assume recursive calls are correct.

def mergeSort(l):
    if len(l) <= 1:
        return l
    else:
        s = []
        middle = len(l)//2
        left = mergeSort(l[:middle])
        right = mergeSort(l[middle:])
        lindex = 0
        rindex = 0

        while len(left) != lindex or len(right) != rindex:
            if len(left) == lindex:
                s.append(right[rindex])
                rindex += 1
            elif len(right) == rindex:
                s.append(left[lindex])
                lindex += 1
            elif left[lindex] < right[rindex]:
                s.append(left[lindex])
                lindex += 1
            elif right[rindex] < left[lindex]:
                s.append(right[rindex])
                rindex += 1
            else:
                s.append(left[lindex])
                lindex += 1
        return s


def mergeSort2(l):
    if len(l) > 1:
        middle = len(l)//2
        left = mergeSort(l[:middle])
        right = mergeSort(l[middle:])
        lindex = 0
        rindex = 0
        sindex = 0
        while len(left) != lindex or len(right) != rindex:
            if len(left) == lindex:
                l[sindex] = right[rindex]
                rindex += 1
                sindex += 1
            elif len(right) == rindex:
                l[sindex] = left[lindex]
                lindex += 1
                sindex += 1
            elif left[lindex] < right[rindex]:
                l[sindex] = left[lindex]
                lindex += 1
                sindex += 1
            elif right[rindex] < left[lindex]:
                l[sindex] = right[rindex]
                rindex += 1
                sindex += 1
            else:
                l[sindex] = left[lindex]
                lindex += 1
                sindex += 1


def quickSort(l, first, last):
    if first >= last:
        return
    split = partition(l, first, last)
    quickSort(l, first, split - 1)
    quickSort(l, split + 1, last)


def partition(l, first, last):
    pivotval = l[first]
    k = first + 1
    for i in range(first + 1, last + 1):
        if l[i] <= pivotval:
            l[i], l[k] = l[k], l[i]
            k += 1
    l[first], l[k - 1] = l[k - 1], l[first]
    return k - 1


l = [5, 5, 11, 14, 5, 3, 5, 4, 12, 5]
mergeSort2(l)
print(l)