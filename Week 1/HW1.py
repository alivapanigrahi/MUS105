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

# remove substring function
def remove_substring_instances(in_str, substr):
  new_string = in_str.replace(in_str, substr)
  return(new_string, in_str.count(substr))
print(remove_substring_instances("hello", "ell"))

# list to string function
def list_to_str(l):
  for i in l:
    return(str(i))
print(list_to_str([1, 2, 3, 4, 5]))