def centered_average(nums):
    nums.sort()  
    trimmed = nums[1:-1]  
    return sum(trimmed) // len(trimmed)  
