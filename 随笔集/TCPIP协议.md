#### 4.TCP编程【掌握】

##### 4.1tcp概念

> Socket：套接字，应用程序通常需要通过套接字向网络发出请求或者应答网络请求，使得主机或者一台计算机的进程间可以通信
>
> Socket是网络编程中的一个抽象概念，通常使用Socket表示打开了一个网络连接，打开一个Socket需要知道目标计算机的ip地址，端口号，指定协议
>
> TCP：Transmission  Control  Protocol ,传输控制协议，基于字节流的传输层通信协议
>
> 特点：
>
> ​	a.安全的【确保接收方完全正确的接收到消息】
>
> ​	b.面向连接的【面向连接的协议，发送消息之前，需要建立连接，所以TCP需要耗费时间】
>
> ​	c.数据传输的效率比较低
>
> ​	d.一旦双方建立连接，可以按照统一的格式传输数据，数据的大小是没有限制的
>
> 使用经典的三次握手建立连接
>
> ​	a.客户端向服务端发起请求：第一次握手
>
> ​	b.服务端收到请求之后，回客户端一个响应：第二次握手
>
> ​	c.客户端收到服务端的响应之后，回给服务端一个确认信息：第三次握手
>
> 注意：使用tcp来实现数据的传输需要有发送方和接收方，但是两个通信实体之间并没有严格的客户端和服务端之分，在两个通信实体进行通信之前，必须有一个通信实体做出主动姿态，主动发起连接请求

##### 4.2socket通信流程

> 创建tcp连接时，主动发起请求的叫做客户端，被动接受请求的叫做服务端

##### 4.3tcp编程

> 流程
>
> client.py
>
> ```python
> #发送方【客户端】
> 
> import  socket
> 
> #1.客户端创建socket
> client = socket.socket()
> 
> #2.客户端打开socket，根据服务端的ip地址和端口号试图连接服务端的socket
> """
> connet(元组)
> 元组：ip地址和端口
> """
> client.connect(("10.12.153.31",8888))
> 
> #3.客户端向服务端发送消息【客户端向socket写入信息】
> """
> sendall(string,flag)
> string:将要发送给服务端的数据，注意：需要将字符串类型转换为字节类型
> 工作原理：内部通过递归调用send，将所有的内容全部发送出去
> 返回值：成功则返回None，失败则会抛出异常
> """
> client.sendall(bytes("Python1804你好",encoding="utf-8"))
> #bytes
> 
> #4.关闭socket
> client.close()
> ```
>
> server.py
>
> ```python
> #接收方【服务端】
> import socket
> 
> #服务端流程描述
> #1.创建socket对象
> #根据地址类型，socket类型，协议创建socket
> server = socket.socket()
> 
> #2.服务端为socket绑定ip地址和端口号
> #bind(元组)：将IP地址和端口绑定到指定socket上，ip地址和端口号以元组的形式传参
> #注意8888表示的是服务端的端口，客户端的端口系统自动分配
> ip_port = ("10.12.153.31",8888)
> server.bind(ip_port)
> 
> #3.服务端socket监听端口号请求，随时准备接受客户端发来的连接
> #注意：此时，只是在监听，服务器的socket并没有被打开
> """
> listen(backlog)
> 开始监听传入的连接，backlog指定在拒绝连接之前，可以挂起的最大的连接数量
> backlog等于5，表示内核已经连接到了请求，但是服务器还没有调用accept进行处理
> 注意：backlog不能无限大，因为在内核中需要维持连接队列
> """
> server.listen(5)
> 
> #问题：代码执行到listen，会产生阻塞，直到有客户端连接到服务端
> print("server waiting.......")
> 
> 
> #4.接收客户端发来的请求
> """
> accept():服务端socket接收客户端的socket请求，服务端socket是被动打开的，开始接收客户端的请求
> 直到客户端返回连接信息【三次握手】，此时，socket会进入阻塞状态，
> accept函数会一直等待客户端返回连接信息，开始接收下一个客户端的请求
> 返回值：（conn,addr）:其中conn代表是连接到的客户端对象，可以接收和发送数据，addr代表的是连接到的客户端的地址
> """
> conn,addr = server.accept()
> 
> 
> #5.接收客户端的消息
> """
> recv(字节数):接收套接字的数据，返回值为字符串，注意：接收到的数据为字节类型，所以为了能够识别，需要转换为字符串
> """
> client_data = conn.recv(1024)
> print("客户端%s发来的消息:%s" %(addr,str(client_data,"utf-8")))
> 
> 
> #6.关闭socket
> server.close()
> ```
>
> 循环发送数据和接收数据
>
> server.py
>
> ```python
> import  socket
> 
> server = socket.socket()
> 
> server.bind(("10.12.153.31",9999))
> 
> server.listen(5)
> print("服务端启动成功")
> 
> clientSocket,clientAddress = server.accept()
> print("%s-----%s连接成功" %(str(clientSocket),clientAddress))
> 
> while True:
>     #接收客户端发来的内容
>     data = clientSocket.recv(1024)
>     #将字节类型转换为字符串类型：解码
>     print("客户端说：" + data.decode("utf-8"))
>     sendData = input("请输入要回复给客户端的内容：")
>     clientSocket.send(sendData.encode("utf-8"))
> 
>     if data.decode("utf-8") == "bye" or data.decode("utf-8") == "再见":
>         break
> ```
>
> client.py
>
> ```python
> import  socket
> 
> client = socket.socket()
> 
> 
> client.connect(("10.12.153.31",9999))
> 
> while True:
>     #发送
>     data = input("请输入要发送给服务端的内容：")
>     #将字符串转换为字节类型：编码
>     client.send(data.encode("utf-8"))
>     #接收
>     info = client.recv(1024)
>     print("服务端说：" + info.decode("utf-8"))
> 
>     if data == "bye" or data == "再见" or info.decode("utf-8") == "bye":
>         break
> ```

#### 5.UDP编程

> 【面试题：tcp和udp之间的区别】
>
> User Datagram  Protocol，用户数据包协议，提供面向事务的简单不可靠的信息传送
>
> 特点：
>
> ​	a.不安全的【发送方所发送的数据包并不一定以相同的次序到达接收方，或者接收方不一定能够接收到】，比如：飞秋
>
> ​	b.无连接的【每个数据包【报】中给出了完整的地址信息，因此无需建立发送方和接收方之间的连接】
>
> ​	c.效率高，速度快
>
> ​	d.传输的数据有大小限制，每个被传输的数据包必须限定在64k以内
>
> 