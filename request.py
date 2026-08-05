# import requests
# a=requests.get("https://github.com/MoreshwarPachbhai")
# print(a.json())

# import requests

# a = requests.get("https://api.github.com/users/MoreshwarPachbhai")

# print(a.status_code)
# print(a.json())


import requests

a = requests.get("https://www.instagram.com/maisamayhoon?igsh=MWIzenYzanZzNXdybA==")

print(a.status_code)
print(a.text[:300])   # Print the first 300 characters