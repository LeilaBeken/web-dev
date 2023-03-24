def make_bricks(small, big, goal):
  while goal >= 5 and big > 0:
    goal -= 5
    big-=1
  return goal <= small

def no_teen_sum(a, b, c):
  sum = 0
  for i in list([a, b, c]):
    if i in range(13, 15) or i in range(17, 20): i = 0
    sum+=i
  return sum

def make_chocolate(small, big, goal):
  g = int(goal/5)
  if g <= big:
    return goal-g*5 if goal-g*5 <= small else -1
  else:
    goal -= (big*5)
    return goal if goal <= small else -1

def lone_sum(a, b, c):
  if a == b and b == c:
    a = b = c = 0
  elif a == b:
    a = b = 0
  elif a == c:
    a = c = 0
  elif c == b:
    c = b = 0
  return a + b + c

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)

def round10(s):
  return s+10-s%10 if s%10>=5 else s-s%10

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  elif b == 13:
    return a
  elif c == 13:
    return a + b
  else: return a+b+c


def close_far(a, b, c):
  return gg(a, b, c) or gg(a, c, b)


def gg(a, b, c):
  return abs(a - b) <= 1 and abs(a - c) >= 2 and abs(b - c) >= 2