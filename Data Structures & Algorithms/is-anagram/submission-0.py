class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mS, mT = {}, {}

        for i in range(len(s)):
            mS[s[i]] = mS.get(s[i], 0) + 1
            mT[t[i]] = mT.get(t[i], 0) + 1
        
        return mS == mT