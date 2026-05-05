class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        keys = set(s) | set(t)
        count_s= dict(zip(keys, map(s.count, keys)))
        count_t= dict(zip(keys, map(t.count, keys)))

        return count_s== count_t