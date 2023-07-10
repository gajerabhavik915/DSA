# we will push open parentheses in stack and when we get any close, will try to match in stack.pop . 
# if it's match then it will be poped up from stack or else will return false.
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        closetoopen={')':'(','}':'{',']':'['}
        for i in s:
            if i in closetoopen:
                if stack and stack[-1]==closetoopen[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

