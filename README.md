# EmotionMap 情绪地图
Explore the emotion distribution with several different data sources in a global scale.
探究全球尺度情绪分布

# Standard rules 标准和要求
## Repository organization 项目组织 
### DataCollection
Including code files collect data from Flickr, Twitter, Weibo, Panorama photos.
### EmotionDetection
Including code files detect emotion conditions from dataset.
### SpatialAnalysis
Including code files for spatial analysis.

## Name rules 命名要求
每个项目，函数，变量根据不同的功能进行命名，要求是尽量能够说明用途；项目名，变量名首个单词最好是名词，函数名首个单词最好是动词。
python的项目名，函数名，变量名均为小写，单词之间使用下划线进行连接。
例如：get_flickr_photos
C#，MATLAB的项目名，函数名的单词首字母均为大写，单词之间无空格。
例如：GetFlickrPhotos
C#，MATLAB的变量名，整个变量名首字母为小写，其余单词首字母均为大写，单词之间无空格。
例如：flickrPhotos

## 注释要求
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
提交命名为 "author-date-time"
例如："kyh-170804-1"
每个文件提交后需要在本文档中添加相应的条目，包含文件目录和文件功能叙述。

# File organization 文档组织
## DataCollection

### get_flickr_photos

#### get_flickr_photos.py
用于获取Flickr照片

## EmotionDetection
## SpatialAnalysis