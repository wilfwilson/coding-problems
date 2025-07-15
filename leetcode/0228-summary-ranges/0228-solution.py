class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []

        if len(nums) > 0:
            x = nums[0]
            start = x
            last = x

            for i in range(1, len(nums)):
                x = nums[i]
                if x - 1 != last:
                    # Output range
                    if start == last:
                        out.append(str(start))
                    else:
                        out.append(str(start) + "->" + str(last))
                    start = x
                last = x

            if x == start:
                out.append(str(start))
            else:
                out.append(str(start) + "->" + str(x))
        
        return out
