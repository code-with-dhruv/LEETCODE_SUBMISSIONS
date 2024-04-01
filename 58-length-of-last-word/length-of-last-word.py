class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        k=[]
        lis = list(s.strip().split(" "))
        return len(lis[-1])
        