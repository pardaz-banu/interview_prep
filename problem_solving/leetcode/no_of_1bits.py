class Solution:
    def hammingWeight(self, n: int) -> int:
        #print(bin(n))
        return str(bin(n)).count('1')
