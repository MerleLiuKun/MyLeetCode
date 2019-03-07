func removeElement(nums []int, val int) int {
    s_idx := 0
    for q_idx:=0; q_idx<len(nums); q_idx++{
        if nums[q_idx] != val {
            nums[s_idx] = nums[q_idx]
            s_idx ++
        }
    }
    return s_idx
}
