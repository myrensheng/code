import re
from urls import *

def app(environ,start_response):

    path_info = environ['PATH_INFO']
    print(path_info)
    path_info = path_info.strip('/') + '/'

    # 路由
    for pattern,func in urlspattern:
        # 和path_info 匹配
        if re.match(pattern,path_info):
            return func(environ,start_response)

    # 如果无法匹配，报404
    start_response("404 ok", [("ContentType", 'text/html')])
    return [b'File Not Found']
    # if path_info == '/login':
    #     return login(environ,start_response)
    # else:
    #     return index(environ,start_response)  #返回响应体内容，必须是可迭代对象，内容必须是字节流