# Q1.
def mySqrt(x):
    if x == 0:
        return 0

    left, right = 1, x
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid > x:
            right = mid - 1
        else:
            left = mid + 1

#Q2.

def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

#Q3.

def missingNumber(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2

    for num in nums:
        expected_sum -= num

    return expected_sum

#Q4.

def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    # Find the meeting point
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Find the start of the cycle
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow


#Q5.

def intersection(nums1, nums2):
    set1 = set(nums1)
    set2 = set(nums2)

    return list(set1.intersection(set2))


#Q6.

def findMin(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    return nums[left]

#Q7.

def searchRange(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    if nums[left] != target:
        return [-1, -1]

    start = left
    right = len(nums) - 1

    while left < right:
        mid = (left + right + 1) // 2

        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid

    end = left

    return [start, end]


#Q8.

from collections import defaultdict

def intersect(nums1, nums2):
    freqMap = defaultdict(int)
    for num in nums1:
        freqMap[num] += 1

    intersection = []
    for num in nums2:
        if freqMap[num] > 0:
            intersection.append(num)
            freqMap[num] -= 1

    return intersection


