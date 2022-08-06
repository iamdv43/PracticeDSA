def countMaxOperation(log, target):
    log = list(log)
    target = list(target)
    count = len(log)
    for i in target:
        count = min(count, log.count(i))
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