class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
            遍历 + check
        """
        nums = sorted(nums)
        res = []
        pre = None
        for idx in range(len(nums)-2):
            value = nums[idx]
            if value > 0:
                break
            if pre == value:
                continue
            left, right = idx + 1, len(nums)-1
            target = 0 - value
            pre_l, pre_r = None, None
            while left != right:
                cur_l, cur_r = nums[left], nums[right]
                cur = cur_l + cur_r
                if cur > target:
                    right -= 1
                elif cur < target:
                    left += 1
                else:
                    if not (pre_l == cur_l or pre_r == cur_r):
                        res.append([value, nums[left], nums[right]])
                        pre_l, pre_r = cur_l, cur_r
                    left += 1
            pre = value
        return res
