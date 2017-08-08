FlickrGeoDataFromFile修改

Author：HCHO

修改内容：实现利用txt文本文件完成按坐标筛选Flickr照片的批量处理

PS.因修改时间较短（用于解决一个bug），对原作品有较大破坏，但能完成批量处理的目的。

使用方法：先导入Flickr数据文件，然后在批量处理栏导入txt文件即可完成筛选照片的批量处理。

txt文件格式：参照实验数据txt，变量输入顺序为maxLat,minLat,maxLon,minLon,文件名。（记得中间用逗号隔开）

常量DATANUMBER为批量处理的个数上限，初设为5，可根据情况在程序中修改。

代码较乱见谅，日后修改。