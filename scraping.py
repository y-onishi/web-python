import requests
from bs4 import BeautifulSoup

#ユニバーサルミュージックビートルズ公式ニュース
r = requests.get("https://www.universal-music.co.jp/the-beatles/news/")
soup = BeautifulSoup(r.content, "lxml")

#タイトル・リンク先をスクレイピング
contents = [(list_row_detail.contents[3].string, a_tag.get('href')) \
    for list_row_detail, a_tag in \
    zip(soup.select("div.list-row a div"), soup.select("div.list-row a"))]
