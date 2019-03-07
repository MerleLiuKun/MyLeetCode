class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        s_idx = 0
        for q_idx in range(0, len(nums)):
            if nums[q_idx] != val:
                nums[s_idx] = nums[q_idx]
                s_idx += 1
        return s_idx
