class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        min_repeats = (len(b) + len(a) - 1) // len(a)
        t = a * min_repeats
        if b in t:
            return min_repeats
        t += a
        if b in t:
            return min_repeats + 1
            
        return -1
