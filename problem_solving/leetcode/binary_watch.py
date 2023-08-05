class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for i in range(12):
            for j in range(60):
                if bin(i).count('1') + bin(j).count('1') == turnedOn:
                    result.append(f'{i}:{j:02d}')
        return result
