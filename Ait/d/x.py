# x = str(input("What is your no.:- "))
# print(x)
# if(x[0] in "479"):
#     print("okay your number is selected! thanks for visit! :)")
# else:
#     print('sorry! this number is other country')
  

import phonenumbers
from phonenumbers.phonenumberutil import (
    region_code_for_country_code,
    region_code_for_number,
)

pn = phonenumbers.parse(input('enter mob.no'))
print(region_code_for_country_code(pn.country_code))