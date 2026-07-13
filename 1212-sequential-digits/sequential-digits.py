class Solution:
    def sequentialDigits(self, l:int, h: int) -> List[int]:
        ans=[]
        for i in range(1,10):
            num=i
            for j in range(i+1,10):
                num=num*10 + j 
                if l <=num <= h:
                    ans.append(num)
        ans.sort()
        return ans
