class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        return next((num for num in count if count[num] == 1),None)
        