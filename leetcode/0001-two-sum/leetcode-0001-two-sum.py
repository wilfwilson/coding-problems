class Solution:

    # Finds the known-to-exist unique, distinct indices <i>, <j> such that:
    # <nums[i] + nums[j] = target>
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Dict of found differences between <target> and the elements of <nums>
        seen = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in seen:
                return [i, seen[diff]]
            else:
                seen[nums[i]] = i
