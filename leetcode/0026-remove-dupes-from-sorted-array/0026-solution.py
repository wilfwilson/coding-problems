class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        last_val = nums[0]
        last_index = 0

        for i in range(1, len(nums)):
            if nums[i] != last_val:
                last_val = nums[i]
                last_index += 1
                nums[last_index] = nums[i]

        return last_index + 1
