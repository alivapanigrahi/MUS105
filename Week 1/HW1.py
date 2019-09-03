# power function
def power(base, exp):
  result = 1
  for i in range(exp):
    result *= base
  return result
print(power(2, 3))

# sum of list elements function
def list_sum(l):
  return sum(l)
print(list_sum([1,2.0,3,4.0]))