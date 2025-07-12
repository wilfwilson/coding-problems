class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(x):
            if len(x) == 1:
                return [x]

            out = []
            for i in x:
                y = list(x)
                y.remove(i)
                new = dfs(y)
                for z in new:
                    out.append([i] + z)
            return out

        return dfs(nums)
