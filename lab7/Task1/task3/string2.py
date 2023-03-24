def double_char(str):
  res = ""
  for i in str:
    res+=(i*2)
  return res

def count_code(str):
  i = 0
  cnt = 0
  while i < len(str)-3:
    if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
      cnt+=1
      i+=4
    else: i+=1
  return cnt

def count_hi(str):
  i = 0
  cnt = 0
  while i < len(str)-1:
    if str[i] == 'h' and str[i+1] == 'i':
      cnt+=1
      i+=2
    else: i+=1
  return cnt

def end_other(a, b):
  return a.lower().endswith(b.lower()) or b.lower().endswith(a.lower())

def cat_dog(str):
  return str.count('cat') == str.count('dog')

def xyz_there(str):
  return bool(str.count('xyz')-str.count('.xyz'))