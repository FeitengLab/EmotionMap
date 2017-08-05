% Author: Yuhao Kang
% Function: PCA ���ɷַ���
% �޸��ļ�·��,������������.
% �鿴Z�Ľ��.�����Ƶ�excel����.
% �����ﾧMATLAB5.pdf�޸�
%% Read data from excel
% Manhattan
% xls_data=xlsread('Data_Man.xlsx',1);
% emotion_data=xls_data(:,2:9);

% London Tokyo
xls_data=xlsread('Data_Tok_Lon.xlsx',1);
emotion_data=xls_data(:,4:11);
%% PCA
S=cov(emotion_data);%��Э����
[U,V]=eig(S);
E=transpose(rot90(U));
G=rot90(rot90(V));
eigv=diag(G);
per=eigv/sum(eigv);
%% Compute emotion score
Z=-emotion_data*E(:,1);