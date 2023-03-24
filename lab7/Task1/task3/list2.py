def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      count += 1
  return count

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  nums.sort()
  count = 0
  total = 0
  for i in range(1, len(nums) - 1):
    count += 1
    total += nums[i]
  return total / count

def sum13(nums):
  total = 0
  skip = False
  if len(nums) == 0:
    return 0
  else:
    for i in range(len(nums)):
      if nums[i] == 13:
        skip = True
      elif skip:
        skip = False
      else:
        total += nums[i]
  return total

def sum67(nums):
  total = 0
  skip = False
  for i in range(len(nums)):
    if nums[i] == 6:
      skip = True
    elif nums[i] == 7 and skip:
      skip = False
    elif not skip:
      total += nums[i]
  return total

def has22(nums):
  has2 = False
  for i in range(len(nums)):
    if has2 and nums[i] == 2:
      return True
    elif nums[i] == 2:
      has2 = True
    else:
      has2 = False
  return False