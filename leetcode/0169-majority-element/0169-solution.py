class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # n log(n) solution: since the majority element occurs in at least
        # half of the entries of <nums>, it in particular occurs in the entry
        # in the midpoint of <nums>, when <nums> is sorted.
        nums.sort()
        midpoint = len(nums) // 2
        return nums[midpoint]
