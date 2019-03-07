class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        cur = None
        for i in range(len(nums)-1, -1, -1):
            if nums[i] == cur:
                nums.remove(cur)
            else:
                cur = nums[i]
        return len(nums)


    def removeDuplicates2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s_idx = 0
        for q_idx in range(len(nums)):
            if nums[q_idx] != nums[s_idx]:
                s_idx += 1
                nums[s_idx] = nums[q_idx]
        return s_idx + 1
