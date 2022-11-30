#  TODO: ValueError handling, min length check

import string
import random

length = int(input("Desired length of password (must be at least 4: "))

reqs = random.choice(string.ascii_lowercase) + random.choice(string.ascii_uppercase) + random.choice(string.digits) + random.choice(string.punctuation)

ascii_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

passw = ''

pass_chars = list(reqs)
for i in range(length-4):
	pass_chars += random.choice(ascii_chars)

while len(pass_chars) > 0:
	temp = random.choice(pass_chars)
	passw += temp
	pass_chars.remove(temp)
	
print(f'Generated password: {passw}')
