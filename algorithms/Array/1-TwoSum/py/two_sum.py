class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for idx, value in enumerate(nums):
            another = target - value
            if another in res:
                return [res[another], idx]
            else:
                res[value] = idx
        return None
