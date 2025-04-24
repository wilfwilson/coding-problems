class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_combos = {}
        i = 0
        out = []

        for s in strs:
            x = ''.join(sorted(s))
            if x in letter_combos:
                i = letter_combos[x]
                out[i].append(s)
            else:
                letter_combos[x] = len(out)
                out.append([s])

        return out
