class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        tmp = 1
        res = [1]
        for i in range(1, rowIndex + 1):
            tmp = tmp * (rowIndex +1 -i) // i;
            res.append(tmp)
        return res
