a = [1,2,3,4]

try:
  # index 4 does not exist in a
  print(a[4])
except:
  print("Index 4 does not exists in the list")
finally:
  print("I run not matter what")

def get_remainder(a,b):
  if b == 0:
    # raise Exception("exception message")
    raise "Division by Zero Not Supported"
  else:
    remainder = a%b
    return remainder

try:
  get_remainder(10,0)
except:
  print("Exception Raised")