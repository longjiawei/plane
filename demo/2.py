from http import cookiejar
from urllib import request, parse

cookie  = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie) #创建cookie管理器
http_handler = request.HTTPHandler()  #创建http管理器
https_handler = request.HTTPSHandler()  #创建https管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)
def login():
    url = "http://www.scpta.gov.cn/log/login.do"
    data = {
        "email": "8188461126",
        "password": "long8123044"
    }
    data = parse.urlencode(data)
    req = request.Request(url, data = data.encode())
    rsp = opener.open(req)
def getHomePage():
    url = "http://zhibo.renren.com/top"

    # 如果已经执行了login函数，则opener自动已经包含相应的cookie值
    rsp = opener.open(url)


    html = rsp.read().decode()
    with open("rsp.html", "w") as f:
        f.write(html)

if __name__ == '__main__':
    login()
    getHomePage()




