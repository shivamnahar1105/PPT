#Q1.
def threeSumClosest(nums, target):
    nums.sort()
    n = len(nums)
    closest_sum = float('inf')

    for i in range(n - 2):
        left = i + 1
        right = n - 1

        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]

            if current_sum == target:
                return current_sum

            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            if current_sum > target:
                right -= 1
            else:
                left += 1

    return closest_sum

  
  nums = [-1, 2, 1, -4]
target = 1

result = threeSumClosest(nums, target)
print(result)


#Q2. 
def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            left = j + 1
            right = n - 1

            while left < right:
                current_sum = nums[i] + nums[j] + nums[left] + nums[right]

                if current_sum == target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif current_sum > target:
                    right -= 1
                else:
                    left += 1

    return result

  nums = [1, 0, -1, 0, -2, 2]
target = 0

result = fourSum(nums, target)
print(result)


#Q3.

def nextPermutation(nums):
    n = len(nums)
    i = n - 2

    # Find the first element that can be modified
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i >= 0:
        j = n - 1

        # Find the first element greater than nums[i]
        while j > i and nums[j] <= nums[i]:
            j -= 1

        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]

    # Reverse the subarray from i+1 to the end
    left = i + 1
    right = n - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

# Example usage
nums = [1, 2, 3]
nextPermutation(nums)
print(nums)  # Output: [1, 3, 2]


#Q4.
def searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

# Example usage
nums = [1, 3, 5, 6]
target = 5
index = searchInsert(nums, target)
print(index)  # Output: 2


#Q5.
def plusOne(digits):
    carry = 1
    n = len(digits)

    for i in range(n - 1, -1, -1):
        digits[i] += carry

        if digits[i] == 10:
            digits[i] = 0
        else:
            break

    if carry == 1:
        digits.insert(0, 1)

    return digits

# Example usage
digits = [1, 2, 3]
result = plusOne(digits)
print(result)  # Output: [1, 2, 4]

#Q6.
def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# Example usage
nums = [2, 2, 1]
result = singleNumber(nums)
print(result)  # Output: 1

#Q7.
def findMissingRanges(nums, lower, upper):
    result = []
    start = lower

    for num in nums:
        if num > start:
            if start == num - 1:
                result.append(str(start))
            else:
                result.append(str(start) + "->" + str(num - 1))
            start = num + 1

    if start <= upper:
        result.append(str(start) + "->" + str(upper))

    return result

# Example usage
nums = [0, 1, 3, 50, 75]
lower = 0
upper = 99
result = findMissingRanges(nums, lower, upper)
print(result)  # Output: ['2', '4->49', '51->74', '76->99']

#Q8.
def canAttendMeetings(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time

    for i in range(1, len(intervals)):
        if intervals[i][0] < intervals[i-1][1]:
            return False

    return True

# Example usage
intervals = [[0, 30], [5, 10], [15, 20]]
result = canAttendMeetings(intervals)
print(result)  # Output: False


