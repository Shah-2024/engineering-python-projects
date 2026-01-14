numbers = [10, 20, 30, 40, 50]

#Mean Function
def mean(nums):
    total = 0
    for n in nums: total += n
    return total / len(nums)

#Min function
def minimum(nums):
    min_value = nums[0]
    for n in nums:
        if n < min_value: min_value = n
    return min_value
    
#Max function
def maximum(nums):
    max_value = nums[0]
    for n in nums:
        if n > max_value: max_value = n
    return max_value



#Print formatted results
print("Statistics Results")
print("-------------------")
print("Mean:", mean(numbers))
print("Min :", minimum(numbers))
print("Max :", maximum(numbers))