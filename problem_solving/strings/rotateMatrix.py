'''Logic:
First swap the first half matrix diagnal side keeping diagonal constant
and then swap row by half
'''

ip = [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(ip[0])):
    for j in range(i,len(ip[0])):
        ip[i][j], ip[j][i] = ip[j][i], ip[i][j]
m = (len(ip[0])-1)//2
t = len(ip[0])
#print(ip)
for col in range(len(ip)):
    for row in range(m):
        ip[row][col], ip[t-row-1][col] = ip[t-row-1][col], ip[row][col]
    print(ip)
print(ip)
