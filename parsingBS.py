from bs4 import BeautifulSoup
from urllib import request
import requests


def get_content(url):
    result = []  # 파일명과 파일경로가 저장될 리스트를 정의함
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    req = requests.get(url, headers=headers)

    if req.status_code == 200:
        content = req.content
        soup = BeautifulSoup(content, 'html.parser')
        writeDate = soup.select_one('#dailybible_info').text
        title = soup.select_one('#bible_text').text
        bibleInfo = soup.select_one('#bibleinfo_box').text
        bibleDocu = soup.select_one('#body_cont_3').text
        audio = soup.select_one('#video > source')['src']
        result = [writeDate, title, bibleInfo, bibleDocu, audio]
    else:
        result = {}
    return result


url = 'https://sum.su.or.kr:8888/bible/today'
a = get_content(url)

wdate = a[0].strip()
title = a[1].strip()
bibleInfo = a[2].strip()
bibleDocu = a[3].strip()
bibleDocu = bibleDocu.replace("  ", "")
audio = a[4].strip()
message = f"{title}\n\n{bibleInfo}\n\n{bibleDocu}\n\n{audio}"

print(message)