class Solution:
    def sumAndMultiply(self, n: int) -> int:
        sum=0
        s=""
        if n==0: return 0
        for num in str(n):
            if num!='0':
                sum+=int(num)
                s+=num
        return int(s)*sum

        