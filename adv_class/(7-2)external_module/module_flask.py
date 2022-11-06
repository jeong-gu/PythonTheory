#파이썬에서는 웹개발을 할 때 보통 Django나 Flask를 이용합니다.
#Django는 매우 다양한 기능을 제공하는 웹 개발 프레임워크입니다.
#Flask는 작은 기능만을 제공하는 웹 개방 프레임워크입니다.

from flask import Flask

app = Flask(__name__)


@app.route("/")  #데코레이터
def hello():
    return "<h1>Hello World!</h1>"


#이거 솔직히 이해 안됌.
