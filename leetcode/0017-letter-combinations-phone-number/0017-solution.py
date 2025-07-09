class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["", "", "abc", "def", "ghi", "jkl", "mno", "qprs", "tuv", "wxyz"]

        if len(digits) == 0:
            return []

        out = []
        def dfs(sub):
            k = len(sub)
            if k == len(digits):
                out.append(sub)
                return
            for s in letters[int(digits[k])]:
                dfs(sub + s)

        dfs('')
        return out
