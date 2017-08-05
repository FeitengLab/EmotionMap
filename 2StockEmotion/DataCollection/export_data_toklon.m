% Author: Yuhao Kang
% Function: Export data
% 修改文件路径,导入伦敦和东京情绪数据.
% 将数据导出为.mat格式文件.
%% Read data from excel
xls_data_1=xlsread('Data_Tok_Lon.xlsx',1);
xls_data_2=xlsread('Data_Tok_Lon.xlsx',2);
xls_data_3=xlsread('Data_Tok_Lon.xlsx',3);
%% Emotion
month=xls_data_1(:,1);
day=xls_data_1(:,2);
year=xls_data_1(:,3);
emotion=xls_data_1(:,14);
site=xls_data_1(:,15);
%% Stock
ftse=xls_data_2(:,4);
n225=xls_data_3(:,4);