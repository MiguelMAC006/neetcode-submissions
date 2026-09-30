class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupes = {}

        for num in nums:
            if num in dupes:
                return True
            else:
                dupes[num] = dupes.get(num, 0) + 1
        
        return False

         