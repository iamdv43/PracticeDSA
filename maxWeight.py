def maxWeight(weights):
    n = len(weights)
    for i in range(len(weights)-1,0,-1):
        if i > 0 and weights[i - 1] < weights[i]:
            weights[i] = weights[i - 1] + weights[i]
            weights.remove(weights[i-1])
    return max(weights)

package_weights = [2,9,10,3,7]
print('Max weight: ', maxWeight(package_weights))