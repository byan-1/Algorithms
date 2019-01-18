#1.1 function to determine if string has all unique characters

#O(n) runtime, O(1) space
def unique(s):
    k = {}
    for char in s:
        if char in k and k[char] == 0:
            k[char] += 1
        elif char not in k:
            k[char] = 0
        else:
            return False

    return True

#without additional data structures: convert characters to ascii, get an array of len 128 and store boolean variables for whether or not the char exists

#1.2 check if two strings are permutations of each other:

def permstrings(s1,s2):
    k1 = {}
    k2 = {}

    if len(s1) != len(s2):
        return False

    for char in s1:
        if char in k1:
            k1[char] += 1
        else:
            k1[char] = 0

    for char in s2:
        if char in k2:
            k2[char] += 1
        else:
            k2[char] = 0

    if k1 == k2:
        return True
    return False

#1.3: URLify: replace " " with "%20"

def urlify(s, tl):
    l = len(s) - 1
    for i in range(tl - 1, -1, -1):
        if s[i] == ' ':
            s[l] = '0'
            s[l - 1] = '2'
            s[l - 2] = '%'
            l -= 3
        else:
            s[l] = s[i]
            l -= 1
    return s


#1.4: palindrome permutation: check if a string is a permutation of a palindrome

def palinperm(str):
    l = len(str)
    charcount = {}
    for char in str:
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1

    oddcount = 0
    for key, freq in charcount.items():
        if freq % 2 == 1:
            oddcount += 1

    if (l % 2 == 0 and oddcount == 0) or (l % 2 == 1 and oddcount == 1):
        return True
    return False

def palinperm(str):
    l = len(str)
    charcount = {}
    for char in str:
        if char in charcount:
            charcount[char] += 1
        else:
            charcount[char] = 1

    foundodd = 0
    for key, freq in charcount.items():
        if freq % 2 == 1:
            if foundodd:
                return False
            foundodd = 1
    return True


#one away: check if a string is 1 edit away

def oneaway(str1,str2):
    l1 = len(str1)
    l2 = len(str2)
    if abs(l2 - l1) > 1:
        return False


    diffflag = 0
    if abs(l2 - l1) == 1:
        if l2 > l1:
            i = 0
            j = 0
            while(i < l1):
                if str1[i] != str2[j]:
                    if diffflag:
                        return False
                    diffflag = 1
                else:
                    i += 1
                j += 1

        if l1 > l2:
            i = 0
            j = 0
            while (i < l2):
                if str2[i] != str1[j]:
                    if diffflag:
                        return False
                    diffflag = 1
                else:
                    i += 1
                j += 1

    if l2 - l1 == 0:
        for i in range(l1):
            if str1[i] != str2[i]:
                if diffflag:
                    return False
                diffflag = 1
    return True


#1.6: string compression

def strcomp(s):
    if len(s) < 1:
        return s
    result = ''
    if len(s) == 1:
        result += s + str(1)
        return result

    count = 0
    strlist = []
    for i in range(len(s)):
        count += 1
        if i == len(s) - 1 or s[i] != s[i+1]:
            strlist.append(s[i] + str(count))
            count = 0
    return ''.join(strlist)

#1.7: rotate matrix by 90 degrees
def rotatematrix(matrix):
    l = len(matrix)
    layer = 0

    while layer < l//2:
        first = layer
        last = l - 1 - layer
        temp = matrix[first][first:last]
        for i in range(first, last):
            matrix[first][i] = matrix[last - i + first][first]
        for i in range(first, last):
            matrix[i + 1][first] = matrix[last][i+1]
        for i in range(first, last):
            matrix[last][i + 1] = matrix[last - i - 1 + first][last]
        for i in range(first, last):
            matrix[i][last] = temp[i-first]
        layer += 1

#1.8 zero-matrix: if an element in an MxN matrix is 0, its entire row and col are set to zero
#O(mn) time complexity, O(Max(m,n)) space
def zerorow(matrix, row):
    for i in range(len(matrix[row])):
        matrix[row][i] = 0

def zerocol(matrix,col):
    for i in range(len(matrix)):
        matrix[i][col] = 0

def zeromatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    zerorows = []
    zerocols = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if i not in zerorows:
                    zerorows.append(i)
                if j not in zerocols:
                    zerocols.append(j)

    for row in zerorows:
        zerorow(matrix, row)
    for col in zerocols:
        zerocol(matrix, col)

#O(1) space: use first row/col as a replacement for row/col lists
def zeromatrix2(matrix):
    rowzero = 0
    colzero = 0
    m = len(matrix)
    n = len(matrix[0])
    for i in range(n):
        if matrix[0][i] == 0:
            rowzero = 1
    for i in range(m):
        if matrix[i][0] == 0:
            colzero = 1

    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1,n):
        if matrix[0][i] == 0:
            zerocol(matrix, i)
    for i in range(1,m):
        if matrix[i][0] == 0:
            zerorow(matrix,i)
    if rowzero == 1:
        zerorow(matrix, 0)
    if colzero == 1:
        zerocol(matrix, 0)

#string rotation: given two strings s1 and s2, find whether s2 is a rotation of s1 using only one call of isSubstring

def stringrotation(s1,s2):
    if len(s1) != len(s2) or len(s1) == 0:
        return False
    s1s1 = s1 + s1
    return s2 in s1s1