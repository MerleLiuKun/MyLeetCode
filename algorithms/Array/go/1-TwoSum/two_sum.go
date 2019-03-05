func twoSum(nums []int, target int) []int {
    res := make(map[int]int)
    for i:=0; i< len(nums); i++ {
        if idx, ok := res[target-nums[i]]; ok{
            return []int{idx, i}
        }
        res[nums[i]] = i
    }
    return nil
}
