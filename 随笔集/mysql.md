## 修改用户密码

```mysql
方法一：【不管用好像】
使用set password 命令
例如：set password for root@localhost = password('123');
方法二：
用updata直接编辑user表

```

## 基本用法

```mysql
mysql -h localhost -u root -p******
show databases;
use mysql;【使用数据库】
select * from 表名称\G；
show create database 数据库名；
show create table 表名称；
切换数据库，只需要show databases；然后use 数据库名；就可以
```

## mysql的增删改查

### 一、增加 create / insert / alter

```mysql
1 增加数据库 create database 数据库名称 default character set utf8；
增加表 
create table 表名称(
	字段名1 数据类型 【约束】,
    字段名1 数据类型 【约束】,
    .........
)
其中字段名就是表头，每一列数据的名称
2 插入数据 insert 【四种方式插入数据】
insert into 表名称(字段名1，......) values
(值1，值2，值3，......),
(值1，值2，值3，......),
(值1，值2，值3，......);
3 增加列
alter table 表名称 add column 字段名 数据类型 【约束】；

```

### 二、删除 delete / drop

```sql
1 删除记录，就是删除表中的一些数据
delete from 表名称 【where条件】；
2 删除一列数据
alter table 表名称 drop column 字段名；
3 删除表
drop table 表名称；
4 删除数据库
drop database 数据库名称；
drop是用来删表和数据库的，delete是用来删除数据【一行，一列】
```

### 三、修改 update / alter / rename

```sql
1 修改表中的数据
update 表名称 set 字段名1=字段值，字段名2=字段值，..... where 条件；
2 修改列名称
alter table 表名称 modify column 字段名 数据类型 【约束】；
3 修改表名称
rename table test to test1；

```

### 四、查询

4.1 条件查询

```sql
select * from 表名称 where 条件；
select 字段名1，字段名2，..... where 条件；
```

4.2 分组查询

```sql
select 字段名1，字段名2，【聚合函数】.... from 表名称 group by 字段名 【having条件】
```

4.3 模糊查询

```sql
select 字段名1，字段名2，..... from 表名称 where 条件 like 模糊条件；【% 匹配任意多个。-匹配一个任意字符】
```

4.4 排序查询

```sql
select 字段名1，字段名2，...... from 表名称 where 条件 order by 字段名[desc，字段名]；
```

4.5 限制查询

```sql
select 字段名1，字段名2，...... from 表名称 where 条件 limit 最多纪录；
```

