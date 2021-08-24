class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        
        r1, i1 = map(int, num1.split('i')[0].split('+'))
        r2, i2 = map(int, num2.split('i')[0].split('+'))
        
        r = r1 * r2 - i1 * i2
        i = r1 * i2 + r2 * i1
        
        return f'{r}+{i}i'