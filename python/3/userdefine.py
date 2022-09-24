# Python Built in Functions
# Return the absolute value of a number:
x = abs(-7.25)
print(x)
# Filter the array, and return a new array with only the values equal to or above 18:
ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)


# user defined functions 

# Function below finds the sum of its two parameters
def sum(val1, val2): 
	return val1 + val2;

print(sum(3, 4))

# Function below accepts any number of parameters
def sum_numbers(*vals):
	total = 0
	for val in vals: 
		total+=val
	return total

print(sum_numbers(1, 2, 3, 4)) # 10