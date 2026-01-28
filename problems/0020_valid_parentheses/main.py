class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {')': '(', ']': '[', '}': '{'}

        for ch in s:
            if ch in parentheses.values():
                stack.append(ch)
                #print(stack)
            else: #closing 
                if not stack: #no opening to pair with
                    return False
                if stack.pop() != parentheses[ch]:
                    return False
        
        return not stack 

       
if __name__ == "__main__":
    s = Solution()

    print(s.isValid("()"))#True
    print(s.isValid("()[]{}"))#True
    print(s.isValid("(]"))#False
    print(s.isValid("([])"))#True
    print(s.isValid("([)]"))#False
    print(s.isValid("("))#False
    print(s.isValid("]["))#False
    print(s.isValid("(([]){})"))#True
