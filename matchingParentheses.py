def validParentheses( s: str) -> bool:
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        if char in dict.values():
            stack.append(char)
        elif char in dict:
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []

print(validParentheses('(){}[]'))