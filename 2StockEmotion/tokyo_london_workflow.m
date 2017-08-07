% Author: Yuhao Kang
% Function: Tokyo & London workflow
%% Read data from excel
% Tokyo & London
% �޸��ļ�·��,������������.
xls_data_1=xlsread('Data_Tok_Lon.xlsx',1);
xls_data_2=xlsread('Data_Tok_Lon.xlsx',2);
emotion_data=xls_data_1(:,4:11);
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
xls_data_1=xlsread('Data_Tok_Lon.xlsx',1);
%% Emotion
month=xls_data_1(:,1);
day=xls_data_1(:,2);
year=xls_data_1(:,3);
emotion=xls_data_1(:,14);
site=xls_data_1(:,15);
%% Stock
ftse=xls_data_2(:,4);% London
n225=xls_data_3(:,4);% Tokyo
%% Export data to .mat
% ������7�����ݵ���Ϊ.mat��ʽ�ļ������µ���
load emotion_data_toklon.mat;
%% London
%% Compute emotion average and deviation
p=1;
for i_year=2012:2016
    for i_month=1:12
        temp=find(year==i_year & month==i_month & site==0);
        emotion_avg_lon(p,1)=mean(emotion(temp));
        emotion_std_lon(p,1)=std(emotion(temp));
        p=p+1;
    end
end
%% Normalize
emotion_avg_lon_nor=zscore(emotion_avg_lon);
%% Plot emotion change
plot(emotion_avg_lon_nor);
%% Correlation London
ftse_nor=zscore(ftse);
corr(ftse_nor,emotion_avg_lon_nor)
%% Tokyo
%% Compute emotion average and deviation
p=1;
for i_year=2012:2016
    for i_month=1:12
        temp=find(year==i_year & month==i_month & site==1);
        emotion_avg_tok(p,1)=mean(emotion(temp));
        emotion_std_tok(p,1)=std(emotion(temp));
        p=p+1;
    end
end
%% Normalize
emotion_avg_tok_nor=zscore(emotion_avg_tok);
%% Plot emotion change
plot(emotion_avg_tok_nor);
%% Correlation Tokyo
n225_nor=zscore(n225);
corr(n225_nor,emotion_avg_tok_nor)