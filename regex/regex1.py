import re

phonenum= re.compile(r'\d{3}-\d{3}-\d{4}')
nums = phonenum.search('my num is 982-182-6531. Komal\'s num is 982-182-6532. His dad has a mobile phone and a telephone. His telephone number is 056-524321. While his phone number is 984-505-6778')
print('Phone numbers found are:'+ nums.group())