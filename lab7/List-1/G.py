def max_end3(nums):
  if nums[2] > nums[0]:
    nums[0] = nums[2]
    nums[1] = nums[2]
  else:
    nums[2] = nums[0]
    nums[1] = nums[0]
  return nums
nums = [1, 2, 3]
