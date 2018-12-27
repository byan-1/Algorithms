#P.2
#a. Unsorted array - find the pair with the maximal difference in O(n) time worst case
#b. Sorted array - find the pair with the maximal difference in O(1) time worst case
#c. Unsorted array - Find the pair with the minimal difference in O(nlog(n)) time worse case
#d. Sorted array - Find the pair with the minimal difference in O(n) time worst case

def quickSort(l, first, last):
    if first >= last:
        return
    pivot = l[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while(leftmark <= rightmark and l[leftmark] <= pivot):
            leftmark += 1
        while(rightmark >= leftmark and l[rightmark] >= pivot):
            rightmark -= 1
        if leftmark >= rightmark:
            done = True
            l[first], l[rightmark] = l[rightmark], l[first]
        else:
            l[leftmark], l[rightmark] = l[rightmark], l[leftmark]

    quickSort(l, first, rightmark - 1)
    quickSort(l, rightmark + 1, last)

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


def unsortedMax(arr):
    min = findMin(arr)
    max = findMax(arr)
    maxdiff = max - min
    return maxdiff

def sortedMax(arr):
    maxdiff = arr[len(arr) - 1] - arr[0]
    return maxdiff

def minDiff(arr):
    quickSort(arr, 0, len(arr) - 1)
    prev = arr[0]
    cur = arr[1]
    mindiff = cur - prev
    while (cur < len(arr)):
        if cur - prev < mindiff:
            mindiff = cur - prev
        prev += 1
        cur += 1

#P3
#O(nlogn) algorithm that partitions sequence of 2n numbers into a n pairs with the property that
#the partition has the minimizes the maximum sum of a pair.

def minpartition(arr):
    partition = []
    quickSort(arr, 0, len(arr) - 1)
    cur = (len(arr) - 1)//2
    next = cur + 1
    while cur >= 0 and next < len(arr):
        partition.append([arr[cur],arr[next]])
        cur -= 1
        next += 1
    return partition

#P4
#n pairs of items: first item is a number and second is one of three colours (r,b,y).
#Items are sorted by number.
#Find O(n) algorithm to sort items by color (r before b before y) such that numbers for identical numbers stay sorted

def sortPairs(arr):

    i = 0
    j = 0
    new = [None] * len(arr)
    while(i < len(arr)):
        if arr[i][1] == 'r':
            new[j] = arr[i]
            j += 1
        i += 1
    i = 0
    while(i < len(arr)):
        if arr[i][1] == 'b':
            new[j] = arr[i]
            j += 1
        i += 1
    i = 0
    while (i < len(arr)):
        if arr[i][1] == 'y':
            new[j] = arr[i]
            j += 1
        i += 1
    return new

def mode(arr):
    d = {}
    for i in range(0, len(arr)):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    return max(d, key=d.get)

#4.6: given 2 sets S1 and S2 each of size n and a number x,
# describe an O(nlogn) algorithm for finding whether there exists a pair of elements, one from S1 and one from S2 that add up to x
# sort both S1 and S2
#compare min element in S1 with min element in S2, if sum is less, increment S2

def findSumPair(arr1, arr2, x):
    quickSort(arr1, 0, len(arr1) - 1)
    for i in range(0, len(arr2)):
        val = x - arr2[i]
        if binarySearch(arr1, val, 0, len(arr1)-1):
            return True
    return False

#Alternative Algorithm:
#Sort both S1 and S2. Have one variable beg begin at 0, another variable end at length n - 1.
#While the beginning is less than the length, and the end is greater or equal to zero, do:
#if S1[beg] + S2[end] > sum, decrement end
#if S1[beg] + S2[end] < sum, increment beg
#if eq, return True (can also return beg/end indices)

#P4-8: find if there are elements in an array whos sum is integer x; assume sorted.
def findSum(arr, x):
    start = 0
    end = len(arr) - 1
    while start != end:
        if arr[start] + arr[end] == x:
            return True
        elif arr[start] + arr[end] > x:
            end -= 1
        elif arr[start] + arr[end] < x:
            start += 1
    return False
#P4-9: find union of sets A and B. Output should be an array of distinct elements that form the union such that they appear more than once in the union.
#Assume sorted, find O(n) solution, where n is the maximal length of A and B.

def union(arr1, arr2):
    i = 0
    j = 0
    union = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            union.append(arr1[i])
            i += 1
            j += 1
        if arr1[i] < arr2[j]:
            i += 1
        if arr1[i] > arr2[j]:
            j += 1
    return union


def findSubsets(arr):
    if arr == []:
        return [[]]
    else:
        sub = findSubsets(arr[1:])
        copy = []
        for elem in sub:
            copy += [elem + [arr[0]]]
        return sub + copy

def sizeSubsets(arr, size):
    if size == 0:
        return [[]]
    else:
        new = []
        for i in range(len(arr)):
            sub = sizeSubsets(arr[i+1:], size - 1)
            for elem in sub:
                new += [elem + [arr[i]]]
        return new

#P4-11: Given a set of integers S of length n, an integer T, and an integer k,
#find an algorithm to test whether k of the integers in S add up to T in O(n**(k-1)logn) time

def checkSum(arr, k, T):
    quickSort(arr, 0, len(arr) - 1)
    return _checkSum(arr,k,T)

def _checkSum(arr,k,T):
    if k <= 2:
        return findSum(arr, T)

    A = [None] * (len(arr) - 1)
    for i in range(0, len(arr)):
        m = 0
        for j in range(0, len(arr)):
            if i != j:
                A[m] = arr[j]
                m += 1
        if _checkSum(A, k - 1, T-arr[i]):
            return True
    return False

#Find all elements occuring more than n/2 times in a list in O(n) time and O(1) space. O(n) space can be achieved easily using hashmap.
#Gives the majority element if there exists a majority element.
def majCand(arr):
    mindex = 0
    count = 1
    for i in range (1, len(arr)):
        if arr[mindex] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            mindex = i
            count = 1
    return arr[mindex]


#Merge k sorted lists into one sorted list

class ListNode:
    def __init__(self, val, index, next):
        self.val = val
        self.index = index
        self.next = next


def form_heap(arr):
    i = (len(arr) - 1) // 2
    while i >= 0:
        sift_down(arr, i)
        i -= 1

def sift_down(arr, i):
    while 2*i + 1 < len(arr):
        if 2*i + 1 == len(arr) - 1 or arr[2*i + 1].val < arr[2*i + 2].val:
            j = 2*i + 1
        else:
            j = 2*i + 2
        if arr[i].val > arr[j].val:
            arr[i], arr[j] = arr[j], arr[i]
        i = j

def mergeSorted(l):
    headarr = []
    size = len(l)*len(l[0])
    for i in range(len(l)):
        headarr.append(ListNode(l[i][0], i, 1))
    form_heap(headarr)
    sorted = [None]*size
    for i in range(0, size):
        sorted[i] = headarr[0].val
        if headarr[0].next < len(l[0]):
            headarr[0].val = l[headarr[0].index][headarr[0].next]
            headarr[0].next += 1
        else:
            headarr[0] = headarr[len(headarr) - 1]
            del headarr[len(headarr) - 1]
        sift_down(headarr, 0)
    return sorted

#4-15: Find kth largest element among n keys
def partition(l, first, last):
    pivot = first
    k = first + 1
    for i in range(first + 1, last + 1):
        if l[i] <= l[pivot]:
            l[i], l[k] = l[k], l[i]
            k += 1
    l[pivot], l[k - 1] = l[k - 1], l[pivot]
    return k - 1


def quickSelect(arr, k):
    if k < 1 or k > len(arr):
        return None
    return _quickSelect(arr, 0, len(arr) - 1, k - 1)

def _quickSelect(arr, start, end, k):
    if start >= end:
        return arr[start]
    splitpoint = partition(l, start, end)
    if k == splitpoint:
        return arr[k]
    if k < splitpoint:
        return _quickSelect(arr, start, splitpoint - 1, k)
    if k > splitpoint:
        return _quickSelect(arr, splitpoint + 1, end, k)

def sortPairsPartition(arr):

    i = 0
    j = 0
    new = [None] * len(arr)
    while(i < len(arr)):
        if arr[i][1] == 'r':
            new[j] = arr[i]
            j += 1
        i += 1
    i = 0
    while(i < len(arr)):
        if arr[i][1] == 'b':
            new[j] = arr[i]
            j += 1
        i += 1
    i = 0
    while (i < len(arr)):
        if arr[i][1] == 'y':
            new[j] = arr[i]
            j += 1
        i += 1
    return new

#4-20: efficient algorithm to arrange n keys so that all negative keys precede all non-negative keys
def negativepart(l):
    pivotval = 0
    k = 1
    for i in range(1, len(l)):
        if l[i] <= pivotval:
            l[i], l[k] = l[k], l[i]
            k += 1
    l[0], l[k - 1] = l[k - 1], l[0]


def circularPoint(arr):
    start = 0
    end = len(arr) - 1
    if arr[0] < arr[end]:
        return 0
    while (start <= end):
        midpoint = (start + end) // 2
        if arr[midpoint] < arr[end]:
            if arr[midpoint - 1] > arr[midpoint]:
                return midpoint
            else:
                end = midpoint - 1
        elif arr[midpoint] >= end:
            start = midpoint + 1
    return None


def indexEq(arr):
    start = 0
    end = len(arr) - 1
    while start <= end:
        midpoint = (start + end)//2
        if arr[midpoint] < midpoint:
            start = midpoint + 1
        elif arr[midpoint] > midpoint:
            end = midpoint - 1
        else:
            return True
    return False


def notPresent(arr):
    n = len(arr) - 1
    if arr[0] > 1:
        return 1
    elif arr[n-1] == n:
        return n + 1
    else:
        return findGap(arr, 0, len(arr) - 1)

def findGap(arr, first, last):
    if last == first + 1:
        return arr[first] + 1
    else:
        mid = (first + last)//2
        if arr[mid]- arr[first] == mid - first:
            return findGap(arr, mid, last)
        else:
            return findGap(arr, first, mid)

l = [1,2,4,8,9,10]
print(notPresent(l))





