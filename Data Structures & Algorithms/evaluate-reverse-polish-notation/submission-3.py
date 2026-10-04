class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result = []

        for token in tokens:
            if token in ['+','-','*','/']:
                num1=result.pop(-2)
                num2=result.pop(-1)

                if token == '+':
                    rs=num1+num2
                elif token == '-':
                    rs=num1-num2
                elif token == '*':
                    rs=num1*num2
                elif token == '/':
                    rs=num1/num2
                result.append(int(rs))
            else:
                result.append(int(token))
        
        return result[-1]
