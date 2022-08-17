def fibonnaci(num):
    if num == 1:
        return 1
    elif num == 0:
        return 0
    else:
        return fibonnaci(num-1) + fibonnaci(num-2)

print(fibonnaci(11))