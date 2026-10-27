# l1 = ["a","a","b","b","b","c","c","c","c"]
# freq = {}

# for item in l1:
#     freq[item] = freq.get(item,0) + 1

# print(freq)

import hashlib

password = "password123"

hashed = hashlib.sha512(password.encode()).hexdigest()
print(hashed)