## Postgresql 上手备忘手册
这是一个你可能需要的一个备忘手册，此手册方便你快速查询到你需要的*常见功能*。有时也有一些曾经被使用过的高级功能，欢迎添加你认为有价值的备忘。如无特殊说明，此手册仅适用于 Linux 下（但是许多也都可以在 Windows 下的 psql 命令窗运行），部分功能可能需要你的版本不能太低。

#### 切换到 postgres 账户
```bash
$ sudo -i -u postgres # 你需要在 sudoers list
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
不想开 pgadmin 的话，找到psql.exe所在目录，在此目录打开cmd，运行：
```bat
$ psql -U postgres DBNAME
```
#### 离开数据库
请注意，Postgresql 的特殊命令都是以 **\\** 开头的
```sql
psql=# \q
```
#### 进入指定数据库
请注意, 数据库名称大小写是敏感的（Case-sensitive）
```bash
$ psql DBNAME # DBNAME
```
#### 查看（列出）所有数据库
如果你刚接手一个数据库，不知道现存哪些数据库，那么你就`$ psql`进入默认数据库进行以下查询（此查询在其他数据库也可以）
```sql
psql=# \list or \l
```
#### 查看当前数据库所有table
```sql
psql=# \dt
```
#### 查看当前数据库所有relation
relation 包括有 table, view, sequence等
```sql
psql=# \d
```
#### 查看某个表的所有字段
```sql
psql=# \d+ TABLENAME
```
#### 查看某数据库占用存储大小
```sql
psql=# select pg_size_pretty(pg_database_size('DBNAME'));
```
#### 导出数据库
命名随意选择，选这个后缀是为了便于标识。另外由于权限问题，推荐保存在 `/tmp` 下。 
```sql
$ pg_dump DBNAME > /tmp/DBNAME.postgresql
```
#### Windwos下从文本恢复数据库，通常需要先创建一个空数据库DBNAME，然后
```bat
$ psql -U postgres DBNAME < the\path\to\your\backupfile
```
#### 创建NoSQL扩展：
```sql
psql=# create extension hstore
```
#### 在psql中执行bash的命令：
```sql
psql=# \! dir
```
#### 导出table
```sql
psql=# copy [TABLENAME|(query)] to 'FILEPATH' with delimiter '|'
```
#### 查看postgres用户的目录
```bash
$ echo ~postgres
```
#### 将指定表到处至压缩文件
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
```
psql=# \timing [on|off]
```
#### 解释语句内部处理过程：
```sql
psql=# EXPLAIN [SQL query]
```
