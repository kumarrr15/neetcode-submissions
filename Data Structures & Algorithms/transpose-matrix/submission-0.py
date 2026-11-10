class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(matrix[0])
        m = len(matrix)
        for i in range(n):
            new_row = []
            for j in range(m):
                new_row.append(matrix[j][i])
            res.append(new_row)
        return res