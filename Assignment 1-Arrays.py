
# Q1.
def twoSum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = twoSum(nums, target)
print(result)  # Output: [0, 1]


#Q2.
def removeElement(nums, val):
    i = 0
    j = 0
    while i < len(nums):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
        i += 1
    return j

# Example usage:
nums = [3, 2, 2, 3]
val = 3
count = removeElement(nums, val)
print(count)  # Output: 2
print(nums)   # Output: [2, 2, _, _] (where "_" represents any value)

#Q3.

def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    
    return left

# Example usage:
nums = [1, 3, 5, 6]
target = 5
index = searchInsert(nums, target)
print(index)  # Output: 2


#Q4.
def plusOne(digits):
    carry = 1
    for i in range(len(digits)-1, -1, -1):
        digits[i] += carry
        if digits[i] == 10:
            digits[i] = 0
        else:
            carry = 0
            break
    if carry == 1:
        digits.insert(0, 1)
    return digits

# Example usage:
digits = [1, 2, 3]
result = plusOne(digits)
print(result)  # Output: [1, 2, 4]

#Q5.
def merge(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    p = m + n - 1
    
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1

# Example usage:
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge(nums1, m, nums2, n)
print(nums1)  # Output: [1, 2, 2, 3, 5, 6]

#Q6.
def containsDuplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example usage:
nums = [1, 2, 3, 1]
result = containsDuplicate(nums)
print(result)  # Output: True

#Q7.
def moveZeroes(nums):
    left = 0
    right = 0
    n = len(nums)
    
    while right < n:
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1
    
    while left < n:
        nums[left] = 0
        left += 1

# Example usage:
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

#Q8.
def findErrorNums(nums):
    numSet = set()
    duplicate = 0
    missing = 0
    n = len(nums)
    
    for num in nums:
        if num not in numSet:
            numSet.add(num)
        else:
            duplicate = num
    
    expectedSum = (n * (n + 1)) // 2
    actualSum = sum(nums)
    missing = expectedSum - actualSum + duplicate
    
    return [duplicate, missing]

# Example usage:
nums = [1, 2, 2, 4]
result = findErrorNums(nums)
print(result)  # Output: [2, 3]
