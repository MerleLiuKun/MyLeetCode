class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
            一般遍历查找
        """
        res = 0
        for idx, num in enumerate(nums):
            if num == target:
                return idx
            elif num < target:
                res = idx + 1
            else:
                return res
        return res
