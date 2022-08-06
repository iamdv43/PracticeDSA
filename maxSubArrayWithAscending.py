def maxSum(nums):
    maxSum = max(nums)
    for ind in range(len(nums),0,-1):
        sumArray = findSum(nums[:ind])
        maxSum = max(maxSum, sumArray)
    return maxSum

def findSum(nums):
    prev = nums[-1]
    temp = nums[-1]
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < prev:
            temp = temp + nums[i]
            prev = nums[i]
        elif nums[i] > prev and prev > 1:
            prev = prev - 1
            temp = temp + prev
        if prev <= 1:
            return temp
    return temp

nums = [7,4,5,2,6,5]
print('ans: ' , maxSum(nums))