#P.26 - Reverse words in a sentence, optimized for time and space

#space inefficient
def reverseWords(string):
    flag = 1
    s = ""
    for char in string:
        s += char
        if char == ' ':
            flag = 0
            break
    if flag == 1:
        return s + " "
    else:
        return reverseWords(string[len(s):len(string)]) + s

def reverseSentenceInplace(list, start, end):
    if end - start < 1:
        s = 0
        e = 0
        for char in list:
            if char == " ":
                reverseWordInplace(l, s, e - 1)
                s = e + 1
            e += 1
        reverseWordInplace(l, s, e - 1)
        return list
    else:
        list[start], list[end] = list[end], list[start]
        reverseSentenceInplace(list, start + 1, end - 1)

def reverseWordInplace(list, start, end):
    if end - start < 1:
        return list
    else:
        list[start], list[end] = list[end], list[start]
        reverseWordInplace(list, start + 1, end - 1)

l = []
str = "this is a simple test string asdf"
l.extend(str)
reverseSentenceInplace(l,0,len(l) - 1)
str = ''.join(l)
print(str)


#Problem 28 - Array product

def arrayProd(X):
    n = len(X)
    left = [None] * (n)
    right = [None] * (n)
    M = [None] * len(X)
    left[0] = 1
    right[n - 1] = 1
    for i in range(1, n):
        left[i] = X[i - 1]*left[i - 1]
    for i in range(n-2, -1, -1):
        right[i] = X[i + 1] * right[i+1]
    for i in range(n):
        M[i] = left[i]*right[i]
    return M

X = [10, 3, 5, 6, 2]
M = arrayProd(X)
print(M)















