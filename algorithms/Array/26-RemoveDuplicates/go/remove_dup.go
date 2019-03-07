func removeDuplicates(nums []int) int {
    if len(nums) == 0{
        return 0
    }
    s_idx := 0

    for q_idx := 1; q_idx<len(nums); q_idx++{
        if nums[q_idx] != nums[s_idx]{
            s_idx++
            nums[s_idx] = nums[q_idx]
        }
    }
    return s_idx + 1

}
