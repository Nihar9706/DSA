class Solution:
    def checkDivisibility(self, n: int) -> bool:
        cnt=0
        prod=1
        s=str(n)
        for num in s:
            cnt+=int(num)
            prod*=int(num)
        return n%(prod+cnt)==0

        
