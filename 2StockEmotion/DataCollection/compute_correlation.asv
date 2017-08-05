% Author: Yuhao Kang
% Function: Correlation between stock and emotion
% 计算股票与情绪之间的相关性
load emotion_data_manhattan.mat
load emotion_data_toklon.mat
%% Correlation Manhattan
djia_nor=zscore(djia);
nasdaq_nor=zscore(nasdaq);
s_p_nor=zscore(s_p);
corr(djia_nor,emotion_avg_nor)
corr(nasdaq_nor,emotion_avg_nor)
corr(s_p_nor,emotion_avg_nor)
%% Correlation London
ftse_nor=zscore(ftse);
corr(ftse_nor,emotion_avg_lon_nor)
%% Correlation Tokyo
n225_nor=zscore(n225);
corr(n225_nor,emotion_avg_tok_nor)