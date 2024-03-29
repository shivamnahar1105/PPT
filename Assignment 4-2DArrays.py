#Q1.

def commonElements(arr1, arr2, arr3):
    p1, p2, p3 = 0, 0, 0
    result = []

    while p1 < len(arr1) and p2 < len(arr2) and p3 < len(arr3):
        if arr1[p1] == arr2[p2] == arr3[p3]:
            result.append(arr1[p1])
            p1 += 1
            p2 += 1
            p3 += 1
        elif arr1[p1] <= arr2[p2] and arr1[p1] <= arr3[p3]:
            p1 += 1
        elif arr2[p2] <= arr1[p1] and arr2[p2] <= arr3[p3]:
            p2 += 1
        else:
            p3 += 1

    return result

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 5, 7, 9]
arr3 = [1, 3, 4, 5, 8]
result = commonElements(arr1, arr2, arr3)
print(result)  # Output: [1, 5]

#Q2.
def findDisappearedNumbers(nums1, nums2):
    set_nums1 = set(nums1)
    set_nums2 = set(nums2)

    distinct_nums1 = list(set_nums1 - set_nums2)
    distinct_nums2 = list(set_nums2 - set_nums1)

    return [distinct_nums1, distinct_nums2]

# Example usage
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = findDisappearedNumbers(nums1, nums2)
print(result)  # Output: [[1, 3], [4, 6]]


#Q3.

def transpose(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])
    transpose = [[0] * num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transpose[j][i] = matrix[i][j]

    return transpose

# Example usage
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose(matrix)
for row in result:
    print(row)

#Q4.
def arrayPairSum(nums):
    nums.sort()
    max_sum = 0

    for i in range(0, len(nums), 2):
        max_sum += min(nums[i], nums[i+1])

    return max_sum

# Example usage
nums = [1, 4, 3, 2]
result = arrayPairSum(nums)
print(result)  # Output: 4

    
    
