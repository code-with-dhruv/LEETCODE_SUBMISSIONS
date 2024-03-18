class Solution:
    def isPalindrome(self, s: str) -> bool:
        k=''.join(ch for ch in s if ch.isalnum())
        k=k.lower()
        if k[::-1]==k:
            return True
        return False
        