class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtrack(i, curr, total):
            #succeeded
            if total == target:
                res.append(curr.copy())
                return
            #failed
            if i >= len(candidates) or total > target:
                return
            
            #include
            curr.append(candidates[i])
            backtrack(i + 1, curr, total + candidates[i])

            #not include
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            backtrack(i + 1, curr, total)
        
        backtrack(0, [], 0)
        return res