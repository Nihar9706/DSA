class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rec={}

        for i,num1 in enumerate(nums):
            num2=target-num1

            if num2 in rec:
                return [rec[num2],i]
            else:
                rec[num1]=i