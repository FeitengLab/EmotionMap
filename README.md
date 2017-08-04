# EmotionMap 情绪地图
Explore the emotion distribution with several different data sources in a global scale.  
探究全球尺度情绪分布

# Standard rules 标准和要求
## Repository organization 项目组织 
### Data Collection
Including code files collect data from Flickr, Twitter, Weibo, Panorama photos.
### Emotion Detection
Including code files detect emotion conditions from dataset.
### Spatial Analysis
Including code files for spatial analysis.

## Naming convention 命名要求
- 每个项目，函数，变量根据不同的功能进行命名，要求是尽量能够说明用途
- 项目名，变量名首个单词最好是名词，函数名首个单词最好是动词
- Python的项目名，函数名，变量名均为小写，单词之间使用下划线进行连接。  
例如：`get_flickr_photos`
- C#，MATLAB的项目名，函数名的单词首字母均为大写，单词之间无空格。 
例如：`GetFlickrPhotos`
- C#，MATLAB的变量名，整个变量名首字母为小写，其余单词首字母均为大写，单词之间无空格。  
例如：`flickrPhotos`

## Commenting instructions 注释要求
python最上方添加注释，包含字符编码，python版本，作者和功能叙述  
例如：

	# coding: utf-8
	
	# version: python3.5
	
	# author: Yuhao Kang
	
	# function: functions

C# using下方添加注释，包含作者和功能叙述  
例如：

	// Author: Yuhao Kang
	
	// Function: Functions
MATLAB首行添加注释，包含作者和功能叙述  
例如：

	% Author: Yuhao Kang

	% Function: Functions

## 提交要求
<<<<<<< HEAD
提交命名为 "author-date-time"
例如："kyh-170804-1"
每个文件提交后需要在本文档中添加相应的条目，包含文件目录和文件功能叙述。
=======
- 每个文件提交后需要在本文档中添加相应的条目，包含文件目录和文件功能叙述。
- 每个文件夹下可以附加说明文件，说明文件推荐命名为：`README.MD`。
>>>>>>> efc92440354993c361040dc8c0cb1d97f2fd4061

# Document organization 文档组织
## Data Collection

### get_flickr_photos

#### get_flickr_photos.py
用于获取Flickr照片

## Emotion Detection
## Spatial Analysis
