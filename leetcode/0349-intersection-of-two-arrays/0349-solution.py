class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Naive solution, but the lists are only at most 1000 entries long,
        # and sorting and doing binary search in such lists is cheap.
        nums1.sort()
        nums2.sort()
        last = None
        out = []
        for x in nums1:
            if x != last and x in nums2:
                out.append(x)
            last = x
        return out
