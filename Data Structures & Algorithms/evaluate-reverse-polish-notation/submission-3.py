import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        calc = []
        ops  = {"+" : operator.add,
                "-" : operator.sub ,
                "*" : operator.mul ,
                "/" : operator.truediv} 

        for c in tokens:
            if c not in ops:
                calc.append(int(c))
            else:
                b, a = calc.pop(), calc.pop()
                calc.append(int(ops[c](a, b)))
        
        return calc.pop()