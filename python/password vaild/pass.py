import re

# password
pswd = 'XdsE83&!'
reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"

# compiling regex
match_re = re.compile(reg)

# searching regex
res = re.search(match_re, pswd)

# validating conditions
if res:
   print("Valid Password")
else:
   print("Invalid Password")


# email

def solve(s):
   pat = "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$"
   if re.match(pat,s):
      return True
   return False

s = "popular_website15@comPany.com"
print(solve(s))



