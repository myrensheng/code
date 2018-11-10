from wsgiref.simple_server import make_server
from myapplication import app

# 创建服务，和ningx服务器一样，非常简单的一个服务器
# 的一个参数是服务器地址：可以写localhost/127.0.0.1/''
# 第二个参数是端口，不要用80，
# 第三个参数是自己的应用，可以是一个函数或者是一个可调用对象
server = make_server('',8000,app)
print("服务器启动....")
server.serve_forever()