class Solution(object):
    x= 125
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]
    print(isPalindrome(None,x))

