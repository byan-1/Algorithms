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

#URLify: replace all " " in string with "%20"

