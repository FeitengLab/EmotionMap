% Author: Yuhao Kang
% Function: Export data
% �޸��ļ�·��,������������.
% �����ݵ���Ϊ.mat��ʽ�ļ�.
%% Read data from excel
xls_data_1=xlsread('Data.xlsx',1);
xls_data_2=xlsread('Data.xlsx',2);
%% Emotion
month=xls_data_1(:,12);
day=xls_data_1(:,13);
year=xls_data_1(:,14);
emotion=xls_data_1(:,15);
%% Stock
nasdaq=xls_data_2(:,1);
s_p=xls_data_2(:,2);
djia=xls_data_2(:,3);