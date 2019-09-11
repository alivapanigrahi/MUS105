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
    (str(i))
    i += 1
  return(str(i) + str(i) + str(i) + str(i))
print(list_to_str([1, 2, 3, 4, 5]))

# string to int function
def str_to_int(num_string):
  a = -1
  if num_string[0:2] == "0b":
    return int(num_string, 2)
  elif num_string[0:2] == "0o":
    return int(num_string, 8)
  elif num_string[0:2] == "0x":
    return int(num_string, 16)
  elif type(int(num_string)) == int:
    return int(num_string)
  else:
    return a
print(str_to_int("0b100"))

# print christmas tree function
def print_christmas_tree(size):
  for i in range (size):
    tree = ' '*(size-i-1) + '*'*(2*i+1) 
    print(tree)
  print(' ' * (size-1) + "*")
print(print_christmas_tree(4))
