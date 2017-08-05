% Author: Yuhao Kang
% Function: 计算月平均情绪值 伦敦和东京
% 修改文件路径,导入情绪数据 emotion_data.mat.
%% Read data from excel
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