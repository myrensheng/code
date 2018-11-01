#数据库操作类
import os

import pymysql

from settings import database

class Model:
    def __init__(self,tablename):
        self.conn = self.__connect()   #连接数据库
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.tablename = tablename
        self.options = {
            'fields': '*',    # 字段列表
            'table': self.tablename,      # 表名
            'where': '',      # where条件
            'groupby': '',    # group by分组条件
            'having': '',     #having 分组过滤条件
            'orderby': '',    #order by排序条件
            'limit': ''       #limit 限制结果集
        }
        self.__cache_field()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    # 字段缓存
    def __cache_field(self):
        # 1.判断是否有表名，如果没有，不做字段缓存
        if not self.options['table']:
            return

        # 如果没有cache目录，则建立
        if not os.path.exists('./cache'):
            os.mkdir('./cache')

        # 如果有表名
        path = './cache/' + self.options['table'] + '.txt'
        content = ''  #字段列表字符串
        if os.path.exists(path):
            with open(path,'r') as fp:
                content = fp.read()
        else:
            # 文件不存在，查询表，取出字段列表，写入文件
            self.cursor.execute("desc " + self.options['table'])
            # data = self.query("desc " + self.options['table'])
            data = self.cursor.fetchall()
            if not data:
                exit()

            # 拼接字段列表
            for rec in data:
                content += rec['Field'] + ','
            content = content.rstrip(',')
            with open(path,'w') as fp:
                fp.write(content)
        # if self.options['fields'] == '*':
        #     self.options['fields'] = content
        self.cachefield = content     #保存字段缓存
        self.options['fields'] = content

    # 连接数据库
    def __connect(self):
        conn = pymysql.connections.Connection(**database)
        return conn

    def field(self,fields):
        self.options['fields'] = fields
        return self
    # def table(self,tablename):
    #     # print(tablename)
    #     self.options['table'] = tablename
    #     # self.__cache_field()
    #     return self

    def where(self, conditions):
        # 判断options中where是否为空
        if not self.options['where']:  #为空
            self.options['where'] = " WHERE " + conditions
        else:
            self.options['where'] += ' and ' + conditions
        return self

    def whereor(self, conditions):
        # 判断options中where是否为空
        if not self.options['where']:  #为空
            self.options['where'] = " WHERE " + conditions
        else:
            self.options['where'] += ' OR ' + conditions
        return self

    # 分组
    def groupby(self,conditions):
        self.options['groupby'] = " GROUP BY " + conditions
        return self
    #having
    def having(self,conditions):
        if not self.options['having']:
            self.options['having'] = " HAVING " + conditions
        else:
            self.options['having'] += ' AND ' + conditions
        return self

    # 排序
    def orderby(self,conditions):
        self.options['orderby'] = " ORDER BY " + conditions
        return self

    #limit
    def limit(self,conditions):
        self.options['limit'] = " LIMIT " + conditions
        return self
    def select(self):
        sql = "SELECT {fields} FROM {table} {where} {groupby} {having} {orderby} {limit}"
        sql = sql.format(**self.options)
        self.sql = sql  #保持sql语句
        return self.query(sql)

    # 还原options条件
    def __init_options(self):
        self.options = {
            'fields': self.cachefield,  # 字段列表
            'table': self.tablename,  # 表名
            'where': '',  # where条件
            'groupby': '',  # group by分组条件
            'having': '',  # having 分组过滤条件
            'orderby': '',  # order by排序条件
            'limit': ''  # limit 限制结果集
        }

    # 可以进行原生的sql查询
    def query(self, sql):
        self.__init_options()
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()  #返回查询结果
        except Exception as e:
            print(e)
            return None   #如果查询出错，返回None

    # 给字符串添加单引号
    def __add_quote(self, data):
        for key in data:
            if isinstance(data[key], str):
                data[key] = "'" + data[key] + "'"
    #insert
    # data必须是字典
    def insert(self,data):
        sql = "INSERT INTO {table}({fields}) values({value})"
        # insert into user(sno,sname) values('9393','kdkd')
        # {'sno':'tom'}
        # 1.把data中值为字符串的两边添加单引号
        self.__add_quote(data)
        print(data)

        # 2.获取字段列表和值列表
        fields = ''
        value = ''
        for key in data:
            fields += key + ','
            value += str(data[key]) + ','
        fields = fields.rstrip(',')
        value = value.rstrip(',')

        # 3.替换sql
        self.options['fields'] = fields
        self.options['value'] = value
        sql = sql.format(**self.options)

        return self.execute(sql)

    def execute(self, sql):
        self.__init_options()
        try:
            res = self.cursor.execute(sql)
            self.conn.commit()
            if res > 0:
                return True
            else:
                return False
        except Exception as e:
            self.conn.rollback()
            return False

    # 删除记录
    def delete(self):
        sql = "DELETE FROM {table} {where}"
        sql = sql.format(**self.options)
        return self.execute(sql)

    # 修改
    # data必须是字典
    def update(self, data):
        self.__add_quote(data)
        s1 = ','.join([key + '=' + str(value) for key, value in data.items()])
        self.options['value'] = s1
        sql = "UPDATE {table} SET {value} {where}".format(**self.options)
        return self.execute(sql)

if __name__ =='__main__':
    model = Model()
    print(model.table('student').select())
    print(model.sql)
    print(model.options['fields'])
    # print(model.options)
    # print(model.conn,model.cursor) or exit()
    #select * from user where uname='tom'
    # print(model.table("user").field('uname,password').where('uname="tom"').select())
    # # print(model.query("select * from stu"))
    # print(model.sql)
    # print(model.options)
    # print(model.table('user').field('uname').where("uid=2").select())
    # print(model.sql)
    # print(model.options)
    # data = model.field("ssex,count(ssex)").table("student").groupby('ssex').having("count(ssex) > 1").select()
    # data = model.field("sno,sname").table("student").orderby('sno desc').limit('3').select()
    # print(data)
    # print(model.sql)
    # data = {'sname': '张三', 'sno': '180513', 'sage': 20}
    # model.table('student').insert(data)
    # print(model.table('student').where("sno='00001'").delete())
    # model.table('student').where("sno='180513'").update({'sname':'tom','sage':20})
    # print(model.table('student').field('Field').)
    # print(model.query("desc student"))