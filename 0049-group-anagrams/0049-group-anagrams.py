class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = []
        for w in strs:
            key = sorted(w)
            for k, lst in groups:
                if k == key:
                    lst.append(w)
                    break
            else:
                groups.append((key, [w]))
        return [lst for _, lst in groups]