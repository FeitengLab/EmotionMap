% Author: Yuhao Kang
% Function: Manhattan workflow
%% Read data from excel
% Manhattan
% �޸��ļ�·��,������������.
xls_data_1=xlsread('Data_Man.xlsx',1);
xls_data_2=xlsread('Data_Man.xlsx',2);
emotion_data=xls_data_1(:,2:9);
%% PCA
% �����ﾧMATLAB5.pdf�޸�
S=cov(emotion_data);%��Э����
[U,V]=eig(S);
E=transpose(rot90(U));
G=rot90(rot90(V));
eigv=diag(G);
per=eigv/sum(eigv);
%% Compute emotion score
% �鿴Z�Ľ��.�����Ƶ�excel����.����֮�����¼�������
Z=-emotion_data*E(:,1);
%% Reload xlsdata
xls_data_1=xlsread('Data_Man.xlsx',1);
%% Emotion
month=xls_data_1(:,12);
day=xls_data_1(:,13);
year=xls_data_1(:,14);
emotion=xls_data_1(:,15);
%% Stock
nasdaq=xls_data_2(:,1);
s_p=xls_data_2(:,2);
djia=xls_data_2(:,3);
%% Export data to .mat
% ������7�����ݵ���Ϊ.mat��ʽ�ļ������µ���
load emotion_data_manhattan.mat;
%% Compute emotion average and deviation
p=1;
for i_year=2012:2016
    for i_month=1:12
        temp=find(year==i_year & month==i_month);
        emotion_avg(p,1)=mean(emotion(temp));
        emotion_std(p,1)=std(emotion(temp));
        p=p+1;
    end
end
%% Normalize
emotion_avg_nor=zscore(emotion_avg);
%% Plot emotion change
plot(emotion_avg_nor);
%% Correlation at Manhattan
djia_nor=zscore(djia);
nasdaq_nor=zscore(nasdaq);
s_p_nor=zscore(s_p);
corr(djia_nor,emotion_avg_nor)
corr(nasdaq_nor,emotion_avg_nor)
corr(s_p_nor,emotion_avg_nor)
