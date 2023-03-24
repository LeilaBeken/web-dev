def cigar_party(cigars, is_weekend):
  return cigars >= 40 and (cigars <= 60 or is_weekend)

def caught_speeding(speed, is_birthday):
  return 0 if speed <= 60 or (is_birthday and speed <= 65) else 1 if speed <= 80 or (is_birthday and speed <= 85) else 2

def love6(a, b):
  return 6 == a or b == 6 or a+b==6 or abs(a-b)==6

def date_fashion(you, date):
  return 0 if you <= 2 or date <= 2 else 2 if you >= 8 or date >= 8 else 1

def sorta_sum(a, b):
  return a+b if a+b not in range(10, 20) else 20

def in1to10(n, outside_mode):
  return (not outside_mode and n in range(1, 11)) or (outside_mode and n not in range(2, 10))

def squirrel_play(temp, is_summer):
  return temp in range(60, 91) or (is_summer and temp in range(60, 101))

def alarm_clock(day, vacation):
  return "7:00" if not vacation and day in range(1, 6) else "10:00" if (vacation and day in range(1, 6)) or not vacation else "off"

def near_ten(num):
  return num % 10 not in range(3, 8)