def countMaxOperation(log, target):
    log = list(log)
    target = list(target)
    found = True
    count = 0
    while found:
        for i in target:
            if i in log:
                log.remove(i)
            else:
                found = False
        if found:
            count += 1
    return count

log = 'mononom'
target = 'mon'
print('Case 1: Count is ', countMaxOperation(log, target))

log = 'abacbc'
target = 'bca'
print('Case 2: Count is ', countMaxOperation(log, target))

log = 'abdadccacd'
target = 'edac'
print('Case 1: Count is ', countMaxOperation(log, target))