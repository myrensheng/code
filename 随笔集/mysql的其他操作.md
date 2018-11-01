## 事务

难理解

## 索引与视图

索引

给需要经常查询的列上加上索引，加上索引会使查询时间变短。

```sql
创建索引
create index 索引名称 on 表名称（字段列表）；
查看索引
show index from 表名称；
删除索引
drop index 索引名称 on 表名称；
```

视图

```sql
create view 视图名称
as
select 语句；

例如：
create view dapt_view
as 
select d_no,as 部门编号，d_name as 部门名称
from dept；
```

## Python操作数据库

```Python

```





























