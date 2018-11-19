#Write a function that takes a string as a parameter and returns a new string that is the reverse of the old string.

def reverseStringRecursive(s):
    r = ""
    if len(s) <= 1:
        return s
    else:
        return s[-1] + reverseStringRecursive(s[:-1])

#Write a function that takes a string as a parameter and returns True if the string is a palindrome, False otherwise.
# Remember that a string is a palindrome if it is spelled the same both forward and backward.
# For example: radar is a palindrome. for bonus points palindromes can also be phrases, but you need to remove the spaces and punctuation before checking.
# for example: madam i’m adam is a palindrome.
def palindromeRecursive(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and palindromeRecursive(s[1:-1])


s = "asdf"
r = reverseStringRecursive(s)
print(r)