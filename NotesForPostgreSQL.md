## PostgreSQL 速查、备忘手册
这是一个你可能需要的一个备忘手册，此手册方便你快速查询到你需要的*常见功能*。有时也有一些曾经被使用过的高级功能。如无特殊说明，此手册仅适用于 Linux 下（但是许多也都可以在 Windows 下的 psql 命令窗运行），部分功能可能需要你的软件版本不能太低。  
**欢迎添加你认为有价值的备忘！**

#### 切换到 postgres 账户
```bash
$ sudo -i -u postgres # 你可能需要在 sudoers list里面，也就是你可以执行
```
#### 进入默认 psql 命令行（默认 postgres 数据库）
此时你的命令前面变成 "postgres=# " 的字样，说明你已经成功进入 postgres 这个数据库，这个数据库存储着一些程序的默认设置，所以请不要随意更改甚至删库。 同时，程序也提示你可以使用 `help` 获取命令帮助，相信你和我一样不想看这冗长的输出，这也是这个手册的价值所在。 
**注意，从此处开始，你可以注意我们的表示习惯:**  

* `$` 开头的命令代表普通命令
* `psql=#` 开头的命令代表在进入 psql 后执行的命令，至于具体的数据库名称在此不标识出来，请读者注意。 
* 大写的DBNAME，TABLENAME 等对应你自己的数据库名、表名等，不是实指。
```bash
$ psql  # 得到以下输出
psql (9.x.xx)
Type "help" for help.

postgres=# 
```
#### Windows下使用psql
Windows下打开 psql 命令窗两种常用方法：

* 打开你的 pgadmin 软件图形界面，在菜单栏找到 `插件 > PSQL Console`
* 不想开 pgadmin 的话，找到 psql.exe 所在目录，在此目录打开cmd，运行：
```bat
$ psql -U postgres DBNAME
```
#### 离开数据库
请注意，Postgresql 的特殊命令都是以 **\\** 开头的，而且结尾不需要分号`;`
```sql
psql=# \q
```
#### 进入指定数据库
请注意, 数据库名称大小写是敏感的（Case-sensitive）
```bash
$ psql DBNAME # DBNAME 是你要进去的数据库名称
```
#### 查看（列出）所有数据库
如果你刚接手一个数据库，不知道现存哪些数据库，那么你就`$ psql`进入默认数据库进行以下查询（此查询在其他数据库也可以）
```sql
psql=# \list or \l
```
显示每个数据库的额外信息，后面的 `+` 对 下面的 `\d, \dt` 也都适用，都是提供数据库占用之类的额外信息。
```sql
psql=# \l+
```
#### 查看当前数据库所有table
```sql
psql=# \dt
```
#### 查看当前数据库所有 relation
relation 包括有 table, view, sequence等
```sql
psql=# \d
```
#### 查看某个表的所有字段
```sql
psql=# \d TABLENAME
```
#### 查看某数据库占用存储大小
```sql
psql=# SELECT pg_size_pretty(pg_database_size('DBNAME'));
```
#### 执行任意 SQL 语句
首先作为关系型数据库，基本的 SQL 语言是必须要支持的。我假设你对此有所了解，当然你不需要对此精通。有一些 SQL 的基本规则你需要在这里格外注意，稍有不慎就可能会导致错误，可能很简单的错误就会打击你的积极性。
##### SQL 语句中双引号和单引号的使用：
* 双引号`"`用来表示的表名，但是一般我们在使用中将__双引号省略__
* 单引号`'`用来表示普通字符串
以下两个命令是等价的：
```sql
psql # SELECT FIELDNAME FROM TABLENAME WHERE FIELDNAME='normalstring';
psel # SELECT "FIELDNAME"  FROM "TABLENAME" WHERE "FIELDNAME"='normalstring';
```
##### SQL 语句必须以 __`;`__ 结尾

#### 导出数据库
命名随意选择，选这个后缀是为了便于标识。另外由于权限问题，推荐保存在 `/tmp` 下。 Windows 下也会出现写文件权限问题，有不同的解决办法，比如修改用户权限等问题，但是这个涉及到用户权限设置等，个人不建议修改。建议自己尝试一下，如果失败，是不是有中文（或其他非ASCII）路径，其次是否是在你的用户路径或者是否在系统路径下。
```bash
$ pg_dump DBNAME > /tmp/DBNAME.postgresql
```
#### Windwos下从文本恢复数据库，通常需要先创建一个空数据库 DBNAME，然后运行：
```bat
$ psql -U postgres DBNAME < PATH\TO\YOUR\DBFILE
```
#### 创建NoSQL扩展：
```sql
psql=# create extension hstore
```
#### 在psql中执行bash的命令：
```sql
psql=# \! dir
```
#### 导出table 或者 到处 SQL 查询的结果
```sql
psql=# copy [TABLENAME|(query)] to 'FILEPATH' with delimiter '|'
```
#### 查看postgres用户的目录
```bash
$ echo ~postgres
```
#### 将指定表到处至压缩文件
这个要求你的系统安装有 `zip` 。当然极少有 Linux 没有这个软件。Windows 如果自己有安装，命令行可以调用的话也可以用，否则就当我什么都没说。
```bash
$ psql -c "copy public.TABLENAME to stdout with delimiter '' csv header"  DATABASE | zip > TABLENAME.zip
```
#### 显示配置文件
```sql
psql=# SHOW config_file;
```
#### 显示软件版本
```sql
psql=# SHOW version();
```
#### 在命令中表示TAB键：
```
E'\t'
```
#### 给某条语句的运行计时：
只输入`\timing` 就是在 on 和 off之间切换，可以显式输入 on 和 off
```
psql=# \timing [on|off]
```
#### 解释语句内部处理过程：
```sql
psql=# EXPLAIN [SQL query]
```
