#Q1.
def arrayPairSum(nums):
    nums.sort()
    max_sum = 0
    
    for i in range(0, len(nums), 2):
        max_sum += min(nums[i], nums[i+1])
    
    return max_sum

# Example usage:
nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
print(result)  # Output: 4

#Q2.
def distributeCandies(candyType):
    uniqueCandies = set()
    n = len(candyType)
    
    for candy in candyType:
        uniqueCandies.add(candy)
        if len(uniqueCandies) == n // 2:
            break
    
    return min(len(uniqueCandies), n // 2)

# Example usage:
candyType = [1, 1, 2, 2, 3, 3]
result = distributeCandies(candyType)
print(result)  # Output: 3

#Q3.
def findLHS(nums):
    numCount = {}
    
    for num in nums:
        if num not in numCount:
            numCount[num] = 1
        else:
            numCount[num] += 1
    
    maxLen = 0
    
    for num in numCount:
        if num + 1 in numCount:
            maxLen = max(maxLen, numCount[num] + numCount[num + 1])
    
    return maxLen

# Example usage:
nums = [1, 3, 2, 2, 5, 2, 3, 7]
result = findLHS(nums)
print(result)  # Output: 5

#Q4.
def canPlaceFlowers(flowerbed, n):
    count = 0
    
    for i in range(len(flowerbed)):
        if (
            flowerbed[i] == 0 and
            (i - 1 < 0 or flowerbed[i - 1] == 0) and
            (i + 1 >= len(flowerbed) or flowerbed[i + 1] == 0)
        ):
            count += 1
            flowerbed[i] = 1
    
    return count >= n

# Example usage:
flowerbed = [1, 0, 0, 0, 1]
n = 1
result = canPlaceFlowers(flowerbed, n)
print(result)  # Output: True

#Q5.
def maximumProduct(nums):
    nums.sort()
    n = len(nums)
    max_product = nums[n-1] * nums[n-2] * nums[n-3]
    alternative_product = nums[0] * nums[1] * nums[n-1]
    return max(max_product, alternative_product)

# Example usage:
nums = [1, 2, 3]
result = maximumProduct(nums)
print(result)  # Output: 6

#Q6.
def search(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Example usage:
nums = [-1, 0, 3, 5, 9, 12]
target = 9
result = search(nums, target)
print(result)  # Output: 4


#Q7.
def isMonotonic(nums):
    increasing = True
    decreasing = True
    
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            increasing = False
        if nums[i] > nums[i-1]:
            decreasing = False
        if not increasing and not decreasing:
            return False
    
    return True

# Example usage:
nums = [1, 2, 2, 3]
result = isMonotonic(nums)
print(result)  # Output: True

#Q8.
def minimumScore(nums, k):
    nums.sort()
    n = len(nums)
    min_score = nums[n-1] - nums[0]
    
    for i in range(n-1):
        min_value = min(nums[0], nums[i+1]-k)
        max_value = max(nums[n-1], nums[i]+k)
        min_score = min(min_score, max_value - min_value)
    
    return min_score

# Example usage:
nums = [1]
k = 0
result = minimumScore(nums, k)
print(result)  # Output: 0


