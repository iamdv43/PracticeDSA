def smallestLexicographical(text):
    for i in range(len(text)):
            if text[i] != 'a':
                return text[:i] + 'a' + text[i + 1:]
    return text[:-1] + 'b' if text[:-1] else ''

print("Ans: ", smallestLexicographical('azyz'))