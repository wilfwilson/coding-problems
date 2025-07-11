class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def transform(x):
            func = {}
            out = ""
            count = 0
            for i in x:
                if not i in func:
                    func[i] = count
                    count += 1
                
                out += chr(func[i])
            return out
        
        return transform(s) == transform(t)
