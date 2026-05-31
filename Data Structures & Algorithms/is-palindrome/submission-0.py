class Solution:
    def isPalindrome(self, s: str) -> bool:
        a = s.replace(" ", "")
        a = "".join(c for c in a if c.isalnum())
        a = a.lower()

        b = a[::-1]
        return a == b
