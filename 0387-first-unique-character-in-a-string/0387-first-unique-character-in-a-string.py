class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1
        """
        Example Testcase #1
        s = "leetcode"   

        count = Counter(s)
        count =  {"l": 1, "e": 3, "t" : 1, "c" : 1, "o" : 1, "d" : 1, }

        for i, c in enumerate(s):
            i = 0, c = "l"
            if count["l"] == 1? Y:
                return i -> 0
        """
