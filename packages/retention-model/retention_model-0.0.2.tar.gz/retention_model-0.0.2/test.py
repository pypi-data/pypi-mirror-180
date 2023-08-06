# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: test.py
# @AUthor: Fei Wu
# @Time: 12月, 09, 2022
import pandas as pd
from retention_model.x_retention_model import *

if __name__ == '__main__':
    data = pd.read_csv('D:\\项目\\X项目\\X发文预估模型\\留存模型\\x_retention_model\\x_retention_model\\x引入留存11月.csv', encoding='utf-8')
    data = data[(data.start_month <= 202208) & (data.lag_month <= 202208)]
    cp_list = pd.read_excel('D:\\项目\\X项目\\X发文预估模型\\留存模型\\x_retention_model\\x_retention_model\\引入作者.xlsx')
    cp_list.set_index('月', drop=1,inplace=True)
    ra = MonthRetention(data)
    # print(ra.retention_predict_per_month(202210))
    pb = Pubnum(data)
    print(pb.avgpub_back_his())
    print(pb.avg_backpub_predict(202209))
    # mc = MonthPubCalc(data, cp_list['人数'])
    # print('发文数：', mc.calc_monthlist_pubnum(202201,202312))
    # mc.calc_monthlist_pubnum(202201, 202312).to_csv('发文量.csv', encoding='utf-8')


