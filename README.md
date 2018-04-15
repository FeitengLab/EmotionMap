# EmotionMap 情绪地图
Explore the emotion distribution with several different data sources in a global scale.  
探究全球尺度情绪分布

# Standard rules 标准要求

## Naming convention 命名要求
- 每个项目，函数，变量根据不同的功能进行命名，要求是尽量能够说明用途
- 项目名，变量名首个单词最好是名词，函数名首个单词最好是动词
- Python的项目名，函数名，变量名均为小写，单词之间使用下划线进行连接
- 涉及到与步骤相关比较强的多个文件的使用，可以在文件名前添加数字表示运行顺序
例如：`get_flickr_photos`
- C#，MATLAB的项目名，函数名的单词首字母均为大写，单词之间无空格。  
例如：`GetFlickrPhotos`
- C#，MATLAB的变量名，整个变量名首字母为小写，其余单词首字母均为大写，单词之间无空格。  
例如：`flickrPhotos`
- SQL语句所有SQL语法单词均大写，具体的变量名均小写。   
例如：SELECT * FROM table_name WHERE id = 1;

## Commenting instructions 注释要求
python最上方添加注释，包含字符编码，python版本，作者和功能叙述  
例如：

	# coding: utf-8
	
	# version: python3.5
	
	# author: Yuhao Kang
	
	# function: functions

C#在using下方添加注释，包含作者和功能叙述  
例如：

	// Author: Yuhao Kang
	
	// Function: Functions
MATLAB首行添加注释，包含作者和功能叙述  
例如：

	% Author: Yuhao Kang

	% Function: Functions
	
SQL首行添加注释，包含作者和功能叙述  
例如：

	/* Author: Yuhao Kang
	
	Function: Functions */

## Committing rules 提交要求
- 提交命名为 "author-date-time(-describe)",其中dexcribe为英文简单描述。  
例如：'kyh-170804-1-Create Files'
- 每个文件提交后需要在本文档中添加相应的条目，包含文件目录和文件功能叙述。
- 每个文件夹下可以附加说明文件，说明文件推荐命名为：`README.MD`。

# Document organization 文档组织

## 0All
Common projects  共有代码
### Flickr数据文件  
百度云盘[链接](http://pan.baidu.com/s/1qXGmuRy) 密码：m7qh    
AWS文件夹下为10个源数据CSV文件（共1亿条数据）  
geotag文件夹下为带有地理坐标数据的CSV文件（共约4600万条数据）
### batch_rename.py
重命名文件夹下所有的文件名  
### FlickrGeoDataFromFile  
将相应矩形区域内的Flickr数据导出为csv  
用法：
- 打开exe文件。  
- 导入Flickr数据文件：选择任意Flickr数据文件即可，系统会自动获取文件夹名称并遍历该文件夹下的所有数据文件。  
例如：E:\BaiduNetdiskDownload\flickr_data\geotag_data\0.csv  
- 导入区域范围数据CSV文件，格式为：左上角经度，纬度，右下角经度，纬度，景点名称。    
格式案例可以参考Region.csv
- 导出格式为csv文件，每一行内容已经统一了格式，可以直接导入数据库。
### CollectData
获取情绪数据
用法：
- 打开CloudDatabase.py文件，该文件包含以下功能：
（1）创建照片表：修改数据库的相关参数，创建照片表
（2）导入CSV文件：传入本地数据的路径，则可以将本地数据传入到云端数据库中
（3）添加情绪字段：在数据传输完毕后，添加新的两列数据字段
- 打开DetectEmotion.py文件，该文件可以对相应的数据库中照片数据进行情绪识别
方法：修改API KEY / SECRET，同时修改表的id即可。    
- 可以参考SQLreference.sql中的相关语句，完成数据库的操作
  
批量从云端导出数据
- 服务器上运行[server_output_checksum.py](0All/CollectData/server_output_checksum.py)
- 本地z命令行运行[linux_file_to_win.py](0All/CollectData/linux_file_to_win.py)（注意需要同目录的几个exe文件）

将情绪数据从照片转换为人脸为单位
- 修改[Photo2Face](0All/CollectData/Photo2Face.py)中数据的路径，即可将照片中所有的情绪转换为以人脸为单位的情绪值

test_facepp_api.py:检查API是否失效

split_file.py:将大文件拆成小文件，每个文件10w张人脸

format_face.py:将所有数据格式标准化从而可以导入数据库中

import_to_database.py:将所有的人脸数据导入本地数据库中

execute_sql.py:放在云端运行相应的SQL语句

### HCHO
贾清源有关获取情绪数据、写入数据库的代码方法文件  
emotion4.01.py
功能：逐一读取数据并存入数据库
修改数据库信息，path即可
emotion4.02.py
功能：随机检测一个表中照片的facenum及attribus
修改数据库信息，API信息，文件名即可

## 1SiteRanking
A Ranking of Tourist Attractions based on the Facial Expressions.
### Data Collection
search_sites.html: 导入csv文件，包括景点的名称，返回景点的经纬度、类型、评分。 

get_flickr_photos.py: 获取Flickr照片  

get_photo_info.py: 获取Flickr照片的信息

DetectEmotion.py: 探测照片的情绪

## 2StockEmotion
Mapping the Sensitivity of the Public Emotion to the Movement of Stock Market Value.
### √ Workflow 1 (MATLAB)
#### √ manhattan_workflow.m
计算曼哈顿地区股票与情绪之间相关性的完整工作流：导入数据，主成分分析，导出数据，标准化，相关性分析   
#### √ manhattan_workflow.m
计算伦敦和东京股票与情绪之间相关性的完整工作流：导入数据，主成分分析，导出数据，标准化，相关性分析   
### Workflow 2 (Python, Jupyter Notebook)
#### × 带数字的文件
- × 输入文件为从数据库直接导出的情绪数据文件和各股票文件（待改进：文件命名需要替换的地方多，需要导出为Python，暴露统一接口）
- 1，2，3，4 开头的文件为程序运行顺序，相同代表可以一起运行。其中2为可视化检查，可以运行一次，也可以不运行。
#### × 不带数字的文件（顺便写的辅助文件）
- √ [三个交易所股票关系.ipynb](2StockEmotion/三个交易所股票关系.ipynb):
绘制NASDAQ、N225、FTSE100三个文件。
- × [数据按照月份导出csv.ipynb](2StockEmotion/数据按照月份导出csv.ipynb):
将数据按照自己要求导出的模板文件，可以按照自己的意愿将需要的数据导出为csv。(改进：函数化）

## 3WorldEmotion
#### GlobalEmotion.ipynb
计算了世界不同人种之间的情绪差异
#### pt_join_country.py
将人脸数据与国家相关联
#### datashader_plot.ipynb
使用 datashader 来画数据量极大的点
#### export_YFCCextended.zip
快速导出成果表
#### send_mail.py
快速发送QQ邮件