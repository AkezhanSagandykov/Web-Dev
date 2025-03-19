def first_last6(nums):
  index = len(nums) - 1
  if nums[index] == 6 or nums[0] == 6:
    return True
  else:
    return False
nums = [1, 2, 6]