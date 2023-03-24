def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

def common_end(a, b):
  return a[0] == b[0] or a[-1] == b[-1]

def reverse3(nums):
  return nums[::-1]

def middle_way(a, b):
  return list([a[1], b[1]])

def same_first_last(nums):
  return nums[0] == nums[len(nums)-1]

def sum3(nums):
  return sum(nums)

def max_end3(nums):
  return list([nums[0] if nums[0] > nums[2] else nums[2]]*3)

def make_ends(nums):
  return list([nums[0], nums[-1]])

def make_pi():
  return list([3, 1, 4])

def rotate_left3(nums):
  return nums[1:] + nums[:1]

def sum2(nums):
    if (len(nums) == 0): return 0
    if (len(nums) == 1): return nums[0]
    return nums[0] + nums[1]

def has23(nums):
  return (2 in nums) or (3 in nums)