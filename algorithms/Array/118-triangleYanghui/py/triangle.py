class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows <= 0:
            return []
        res = [[1]]
        if numRows == 1:
            return res
        for row in range(2, numRows + 1):
            item = []
            for i in range(row):
                if i == 0:
                    item.append(res[row - 2][0])
                elif i == row - 1:
                    item.append(res[row - 2][-1])
                else:
                    item.append(res[row - 2][i] + res[row - 2][i - 1])
            res.append(item)
        return res
