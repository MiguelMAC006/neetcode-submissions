class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, cur, total):
            #succeeded
            if total == target:
                res.append(cur.copy())
                return
            #did not succeed
            if i >= len(nums) or total > target:
                return
            
            #decision to include
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            #decision not to include
            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)
        return res