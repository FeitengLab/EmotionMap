% Author: Yuhao Kang
% Function: Correlation between stock and emotion
% �����Ʊ������֮��������
load emotion_data_manhattan.mat
%% Correlation
djia_nor=zscore(djia);
nasdaq_nor=zscore(nasdaq);
s_p_nor=zscore(s_p);
corr(djia_nor,emotion_avg_nor)
corr(nasdaq_nor,emotion_avg_nor)
corr(s_p_nor,emotion_avg_nor)