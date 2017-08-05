% Author: Yuhao Kang
% Function: PCA 主成分分析
% 修改文件路径,导入情绪数据.
% 查看Z的结果.并复制到excel表里.
% 根据田晶MATLAB5.pdf修改
%% Read data from excel
% Manhattan
% xls_data=xlsread('Data_Man.xlsx',1);
% emotion_data=xls_data(:,2:9);

% London Tokyo
xls_data=xlsread('Data_Tok_Lon.xlsx',1);
emotion_data=xls_data(:,4:11);
%% PCA
S=cov(emotion_data);%求协方差
[U,V]=eig(S);
E=transpose(rot90(U));
G=rot90(rot90(V));
eigv=diag(G);
per=eigv/sum(eigv);
%% Compute emotion score
Z=-emotion_data*E(:,1);