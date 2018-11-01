## 一对一关系

### 使用外键建立一对一表

```sql
建立外键的表中的数据必须小于等于关联的表
外键必须是唯一的 unique
创建外键：
【constraint 外键的名称】foreign key(外键字段) references 关联的表名(表中的字段)
例如： constraint fk_idcard foreign key(person_id) references person(id);

```

### 查询数据

```sql
查询1号人对应的卡号
select person.name,IDCard.cardid from person,IDCard where person.id=IDCard.person_id and person.id=1;
```

## 一对多关系

比如：学校表中每一个学校的id字段是唯一的，学生表中学生所在的学校是唯一的。一所学校对应许多的学生。

### 建立外键

```sql
创建外键时，需要在多表中创建外键
CONSTRAINT fk_students FOREIGN KEY(school_id) REFERENCES schools(id)
ON DELETE CASCADE ON UPDATE CASCADE【同时变化】
```

### 查询数据

```sql
查询3号学生的姓名、年龄、性别、学校名称
select  students.name,students.age,students.sex,schools.school_name 
from schools,students where schools.id=students.school_id 
and students.id=3;

 查询1号学校的所有学生       
 select * from students where school_id=1;

查询1号学校的所有学生,以及他们关联的学校名称
select  students.name,students.age,students.sex,schools.school_name 
from schools,students where schools.id=students.school_id 
and schools.id=1;
```

## 多对多关系

例如一个成员可以加入多个QQ群，一个群里有多个成员

```sql
在多对多中需要建立第三方表创建外键
第三方表中的字段需要包含另外两张表中的主键，这些字段是第三方表中的主键
 create table member_qq(
      member_id   int,
      qq_id  int,
      level   int,
      foreign key(member_id) references member(id),
      foreign key(qq_id) references qq(id),
      primary key(member_id,qq_id)
   );

```

### 查询数据

```sql
查询1号成员的昵称与其加入的群名
select member.nickname,qq.qqname from member,qq,member_qq
where member.id=member_qq.member_id and member_qq.qq_id=qq.id
and member.id=1;
```

等值连接，左外连接，右外连接

子查询（in all any）

合并查询结果（union）

