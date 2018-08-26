## PostgreSQL 速查、备忘手册
这是一个你可能需要的一个备忘手册，此手册方便你快速查询到你需要的*常见功能*。有时也有一些曾经被使用过的高级功能。如无特殊说明，此手册仅适用于 Linux 下（基本都可以愉快运行，一般也都可以在 Windows 下的 psql 命令窗运行，只是稍微麻烦一点），部分功能可能需要你的软件版本不能太低。  
**欢迎添加你认为有价值的备忘！**

#### 切换到 postgres 账户
```sh
$ sudo -i -u postgres # 你可能需要在 sudoers list里面，也就是你可以执行
```
#### 进入默认 psql 命令行（默认 postgres 数据库）
此时你的命令前面变成 "postgres=# " 的字样，说明你已经成功进入 postgres 这个数据库，这个数据库存储着一些程序的默认设置，所以请不要随意更改甚至删库。 同时，程序也提示你可以使用 `help` 获取命令帮助，相信你和我一样不想看这冗长的输出，这也是这个手册的价值所在。 
**注意，从此处开始，你可以注意我们的表示习惯:**  

* `$` 开头的命令代表普通命令，即使用 postgres 用户执行的命令
* `psql=#` 开头的命令代表在进入 psql 后执行的命令，至于具体的数据库名称在此不标识出来，请读者注意。 
* 大写的DBNAME，TABLENAME 等对应你自己的数据库名、表名等，不是实指。
```sh
$ psql  # 得到以下输出
psql (9.x.xx)
Type "help" for help.

postgres=# 
```
#### Windows下使用 psql
Windows下打开 psql 命令窗两种常用方法：

* 打开你的 pgadmin 软件图形界面，鼠标在左侧对象浏览器选中你要进入的数据库，在菜单栏找到 `插件 > PSQL Console`
* 不想开 pgadmin 的话，找到 psql.exe 所在目录（实例：`C:\Program Files (x86)\PostgreSQL\9.x\bin`），在此目录打开cmd（一些其他的程序如`pg_dump`等也都在这个目录），运行：
```bat
$ psql -U postgres DBNAME
```
Windows 注意：很多时候你运行 psql 出错是因为没有输入正确的用户名参数，例如用户名`-U postgres`等。
#### 离开数据库
请注意，Postgresql 的特殊命令都是以 **\\** 开头的，而且结尾不需要分号`;`
```sql
psql=# \q
```
#### 进入指定数据库
请注意, 数据库名称大小写是敏感的（Case-sensitive）
```sh
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
#### 列出某个所有字段（仅字段）
与上面不同，这个仅列出字段，便于在字段很多，但是你有不需要所有的字段的时候直接拷贝。（[来源](https://dba.stackexchange.com/questions/22362/how-do-i-list-all-columns-for-a-specified-table)
```sql
psql=# SELECT * from TABLENAME where false;
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
命名随意选择，选这个后缀是为了便于标识。另外由于权限问题，推荐保存在 `/tmp` 下。  
如果你每次只写文件名的话，会默认保存在 postgres 用户的默认目录下，而这个目录比较深，你可能不太容易找，而且即使可以找到，作为普通用户，还可能涉及到读写权限问题。
Windows 下也会出现写文件权限问题，有不同的解决办法，比如修改用户权限等问题，但是这个涉及到用户权限设置等，个人不建议修改。建议自己尝试一下，如果失败，是不是有中文（或其他非ASCII）路径，其次是否是在你的用户路径或者是否在系统路径下。
```sh
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
#### 在psql中执行 shell 命令：
注意中间的空格，不可忽略
```sql
psql=# \! dir
```
有了这个的帮助，你在 Windows 下，需要运行 `psql.exe` 或者其他程序，就不需要费周章去找到其具体目录了，你可以从 pgadmin 的 [PSQL console](#windows-psql) 来运行一些命令了。例如：
```sql
psql=# \! psql -c "SHOW version()" -U postgres  -- 显示软件版本
```
值得一提的是，这种使用方案并不算好用，因为 Windows 命令行奇怪的编码，以及如果软件在你电脑上自动安装成了中文，一旦输入了错误指令，报错会用中文报错，报错的内容可能就会乱码。
#### 查看postgres用户的目录
```sh
$ echo ~postgres
```

#### 在 shell 里面执行 SQL 语句
一般都是涉及到输入输出的时候使用，基本是如下格式：
```sh
$ psql -c "YOUR SQL QUERY" DATABASENAME
```

#### 导出table 或者 导出 SQL 查询的结果
这种 [COPY 命令](https://www.postgresql.org/docs/current/static/sql-copy.html)也是 SQL 语句的形式，但这不是 SQL 标准要求的东西  
FILEPATH 不支持相对路径
```sql
psql=# copy TABLENAME to 'FILEPATH' with delimiter '|'; -- 指定table
psql=# copy TABLENAME(FIELD1, FILED2) to 'FILEPATH' with delimiter '|'; -- 指定table及其字段
psql=# copy (query) to 'FILEPATH' with delimiter '|'; -- 使用 query
```

#### 导出为json格式的文件
```
psql=# copy (select ROW_TO_JSON(t) from (select * from TABLENAME) t) to 'FILEPATH';
```

#### 在命令中表示TAB键
到处为 csv 的时候你可能需要用到
```
E'\t'
```

#### 将指定表导出至压缩文件
将以上命令也可以在 shell 里面执行，这样的话，我们就可以以文件流的形式将我们的输出传到其他的程序。比如此处，我们使用 `zip` 将输出的文件直接压缩，方便我们下载并节省流量加快速度。（请注意，这个时候，你从这个文件解压出来的文件名仅仅是一个连字符`-`，这是文件流的默认名称）  
（这个要求你的系统安装有 `zip` 。当然极少有 Linux 没有这个软件。Windows 如果自己有安装，命令行可以调用的话也可以用，否则你就当我什么都没说。）
```sh
public 是你的默认 schema 。
$ psql -c "copy public.TABLENAME to stdout with delimiter E'\t' csv header"  DATABASE | zip > TABLENAME.zip
```
#### 显示配置文件
```sql
psql=# SHOW config_file;
```
#### 显示软件版本
```sql
psql=# SELECT version();
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
#### 查看服务运行状态
`pg_lsclusters` 可以用来显示当前数据库服务运行状态，可以查看服务是否开启，以及 _log文件的位置_ ，这个在你的数据库无法开启时可能是你需要的（运行`less LOG_PATH`查看log)。 然后针对你碰到的错误使用搜索引擎，你碰到过的问题，其他人基本都碰到过。
```sh
$ pg_lsclusters
```
#### 快速查询表的（估计）行数
通常当表变得非常大时（千万条数据级以上），数据库没有优化的话，查询速度变得相当缓慢。使用以下命令可以瞬间查找到记录的大致数值。(Ref: [SO](https://stackoverflow.com/a/7945274))
```sh
psql=# SELECT reltuples::bigint AS estimate FROM pg_class where relname='TABLENAME';
```
