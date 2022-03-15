import re
text1 = "alphanumeric@example.org"
text2 = "alphanumeric@long.subdomain.more.subdomain.domain.org"
r1 = re.compile(r'[a-zA-Z0-9]+@[a-zA-Z]+(\.[a-zA-Z]+)+')
print(r1.match(text1).group())
print(r1.match(text2).group())