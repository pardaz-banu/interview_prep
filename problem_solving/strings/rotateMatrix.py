'''Logic:
First swap the first half matrix diagnal side keeping diagonal constant
and then swap row by half
'''

matrix = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(matrix[0])):
    for j in range(i,len(matrix[0])):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
m = (len(matrix[0])-1)//2
t = len(matrix[0])
#print(ip)
for col in range(len(matrix)):
    for row in range(m):
        matrix[row][col], matrix[t-row-1][col] = matrix[t-row-1][col], matrix[row][col]
    print(matrix)
print(matrix)
