from urllib.parse import parse_qs
from hashlib import md5
from models import Model
import jinja2



def load_html(filename):
    path = "./templates/" + filename
    with open(path,'rb') as fp:
        return fp.read()  #返回字节字符串

def index(environ,start_response):
    start_response("200 ok", [("ContentType", 'text/html')])
    content = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Title</title>
            </head>
            <body>
            你好
            </body>
            </html>
                """
    return [content.encode('utf8')]



def login(environ,start_response):
    start_response("200 ok", [("ContentType", 'text/html')])
    return [load_html('login.html')]

def dologin(environ,start_response):
    start_response("200 ok", [("ContentType", 'text/html')])
    if environ['REQUEST_METHOD']  == 'GET':
        # get传参方式
        data = parse_qs(environ['QUERY_STRING'])

    else:   # post
        try:
            length = int(environ.get('CONTENT_LENGTH',0))
        except Exception as e:
            length = 0
        data = environ['wsgi.input'].read(length)
        data = data.decode('utf8')
        print(data)
        data = parse_qs(data)
    username = data.get('username', [''])[0]
    password = data.get('password', [''])[0]
    m5 = md5()
    m5.update(password.encode('utf8'))
    password = m5.hexdigest()

    model = Model('user')
    res = model.field('password').where("uname='%s'" % username).select()
    print(res)
    if len(res) > 0:
        tmp = res[0]['password']
        print(tmp)
        if tmp == password:
            print("ok")
            users = model.field("uname,password").select()
            env = jinja2.Environment(loader=jinja2.FileSystemLoader('./templates'))
            temp = env.get_template('userlist.html')

            return [temp.render(data=users).encode('utf8')]
        else:
            return ["密码错误，非法用户，有多远滚多远".encode('utf8')]
    else:
        return ["用户名错误，非法用户，有多远滚多远".encode('utf8')]


