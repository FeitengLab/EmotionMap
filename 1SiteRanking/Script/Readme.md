## DBSCANjar.py

DBSCAN使用脚本。

将各景点坐标按格式存在Input文件夹下，命名为Sample1，Sample2，Sample3

将config.json改名为config0.json。

可在脚本中修改三个参数

每个文件对应输出一个csv文件和一个json文件。

注：在os.rename处设置断点，使用调试模式运行。因文件太大无法及时生成输出文件易出错。

## BCHjar.py

BCH是用来求放入多个文件的最适宜lambda参数，lambdaTestResult为多个文件一起计算的结果。无需修改config.json的参数。

将聚类好的csv文件放到Cluster文件夹下

result即为最优凹壳结果

注：同在os.rename处设断点运行