#  insert
#  sift_up - needed for insert
#  get_max - returns the max item, without removing it
#  get_size() - return number of elements stored
#  is_empty() - returns true if heap contains no elements
#  extract_max - returns the max item, removing it
#  sift_down - needed for extract_max
#  remove(i) - removes item at index x
#  heapify - create a heap from an array of elements, needed for heap_sort
#  heap_sort() - take an unsorted array and turn it into a sorted array in-place using a max heap
# note: using a min heap instead would save operations, but double the space needed (cannot do in-place).



class MaxHeap:
    def __init__(self):
        self.heap = []

    def siftUp(self, i):
        while i > 0:
            parent = self._parent(i)
            if self.heap[i] > self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def insert(self, data):
        self.heap.append(data)
        self.siftUp(len(self.heap) - 1)

    def print(self):
        k = 1
        for i in range(0, len(self.heap)):
            print(self.heap[i], end = ' ')
            if i == k - 1:
                print('')
                k = k*2 + 1

    def _parent(self, i):
        return (i-1) // 2

    def maxChildIndex(self, i):
        if 2*i + 1 < len(self.heap) - 1:
            if self.heap[2*i + 1] < self.heap[2*i + 2]:
                return 2*i + 2
            else:
                return 2*i + 1
        if 2*i + 1 == len(self.heap) - 1:
            return 2*i + 1

    def siftDown(self, k):
        while k*2 + 1 <= len(self.heap) - 1:
            j = self.maxChildIndex(k)
            if self.heap[k] < self.heap[j]:
                self.heap[k], self.heap[j] = self.heap[j], self.heap[k]
            k = j

    def extractMax(self):
        max = self.heap[0]
        i = len(self.heap) - 1
        self.heap[0] = self.heap[i]
        del self.heap[i]
        self.siftDown(0)
        return max

    def formHeap(self, arr):
        self.heap = arr
        i = (len(arr) - 1)//2
        while i >= 0:
            self.siftDown(i)
            i -= 1

    def heapSort(self):
        i = len(self.heap) - 1
        sorted = [None] * (i + 1)
        while len(self.heap) > 0:
            sorted[i] = self.extractMax()
            i -= 1
        return sorted


def sift_down(arr, i, k):
    while 2*i + 1 <= k:
        if 2*i + 1 == k or arr[2*i + 1] > arr[2*i + 2]:
            j = 2*i + 1
        else:
            j = 2*i + 2
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        i = j


def form_heap(arr):
    i = (len(arr) - 1)//2
    while i >= 0:
        sift_down(arr, i, len(arr) - 1)
        i -= 1


def heap_sort(arr):
    form_heap(arr)
    i = len(arr) - 1
    while i >= 0:
        arr[i], arr[0] = arr[0], arr[i]
        i -= 1
        sift_down(arr, 0, i)








