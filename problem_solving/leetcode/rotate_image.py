class Solution:
    #logic: reverse the columns first and then reverse matrix[i][j] with matrix[j][i]
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)//2):
            for j in range(len(matrix)):
                matrix[i][j],matrix[-(i+1)][j]=matrix[-(i+1)][j],matrix[i][j]
            print(matrix)
        for i in range(len(matrix)):
            for j in range(i,len(matrix)):
                if i==j:
                    continue
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        
