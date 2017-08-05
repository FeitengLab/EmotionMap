% Author: Yuhao Kang
% Function: 计算月平均情绪值
% 修改文件路径,导入情绪数据 emotion_data.mat.
%% Read data from excel
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