% Author: Yuhao Kang
% Function: PCA ���ɷַ���
% �޸��ļ�·��,������������.
% �鿴Z�Ľ��.�����Ƶ�excel����.
% ��emotion_data����Ϊ.mat��ʽ�ļ�
% �����ﾧMATLAB5.pdf�޸�
%% Read data from excel
xls_data=xlsread('Data.xlsx',1);
emotion_data=xls_data(:,2:9);
%% PCA
S=cov(emotion_data);%��Э����
[U,V]=eig(S);
E=transpose(rot90(U));
G=rot90(rot90(V));
eigv=diag(G);
per=eigv/sum(eigv);
%% Compute emotion score
Z=-emotion_data*E(:,1);