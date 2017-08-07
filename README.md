# EmotionMap 情绪地图
Explore the emotion distribution with several different data sources in a global scale.  
探究全球尺度情绪分布

# Standard rules 标准要求

## Naming convention 命名要求
- 每个项目，函数，变量根据不同的功能进行命名，要求是尽量能够说明用途
- 项目名，变量名首个单词最好是名词，函数名首个单词最好是动词
- Python的项目名，函数名，变量名均为小写，单词之间使用下划线进行连接。  
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
- 提交命名为 "author-date-time"。  
例如：'kyh-170804-1'
- 每个文件提交后需要在本文档中添加相应的条目，包含文件目录和文件功能叙述。
- 每个文件夹下可以附加说明文件，说明文件推荐命名为：`README.MD`。

# Document organization 文档组织

## 0All
Common projects
### Flickr数据文件  
百度云盘：链接：http://pan.baidu.com/s/1qXGmuRy 密码：m7qh  其中的27个CSV文件
### FlickrGeoDataFromFile  
将相应矩形区域内的Flickr数据导出为csv  
用法：
- 打开exe文件。  
- 导入Flickr数据文件：选择任意Flickr数据文件即可，系统会自动获取文件夹名称。  
例如：E:\BaiduNetdiskDownload\Flicker_geotag_library\AWS\yfcc100m_dataset-0-x.csv  
- 分别输入地理方位最大最小经纬度范围，凡是该范围内的Flickr数据都会被提取出来。  
- 导出文件名。导出文件会在Flickr数据文件夹下，故只需要输入文件名即可（非路径）。  
导出格式为csv文件，每一行内容已经统一了格式，可以直接导入数据库。  
例如：beijing  

## 1SiteRanking
A Ranking of Tourist Attractions based on the Facial Expressions.
### Data Collection

#### get_flickr_photos

- ##### get_flickr_photos.py
用于获取Flickr照片

### Emotion Detection
### Spatial Analysis



## 2StockEmotion
Mapping the Sensitivity of the Public Emotion to the Movement of Stock Market Value.
### Data Collection
- #### compute_correlation.m  
计算曼哈顿地区股票与情绪之间的相关性
- #### compute_correlation_toklon.m  
计算东京伦敦股票与情绪之间的相关性
- #### comute_emotion_avg.m  
计算情绪各月平均值和方程
- #### emotion_data_manhattan.mat  
曼哈顿区域的数据，包括情绪值，股票值
- #### export_data.m  
将excel文件中曼哈顿区域的数据导出为.mat文件格式
- #### pca_emotion.m  
对曼哈顿地区情绪数据进行主成分分析


### Emotion Detection
### Spatial Analysis