class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n==1:
            return [['Q']]
        board = [['.' for i in range(n)] for j in range(n)]
        cols = set()
        dig1 = set()
        dig2 = set()
        result = []
        def nQueens(rows):
            if rows == n:
                c = [''.join(i) for i in board]
                result.append(c)
                return 
            for i in range(n):
                if i in cols or (rows+i) in dig1 or (rows - i) in dig2:
                    continue
                cols.add(i)
                dig1.add(rows+i)
                dig2.add(rows-i)
                board[rows][i] = 'Q'
                nQueens(rows+1)
                cols.remove(i)
                dig1.remove(rows+i)
                dig2.remove(rows-i)
                board[rows][i]='.'
        nQueens(0)
        return result
                
