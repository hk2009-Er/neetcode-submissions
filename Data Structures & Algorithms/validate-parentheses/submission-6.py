class Solution:
    def isValid(self, s: str) -> bool:
        result =[]
        for i in s:
            if i in ["(","[","{"]:
                result.append(i)
            elif result and ((i == ")" and result[-1] == "(") or (i == "]" and result[-1] == "[") or ((i == "}" and result[-1] == "{")))  :
                result.pop()
            else:
                return False

        if result:
            return False
        return True 
