def hello_name(name):
  return "Hello " + name + '!'

def make_out_word(out, word):
  return out[0:2] + word  + out[2:4]

def first_half(str):
  return str[0:(len(str)/2)]

def non_start(a, b):
  return a[1:] + b[1:]

def make_abba(a, b):
  return a+b+b+a

def extra_end(str):
  return str[(len(str)-2):]*3

def without_end(str):
  return str[1:-1]

def left2(str):
  return str[2:] + str[:2]

def make_tags(tag, word):
  return "<{0}>{1}</{0}>".format(tag, word)

def first_two(str):
  return str[:2]


def combo_string(a, b):
  if len(a) > len(b):
    return b+a+b
  return a + b + a