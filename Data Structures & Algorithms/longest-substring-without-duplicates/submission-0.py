class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = curr = best = 0

        for r in range(len(s)):
            while s[r] in s[l:r]:
                l += 1
                curr -= 1
            curr += 1
            best = max(best, curr)
        
        return best