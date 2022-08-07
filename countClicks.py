def countClicks(text):
    keypad = [1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]
    count = 0
    for i in text:
        count += keypad[ord(i) - ord('a')]
    return count


text = "abacadefghibj"
print("1 Clicks: ", countClicks(text))

text = "abcghdiefjoba"
print("2 Clicks: ", countClicks(text))