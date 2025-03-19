def rotate_left3(nums):
  temp = nums[0]
  nums[0] = nums[2]
  nums[2] = temp
  temp = nums[0]
  nums[0] = nums[1]
  nums[1] = temp
  return nums
nums = [1, 2, 3]
