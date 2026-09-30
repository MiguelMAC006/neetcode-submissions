class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, curr in enumerate(nums):
            if curr > 0:
                break
            
            if i > 0 and nums[i - 1] == curr:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = curr + nums[l] + nums[r]

                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    result.append([curr, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        
        return result



        