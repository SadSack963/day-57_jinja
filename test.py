# import time
# current_year = time.localtime().tm_year
# print(current_year.tm_year)


# import datetime as dt
# current_year = dt.datetime.now().year
# print(current_year)


# import requests
# name = 'john'
# age_url = 'https://api.agify.io'
# query = {'name': name}
# response = requests.get(url=url, params=query)
# response.raise_for_status()
# age = response.json()["age"]
# print(age)
#
# name = 'john'
# gender_url = 'https://api.genderize.io'
# query = {'name': name}
# response = requests.get(url=url, params=query)
# response.raise_for_status()
# gender = response.json()["gender"]
# print(gender)


import requests
blog_url = 'https://api.npoint.io/ed99320662742443cc5b'
response = requests.get(url=blog_url)
response.raise_for_status()
all_blogs = response.json()
print(all_blogs)
