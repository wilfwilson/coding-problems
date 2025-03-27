class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # edge cases
        if target <= nums[0]:
            return 0
        elif target == nums[-1]:
            return len(nums) - 1
        elif target > nums[-1]:
            return len(nums)

        lo = 0
        hi = len(nums) - 1

        while lo < hi - 1:
            i = int((lo + hi) / 2)
            if nums[i] == target:
                return i
            elif nums[i] < target:
                lo = i
            else:
                hi = i
        return hi
