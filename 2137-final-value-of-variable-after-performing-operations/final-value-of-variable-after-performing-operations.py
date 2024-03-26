class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        ctr=0
        for i in range(len(operations)):
            if operations[i][1]=='+':
                ctr+=1
            else:
                ctr-=1
        return ctr
        