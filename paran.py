
"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

"""
def balparant(s):

    stack=[]
    for char in s:
        if char in ["(","{","["]:
            stack.append(char)
        else:
            if not stack:
                return False
        cur=stack.pop()
        if cur ==")" and char!="(":
            return False
        if cur =="}" and char!="{":
            return False
        if cur =="]" and char!="[":
            return False
        if stack:
            return False
        return True
    #driver code
if __name__=="__main__":
    s="{}((())){}[{}]"

    if balparant(s):
        print("balanced")
    else:
        print(" not balanced")