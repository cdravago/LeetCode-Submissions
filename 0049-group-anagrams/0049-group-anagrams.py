class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = defaultdict(list)
        for w in strs:
            d["".join(sorted(w))].append(w)
        return list(d.values())