from urllib import request ,parse,error

if __name__ == '__main__':
    try:
        url = 'http://www.youdao.com/w/computer/'
        # proxy = {'http':'121.40.183.166'}
        # proxy_handler = request.ProxyHandler(proxy)
        # opener = request.build_opener(proxy_handler)
        # request.install_opener(opener)

        data = {'kw':'computer'}
        data = parse.urlencode(data).encode('utf-8')
        headers = {'Content-Length':len(data)}
        req = request.Request(url)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36")
        rs = request.urlopen(req)
        html = rs.read().decode('utf-8')

        print(html)
    except error.URLError  as  e:
        print('URLError{0}', format(e))







