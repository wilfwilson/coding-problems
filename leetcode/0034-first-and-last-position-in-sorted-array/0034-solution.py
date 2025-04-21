class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # Special case an empty list <nums>
        if not nums:
            return [-1, -1]

        # Special case the first entry being the target
        if nums[0] == target:
            first = 0
        else:
            # Otherwise use binary search to find first position of target
            lo = 0
            hi = len(nums) - 1
            while lo < hi - 1:
                i = int((lo + hi) / 2)
                if nums[i] < target:
                    lo = i
                else:
                    hi = i

            if nums[hi] == target:
                first = hi
            else:
                # Target not found
                return [-1, -1]

        # Special case the last entry being the target
        if nums[-1] == target:
            last = len(nums) - 1
        else:
            # Otherwise use binary search to find last position of target
            lo = first
            hi = len(nums) - 1
            while lo < hi - 1:
                i = int((lo + hi) / 2)
                if nums[i] <= target:
                    lo = i
                else:
                    hi = i

            last = lo

        return [first, last]
