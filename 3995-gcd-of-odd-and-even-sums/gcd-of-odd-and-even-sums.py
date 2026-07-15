class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        if n==0:
            return 0
        even=0
        odd=0
        cnt=0
        for i in range(100000000000000000000000000):
            if i%2==0:
                even+=1
            else:
                odd+=1
            cnt+=1
            if cnt==2*n:
                return gcd(odd,even)

        