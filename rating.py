import requests

from bs4 import BeautifulSoup
# 发送 HTTP 请求获取网页内容
response = requests.get("https://www.dytt8.com/html/gndy/dyzz/20240218/64675.html")
response.encoding = 'gbk'
# 使用 BeautifulSoup 解析网页内容
soup = BeautifulSoup(response.text, 'html.parser')

# 找到电影名称
movie_name = soup.find('div', class_='title_all').h1

# 找到豆瓣评分和 IMDB 评分所在的标签
info_tags = soup.find_all('div', class_='co_content8')
for tag in info_tags:
    print(tag.get_text().strip())

# 从标签中提取豆瓣评分和 IMDB 评分
douban_rating = None
imdb_rating = None

for tag in info_tags:
    text = tag.get_text()
    if '◎豆瓣评分' in text:
        douban_rating = text.split('◎豆瓣评分')[1].split('from')[0].strip()
    if '◎IMDb评分' in text:
        imdb_rating = text.split('◎IMDb评分')[1].split('from')[0].strip()

# 打印电影名称、豆瓣评分和 IMDB 评分

print('豆瓣评分:', douban_rating,end='  ')
print('IMDB 评分:', imdb_rating)