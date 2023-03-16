import re
import requests 
from rest_framework.views import APIView 
from rest_framework.response import Response
from bs4 import BeautifulSoup


class Crawling(APIView): 
    
    def post(self, request): 
        url = request.data.get("url")
        stamp = False

        keyword = ["코딩", "대광로제비앙"]
        pattern = '#([0-9a-zA-Z가-힣]*)'
        hash_w = re.compile(pattern)

        stamp_url = url
        url = f"{stamp_url}?__a=1" # 크롤링할 게시물 URL
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        data = soup.find("title").text
        hashtags = hash_w.findall(data)

        userid = data.split("on Instagram")[0].strip()
        print("userid :", userid)

        if any(x in hashtags for x in keyword): 
            stamp = True
        

        return Response({"ok": True, "stamp": stamp, "userid": userid})


