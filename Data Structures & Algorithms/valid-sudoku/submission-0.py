class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #Here, we are going to create a hash set for each row, column and subgrid
        #to keep track of numbers previosly seen on any given row, column, or subgrid
        row_sets = [set() for _ in range(9)] #hash set for rows
        col_sets = [set() for _ in range(9)] #hash set for columns
        subgrid_set = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                if num in row_sets[r]:
                    return False
                if num in col_sets[c]:
                    return False
                if num in subgrid_set[r // 3][c // 3]:
                    return False

                row_sets[r].add(num)
                col_sets[c].add(num)
                subgrid_set[r // 3][c // 3].add(num)

        return True