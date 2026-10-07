class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        total , curr = 0,0
        start = 0

        for i in range(len(gas)):
            net = gas[i] - cost[i]
            curr += net

            if curr < 0:
                start = i +1
                curr =0 
        return start


        