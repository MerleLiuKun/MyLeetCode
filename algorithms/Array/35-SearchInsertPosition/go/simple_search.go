func searchInsert(nums []int, target int) int {
    if len(nums) == 0 {
        return 0
    }
    var res = 0
    for idx := 0; idx<len(nums); idx++{
        if nums[idx] == target {
            return idx
        }
        if nums[idx] < target{
            res ++
        }
        if nums[idx] > target{
            return res
        }
    }
    return res
}
