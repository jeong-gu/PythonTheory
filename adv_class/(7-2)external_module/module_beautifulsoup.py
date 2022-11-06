#Beautiful Soup는 웹 페이지 분석 모듈입니다.
#RSS 기상서비스를 실시간으로 이용

from bs4 import BeautifulSoup
from urllib import request

target = request.urlopen(
    "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, "html.parser")

for location in soup.select("location"):
    print("도시: ", location.select_one("city").string)
    print("날씨: ", location.select_one("wf").string)
    print("최저기온: ", location.select_one("tmn").string)
    print("최고기온: ", location.select_one("tmx").string)
    print("----------")
    print("----------")
