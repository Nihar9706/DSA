class Solution:
    def removeCoveredIntervals(self, A: List[List[int]]) -> int:

        A.sort(key=lambda x: (x[0],-x[1]))

        max_end=0
        valid=0


        for start,end in A:
            if end>max_end:
                valid+=1
                max_end=end
        return valid
        
