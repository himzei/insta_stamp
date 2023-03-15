import re
import requests 
from rest_framework.views import APIView 
from rest_framework.response import Response
from bs4 import BeautifulSoup


class Crawling(APIView): 
    
    def get(self, request): 
        keyword = "존잼"
        pattern = '#([0-9a-zA-Z가-힣]*)'
        hash_w = re.compile(pattern)

        stamp_url = "https://www.instagram.com/p/CY3kQa7vmdu/"
        url = f"{stamp_url}?__a=1" # 크롤링할 게시물 URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        data = soup.find("title").text
        hashtags = hash_w.findall(data)

        userid = data.split("on Instagram")[0].strip()
        print("userid :", userid)

        for tag in hashtags: 
            if keyword == tag: 
                stamp = True
            else:
                stamp = False

        return Response({"ok": True, "userid": userid, "해시태그 인증유무": stamp})


