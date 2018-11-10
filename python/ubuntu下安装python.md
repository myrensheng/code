## 1 切换用户操作

```linux
sudo su 
输入密码后切换到超级用户操作前面显示的是#
root@zhengshuai:/home/zhengshuai# sudo su zhengshuai

sudo su zhegnshuai
切换到其他用户前面显示$
zhengshuai@zhengshuai:~$ 
tree -L 1 查看目录
```

## 2 软件安装

### apt-get安装常用软件

```shell
$sudo apt-get install tree -y #安装软件【加上-y可以不用再装的过程输入yes
$sudo apt-get update #获取新的软件包
$sudo apt-get upgrade #升级有可用的更新软件包
$sudo apt-get remove 包名

 #安装常见的库
 $sudo apt-get update
 $sudo apt-get install man gcc  make  lsof ssh openssl tree vim dnsutils iputils-ping net-tools psmisc sysstat curl telnet traceroute wget libbz2-dev libpcre3 libpcre3-dev libreadline-dev libsqlite3-dev libssl-dev llvm zlib1g-dev git mysql-server mysql-client zip  p7zip
```

## 3 ubuntu安装python

pyenv是一个Python版本管理工具，它能够进行全局的Python版本切换，也可以为单个项目提供对应的Python版本。使用pyenv以后，可以在服务器上安装多个不同的Python版本。不同Python版本之间的切换也非常简单。pyenv官方地址https://github.com/pyenv/pyenv-installer

### 3.1 安装pyenv

```shell
1 安装pyenv，在命令行输入：
$ curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
如果安装了git，可以使用下面安装方式：
 $ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
2 安装结束后会有一个警告
WARNING: seems you still have not added 'pyenv' to the load path.
默认安装到当前用户的工作目录下的.pyenv。 将安装路径写入~/.bashrc
直接在命令行窗口输入：
export PATH="/home/zhu/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
但是有的可能写不进去，使用下面语句即可：
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
$ echo 'eval "$(pyenv init -)"' >> ~/.bashrc
$ exec $SHELL -l
#如果路径第一个结尾是shims则表示成功
/home/python/.pyenv/plugins/pyenv-virtualenv/shims:/home/python/.pyenv/shims:/home/python/.pyenv/bin:/home/python/bin:/home/python/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin
3 更新一下
$pyenv update
```

- 使用pyenv

```shell
1 查看pyenv当前支持的python版本
$pyenv install --list
2 列出当前ubuntu下可用的python版本
$pyenv versions
带*的是当前正在使用的版本，system默认是python2.7.12
3 切换python版本
$pyenv global 3.6.4
$python
4 删除指定的python版本
$pyenv uninstall 3.6.4
```

### 3.2安装virtualenv

virtualenv本身是一个独立的项目，用以隔离不同项目的工作环境。例如，项目A和项目B都是使用Python 2.7.13，但是，项目A需要使用Flask 0.8版本，项目B需要使用Flask 0.9版本。我们只要组合pyenv和virtualenv这两个工具，就能够构造Python和第三方库的任意版本组合，拥有了很好的灵活性，也避免了项目之间的相互干扰。

virtualenv本身是一个独立的工具，用户可以不使用pyenv单独使用virtualenv。但是，如果你使用了pyenv，就需要安装pyenv-virtualenv插件而不是virtualenv软件来使用virtualenv的功能。

项目主页：https://github.com/yyuu/pyenv-virtualenv

- 安装virtualenv（可选）

  如果是python3以上，安装完pyth就已经安装了virtualenv，就不用安装了

  ```
  #安装
  $ pip install virtualenv
  
  #或者，如果提示版本不匹配，可以使用--upgrade参数
  $ sudo pip install --upgrade virtualenv
  ```

- 使用virtualenv创建项目的虚拟环境

**一个项目创建一个virtualenv的虚拟环境**，在这个环境中，可以用pip安装项目所需的库，不会影响其他项目。切记一个项目一个虚拟环境，否则可能会发生莫名的错误。

```
#1.首先创建项目目录
$ sudo mkdir -p myproject/blog
cd myproject/blog

#2.创建项目的虚拟环境
#用法：pyenv virtualenv python版本号 虚拟环境名
$ pyenv virtualenv 3.6.4 env36   #注意版本号必须是已经安装的，否则会报错

#3.切换到虚拟环境
python@ubuntu:/myproject/blog$ pyenv activate env36

pyenv-virtualenv: prompt changing will be removed from future release. configure `export PYENV_VIRTUALENV_DISABLE_PROMPT=1' to simulate the behavior.

(env36) python@ubuntu:/myproject/blog$  # (env36)表示该项目处于虚拟环境中

#验证
(env36) python@ubuntu:/myproject/blog$ python
Python 3.6.4 (default, Mar 29 2018, 10:33:37) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.

#4. 切出虚拟环境
(env36) python@ubuntu:/myproject/blog$ pyenv deactivate env36
```

- 使用pip下载库

使用pip下载，会从国外的网站下载，速度超慢，所以要切换pip到国内的镜像源，一般会用psm切换pip的源

- 1.安装一个软件psm

```
(bbs36)python@ubuntu:/myproject/blog$ pip install psm
[sudo] python 的密码： 
正在读取软件包列表... 完成
正在分析软件包的依赖关系树       
正在读取状态信息... 完成       
E: 无法定位软件包 psm
```

- 2.psm的使用

  以下操作需要在虚拟环境外进行，选择好镜像源后在进入虚拟环境

```
#1.查看列出pip的镜像源
(bbs36)python@ubuntu:/myproject/blog$ psm ls

pypi 	 https://pypi.python.org/simple/
douban 	 http://pypi.douban.com/simple/
aliyun 	 http://mirrors.aliyun.com/pypi/simple/

#查看当前的镜像源
(bbs36)python@ubuntu:/myproject/blog$ psm show

Current source is douban

#2.选择指定的镜像源

(bbs36)python@ubuntu:/myproject/blog$ psm use douban

Source is changed to douban.

#3 使用pip下载库
(bbs36) python@ubuntu:/myproject/blog$ pip install pymysql
```



### 3.3安装python

```shell
1 在安装之前一定要安装所依赖的包，否则安装会失败，【不过现在好像安装python时就会自动安装，我猜的】
$ sudo apt-get install libc6-dev gcc
$ sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm
2 安装python
$ pyenv install 3.6.4 -v # -v表示以日志的模式显示安装过程
#因为pyenv会自动到github上下载，速度超慢，所以一般会选择使用curl或者wget下载到~/.pyenv/cache下，然后再用pyenv安装，下面是可选的安装模式
$cd ~/.pyenv
$sudo mkdir chche
$sudo wget -c http://mirrors.sohu.com/python/3.6.4/Python-3.6.4.tar.xz -P  ~/.pyenv/cache/
$ pyenv install 3.6.4 -v
3 更新pyenv数据库
$pyenv rehash
4 列出所安装的python版本
$pyenv versions
5 切换python版本
$pyenv global 3.6.4
6 验证版本
$pythn 

```

注意：

- 使用pyenv管理python，必须是用pyenv安装的python才行，系统以前有的，需要重新用pyenv安装
- 使用pip安装第三方模块时会安装到~/.pyenv/versions/xxx下，不会和系统模块发生冲突；
- 使用pip安装模块后，可能需要执行pyenv rehash更新数据库。





## ubuntu下安装pycharm

csdn中有各种详细的教程