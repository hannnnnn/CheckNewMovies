import datetime
import requests
import re
from bs4 import BeautifulSoup

# today = datetime.date.today().strftime("%Y%m%d")
# yesterday = (datetime.date.today()-datetime.timedelta(days=1)).strftime("%Y%m%d")
today = "20240218"
yesterday = "20240216"
days = [yesterday,today]
# print(f"/html/gndy/dyzz/{date}/.*")
# print("/html/gndy/dyzz/%s/.*" %date)
# print("/html/gndy/dyzz/{0}/.*".format(date))

cookies = {
    'googlesearch': 'False',
    '1707995034153': 'undefined',
    'crisp-client%2Fsession%2Fc6676a05-9c7c-4272-be79-c1818f47ad91': 'session_da7bed5f-afed-47a3-ba4c-58793104a181',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': 'googlesearch=False; 1707995034153=undefined; crisp-client%2Fsession%2Fc6676a05-9c7c-4272-be79-c1818f47ad91=session_da7bed5f-afed-47a3-ba4c-58793104a181',
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

url = 'https://www.dytt8.com/'
response = requests.get(url=url)
response.encoding = "gbk"
content = BeautifulSoup(response.text, "lxml")

def get_rating (url):
    # 发送 HTTP 请求获取网页内容
    response = requests.get(url)
    response.encoding = 'gbk'
    # 使用 BeautifulSoup 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 找到电影名称
    movie_name = soup.find('div', class_='title_all').h1.text.strip()

    # 找到豆瓣评分和 IMDB 评分所在的标签
    info_tags = soup.find_all('div', class_='co_content8')
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


for content2 in content.select(".bd3r",limit = 1):
    for day in days:
        movies = content2.findAll(name = "a", attrs = {"href" : re.compile("/html/gndy/dyzz/{0}/.*".format(day))})
        maglink = []
        for movie_name in movies:
            print(movie_name.string,end=' ')
            # print(url+movie_name.attrs['href'])
            detail_url = url+movie_name.attrs['href']
            get_rating(detail_url)
            detail_page = requests.get(detail_url, cookies=cookies, headers=headers)
            detail_page.encoding = "gbk"
            detail_content = BeautifulSoup(detail_page.text, "lxml")
            # detail_content = detail_content.select("#Zoom a")
            # for whatiwant in detail_content:
            #     print(whatiwant.attrs['href'])
            # print(detail_content[0].attrs['href'])
            temp = detail_content.find_all('a', attrs={"href" : re.compile("magnet.*")})
            # maglink.append(temp[0]['href'])
            print(temp[0]['href'])







# print(content.head.children)
#
# for child in content.div.children:
#     print(child)

# print(content.select("head"))
# for i in content.select("head"):
#     print(i.select("meta"))
# print(content.find_all("a",string=re.compile('.*3年剧情《金手指》HD国粤')))

