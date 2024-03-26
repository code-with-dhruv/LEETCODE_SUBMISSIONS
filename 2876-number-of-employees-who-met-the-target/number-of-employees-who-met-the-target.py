class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        ctr=0
        for i in hours:
            if i>=target:
                ctr+=1
        return ctr
        