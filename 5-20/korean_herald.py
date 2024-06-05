# Using Python and what you've learned so far, retrieve the "Most Popular"
# article headlines from the Korea Herald website. List the headlines in
# the following format:
# [1]: Headline 1
# [2]: Headline 2
# [n]: Headline n

import requests

r = requests.get("https://www.koreaherald.com/")

html_content = r.text

# html_find = html_content.find("popular_list")
# popular_list = html_content[html_find:html_find + 10000]
# # print("AAAAA", popular_list, "AAAAA")
# popular_list_lines = []
# popular_line = popular_list.find()

# html_content.split('<p class="news_title">')
print(html_content.split('<p class="news_title">'))


