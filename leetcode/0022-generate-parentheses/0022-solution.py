class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        out = []
        def dfs(string, nrOpen, nrClose):
            if nrClose == n:
                out.append(string)
            else:
                if nrOpen < n:
                    dfs(string + '(', nrOpen + 1, nrClose)
                if nrClose < nrOpen:
                    dfs(string + ')', nrOpen, nrClose + 1)

        dfs('', 0, 0)
        return out
