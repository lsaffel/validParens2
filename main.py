def isValid(s: str) -> bool:
    stack = []
    closeToOpen = {")": "(", "]": "[", "}": "{"}
    for c in s:
        if c in closeToOpen:    # if c is a closing paren of some sort
            # stack[-1] refers to the last element on the stack, without popping it
            # "if stack" means if stack is not empty
            # "stack[-1] == closeToOpen[c]" << last element on stack has
            #   correct match (to c) in the dictionary key-value pairs
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()     # remove last element on stack, since it matches c
            else:
                return False
        else:
            stack.append(c)
    return True if not stack else False


if __name__ == '__main__':
    print(isValid("{}"))
    print(isValid("{]"))
    print(isValid("{{(())}}"))
    print(isValid("{[(())]}"))
    print(isValid("[[({})]]"))

