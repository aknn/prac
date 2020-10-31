
print('I am:', __name__)
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