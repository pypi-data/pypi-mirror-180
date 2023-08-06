# -*- coding: utf-8 -*-
# ---
# @Software: PyCharm
# @File: x_retention_model.py
# @AUthor: Fei Wu
# @Time: 11月, 23, 2022
import pandas as pd
from scipy.optimize import minimize
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from frechetdist import frdist
# from matplotlib import pyplot as plt

class Retention:
    def __init__(self, total_cp: int, lost_cp: pd.Series):
        self.lost_cp = lost_cp
        self.total_cp = total_cp

    def ab_predict(self):
        L_func = lambda x:  -sum(self.lost_cp * [np.log(self.p_func(i,x[0],x[1])) for i in range(1,len(self.lost_cp)+1)]) \
                            - (self.total_cp - self.lost_cp.sum()) * np.log(self.s_func(len(self.lost_cp),x[0],x[1]))
        e = 1e-10
        cons = (
            {'type': 'ineq', 'fun': lambda x: x[0] - e},
            {'type': 'ineq', 'fun': lambda x: x[1] - e},
        )
        x0 = [1, 1]
        res = minimize(L_func, x0, method='SLSQP', constraints=cons)
        return res.x

    @staticmethod
    def p_func(t, a, b):
        p_1 = a / (a + b)
        if t == 1:
            return a / (a + b)
        else:
            for i in range(2, t + 1):
                p_1 = p_1 * (b + i - 2) / (a + b + i - 1)
            return p_1

    @staticmethod
    def s_func(t, a, b):
        r = 1
        for i in range(1, t + 1):
            r = r * (b + i - 1) / (a + b + i - 1)
        return r

class MonthRetention:
    def __init__(self, data, start_month='start_month', lag_month='lag_month', pr='pr', cp_num='cp_num'):
        '''
        :param data: 历史月数据，包含历史所有月引入cohort的发文数、活跃CP数、留存率，直接从数据库下载得到
        :param start_month: 引入月的字段名 该字段默认为整型
        :param lag_month: 观测月的字段名 该字段默认为整型
        :param pr: 留存率的字段名 该字段默认为为浮点型
        :param cp_num: 活跃人数的字段名 该字段默认为整型
        '''
        self.data = data
        self.start_month = start_month
        self.lag_month = lag_month
        self.pr = pr
        self.cp_num = cp_num

    def args_predict(self):
        '''
        :return: 返回两个dataFrame类型，第一个返回历史所有引入月的当月留存率m0_active_cp和估计的留存率模型参数args；第二个是调整后的历史留存率
        数据，每一列为一个引入月cohort
        comment: 对于有6个月及以上（不含引入当月）的cohort，直接使用对应cohort估计参数，其他使用最近的满足6个月及以上条件的cohort的参数值，保留引入当月的留存率
        '''
        self.data['lag'] = self.data[self.lag_month].apply(lambda x: int(str(x)[0:4]) * 12 + int(str(x)[4:])) - \
                self.data[self.start_month].apply(lambda x: int(str(x)[0:4]) * 12 + int(str(x)[4:]))
        df1 = pd.pivot(self.data, index='lag', columns=self.start_month, values=self.pr)
        df2 = pd.pivot(self.data, index='lag', columns=self.start_month, values=self.cp_num)
        result = pd.DataFrame(index=df1.columns, columns=['m0_active_cp','args'])
        for col in df2.columns:
            first_pr = df1.iloc[0][col]
            result.loc[col, 'm0_active_cp'] = first_pr
            if df2[col].dropna().shape[0] >= 7:
                active_cp = df2[col].dropna()
                total_cp = df2.iloc[0][col] / df1.iloc[0][col]
                active_cp.iloc[0] = total_cp
                lost_cp = active_cp.shift(1) - active_cp
                lost_cp = lost_cp.dropna()
                cl = Retention(total_cp, lost_cp)
                ab = cl.ab_predict()
                result.loc[col]['args'] = ab
        result['args'] = result['args'].fillna(method='ffill')
        return result, df1

    def month_range(self, start_month, end_month):
        '''
        计算两个月份间的所有月份列表
        :param start_month: int类型，如202202，开始月份
        :param end_month: int类型，如202210，结束月份
        :return: list类型，返回两月份间的所有月份，含开始和结束月份，每个元素是字符型
        '''
        months = 12*(int(str(end_month)[0:4]) - int(str(start_month)[0:4])) + int(str(end_month)[4:]) - int(str(start_month)[4:])
        month_range = ['%04d%02d' % (int(int(str(start_month)[0:4]) + n // 12), int(n % 12 + 1))
                       for n in range(int(str(start_month)[4:])-1, int(str(start_month)[4:]) + months)]
        return month_range

    def retention_predict_per_month(self, pre_month: int):
        '''
        给定一个需要预测留存率的月份，返回截止到预测月份（含），所有引入月份在预测月份的留存率
        :param pre_month: int类型，需要预测留存率的月份
        :return: 不同引入月份在预测月份的留存率
        comment: 当预测月份是历史数据中的一个cohort，直接返回历史留存率；当预测月份非历史数据中的cohort，利用args_predict的留存模型参数进行
        预测，同时预测月份当月的留存率用最近的历史cohort的首月留存率代入
        '''
        args, df = self.args_predict()
        month_list = self.month_range(min(df.columns.tolist()), pre_month)
        month_list = sorted([int(i) for i in month_list])
        result = pd.DataFrame(index=month_list, columns=[pre_month])
        # print(args)
        if pre_month in args.index:
            for col in month_list:
                lag_month = 12 * (int(str(pre_month)[0:4]) - int(str(col)[0:4])) + int(str(pre_month)[4:]) - int(str(col)[4:])
                result.loc[col, pre_month] = df.loc[lag_month][col]
        else:
            for col in month_list:
                lag_month = 12 * (int(str(pre_month)[0:4]) - int(str(col)[0:4])) + int(str(pre_month)[4:]) - int(str(col)[4:])
                # 计算预测值
                try:
                    result.loc[col, pre_month] = Retention.s_func(lag_month, *args.loc[col]['args'])
                except:
                    result.loc[col,pre_month] = Retention.s_func(lag_month, *args.iloc[-1]['args'])
            result.loc[pre_month, pre_month] = args.iloc[-1]['m0_active_cp']
        return result

class Pubnum:
    def __init__(self, data, start_month='start_month', lag_month='lag_month', cp_num='cp_num', pub_num='pub_num'):
        self.data = data
        self.data['avg_pub'] = self.data[pub_num] / self.data[cp_num]
        self.start_month = start_month
        self.lag_month = lag_month
        self.pub_num = pub_num
        self.cp_num = cp_num

    def avgpub_his(self):
        df = pd.pivot(self.data, index=self.lag_month, columns=self.start_month, values='avg_pub')
        result = pd.DataFrame(index=df.columns, columns=['m0_pub_num', 'avg_pub'])
        for col in df.columns:
            result.loc[col,'m0_pub_num'] = df.loc[col,col]
            result.loc[col,'avg_pub'] = df[df.index != col][col].iloc[-6:].mean()
        result = result.fillna(method='ffill')
        return result, df

    def month_range(self, start_month, end_month):
        '''
        计算两个月份间的所有月份列表
        :param start_month: int类型，如202202，开始月份
        :param end_month: int类型，如202210，结束月份
        :return: list类型，返回两月份间的所有月份，含开始和结束月份，每个元素是字符型
        '''
        months = 12*(int(str(end_month)[0:4]) - int(str(start_month)[0:4])) + int(str(end_month)[4:]) - int(str(start_month)[4:])
        month_range = ['%04d%02d' % (int(int(str(start_month)[0:4]) + n // 12), int(n % 12 + 1))
                       for n in range(int(str(start_month)[4:])-1, int(str(start_month)[4:]) + months)]
        return month_range

    def avgpub_predict(self, pre_month):
        '''
        :param pre_month: int类型，预测月份，如202301
        :return:
        '''
        r, df = self.avgpub_his()
        month_list = self.month_range(r.index.min(), pre_month)
        month_list = sorted([int(i) for i in month_list])
        result = pd.DataFrame(index=month_list, columns=[pre_month])
        if pre_month in r.index:
            result[pre_month] = df.T[pre_month].dropna()
        else:
            result[pre_month] = r['avg_pub']
            result[pre_month] = result[pre_month].fillna(method='ffill')
            try:
                result.loc[pre_month, pre_month] = r.loc[pre_month]['m0_pub_num']
            except:
                result.loc[pre_month, pre_month] = r.iloc[-1]['m0_pub_num']
        return result

class MonthPubCalc:
    def __init__(self, data, total_cp:pd.Series,
                 start_month='start_month', lag_month='lag_month', cp_num='cp_num', pub_num='pub_num', pr='pr'):
        self.data = data
        self.start_month = start_month
        self.lag_month = lag_month
        self.pub_num = pub_num
        self.cp_num = cp_num
        self.pr = pr
        self.total_cp = total_cp.copy()
        self.data['total_cp'] = self.data['cp_num'] / self.data['pr']

    def calc_month_pubnum(self,pre_month):
        '''
        :param pre_month: 预测月份
        :param total_cp:  截止预测月份每月新引入的的作者数，索引为月，如202201
        :return: 预测月份的发文数
        '''
        retention = MonthRetention(self.data, start_month=self.start_month, lag_month=self.lag_month,pr=self.pr,cp_num=self.cp_num)
        avgpub = Pubnum(self.data,start_month=self.start_month,lag_month=self.lag_month,cp_num=self.cp_num,pub_num=self.pub_num)
        retention_rate = retention.retention_predict_per_month(pre_month)
        avgpub_num = avgpub.avgpub_predict(pre_month)
        pubnum = retention_rate[pre_month] * avgpub_num[pre_month] * self.total_cp
        return pubnum.sum()

    def month_range(self, start_month, end_month):
        '''
        计算两个月份间的所有月份列表
        :param start_month: int类型，如202202，开始月份
        :param end_month: int类型，如202210，结束月份
        :return: list类型，返回两月份间的所有月份，含开始和结束月份，每个元素是字符型
        '''
        months = 12*(int(str(end_month)[0:4]) - int(str(start_month)[0:4])) + int(str(end_month)[4:]) - int(str(start_month)[4:])
        month_range = ['%04d%02d' % (int(int(str(start_month)[0:4]) + n // 12), int(n % 12 + 1))
                       for n in range(int(str(start_month)[4:])-1, int(str(start_month)[4:]) + months)]
        return month_range
    def calc_monthlist_pubnum(self,start,end):
        month_list = self.month_range(start, end)
        month_list = [int(month) for month in month_list]
        result = pd.DataFrame(index=month_list, columns=['pubnum'], data=month_list)
        result['pubnum'] = result.pubnum.apply(lambda x: self.calc_month_pubnum(x))
        return result

class IncomePredict:
    def __init__(self, df_his: pd.DataFrame, df_pre:pd.DataFrame, month:str, delta_days:str, vv_income:str, n=15, m=90):
        """
        :param df_his: 历史流量or收入，按月
        :param df_pre: 需预测月份的发文后n天内流量or收入
        :param month: 月份字段名
        :param delta_days: 发文后时间间隔，发文当天为0
        :param vv_income: 流量or收入
        :param n: 预测月份发文后有流量、收入数据的最小天数 默认15
        :param m: 需要预测的天数
        """
        self.df_his = df_his  #15天收入or收入,保证第一列为发文月份，第二列为发文后第n天，第三列为流量或收入
        self.df_pre = df_pre
        self.month = month
        self.delta_days = delta_days
        self.vv_income = vv_income
        self.n = n
        self.m = m
        return

    def data_select(self):
        data1 = pd.pivot(self.df_his, index=self.delta_days, columns=self.month, values=self.vv_income)
        data2 = pd.pivot(self.df_pre, index=self.delta_days, columns=self.month, values=self.vv_income)
        data1 = data1.iloc[0:self.m].cumsum(axis=0)
        data2 = data2.iloc[0:self.n].cumsum(axis=0)
        corr_dict = {}
        for col in data2.columns:
            temp = data1.iloc[0:self.n].apply(lambda x: np.corrcoef(x, data2[col])[0,1])
            temp.sort_values(ascending=False, inplace=True)
            corr_dict.update({col: temp.index[0]})
        return data1, data2, corr_dict

    def data_select_fr(self):
        data1 = pd.pivot(self.df_his, index=self.delta_days, columns=self.month, values=self.vv_income)
        data2 = pd.pivot(self.df_pre, index=self.delta_days, columns=self.month, values=self.vv_income)
        data1 = data1.iloc[0:self.m].cumsum(axis=0)
        data2 = data2.iloc[0:self.n].cumsum(axis=0)
        scaler = StandardScaler()
        data1_st = pd.DataFrame(scaler.fit_transform(data1.iloc[0:self.n]), index=data1.iloc[0:self.n].index, columns=data1.columns)
        data2_st = pd.DataFrame(scaler.fit_transform(data2), index=data2.index, columns=data2.columns)
        fr_dict = {}
        for col in data2_st.columns:
            temp = data1_st.apply(lambda x: frdist(list(zip(range(self.n), x)), list(zip(range(self.n),data2[col]))))
            temp.sort_values(ascending=False, inplace=True)
            fr_dict.update({col: temp.index[0]})
        return data1, data2, fr_dict

    def calc_income_vv(self, method='corr'):
        if method == 'corr':
            data1, data2, corr_dict = self.data_select()
        else:
            data1, data2, corr_dict = self.data_select_fr()
        result = []
        for col in data2.columns:
            pre = data2.iloc[-1][col] / data1.iloc[self.n-1][corr_dict[col]] * data1.iloc[-1][corr_dict[col]]
            result.append((col, pre))
        return result

if __name__ == '__main__':
    df = pd.read_csv('D:/项目/X项目/X发文预估模型/留存模型/X引入留存(月).csv', encoding='utf-8')
    df['cp'] = df['cp_num'] / df['pr']
    total_cp = df.groupby('start_month')['cp'].max()
    df = df[(df.start_month <= 202209) & (df.lag_month <= 202209)]
    df['lag'] = df['lag_month'].apply(lambda x: int(str(x)[0:4]) * 12 + int(str(x)[4:])) - \
                df['start_month'].apply(lambda x: int(str(x)[0:4]) * 12 + int(str(x)[4:]))
    df1 = pd.pivot(df, index='lag', columns='start_month', values='pr')
    df2 = pd.pivot(df, index='lag', columns='start_month', values='cp_num')
    # first_pr = df1.apply(lambda x: (x.sum() - x.min() - x.max()) / (len(x.dropna())-2) if len(x.dropna()) > 2 else x.mean(), axis=1).iloc[0]
    # survive_pr = df1.loc[1:][202107].dropna()
    # month1 = 202111
    # first_pr = df1.iloc[0][month1]
    # active_cp = df2.iloc[0:7][month1].dropna()
    # total_cp = df2.iloc[0][month1] / df1.iloc[0][month1]
    # active_cp.iloc[0] = total_cp
    # lost_cp = active_cp.shift(1) - active_cp
    # lost_cp = lost_cp.dropna()

    #取202107-202202的总数进行参数估计
    # active_cp = df2.iloc[:9,1:9]
    # active_cp = active_cp.sum(axis=1)
    # total_cp = sum(df2.iloc[0][1:9] / df1.iloc[0][1:9])
    # active_cp.iloc[0] = total_cp
    # lost_cp = active_cp.shift(1) - active_cp
    # lost_cp = lost_cp.dropna()
    # cl = Retention(total_cp, lost_cp)
    # ab = cl.ab_predict()
    # print(ab)
    #预测效果评估
    # month = 202205
    # y = [cl.s_func(i, *ab) for i in range(1, df1.iloc[1:][month].dropna().shape[0])]
    # # print(cl.s_func(36, *ab))
    # y = [first_pr] + y
    # x = list(range(df1[month].dropna().iloc[0:-1].shape[0]))
    # plt.plot(x, y, color='red', label='predict')
    # plt.plot(x, df1[month].dropna().iloc[0:-1], color='blue', label='actual')
    # plt.ylim([0,1])
    # plt.xticks(x)
    # plt.legend()
    # plt.show()
    # print('MAPE:',np.mean(abs(y - df1[month].dropna().iloc[0:-1]) / df1[month].dropna().iloc[0:-1]))
    # print('last_month MAPE:', abs(y[-1] - df1[month].dropna().iloc[-2]) / df1[month].dropna().iloc[-2])
    ra = MonthRetention(df)
    print(ra.retention_predict_per_month(202210))
    la = Pubnum(df)
    print(la.avgpub_predict(202210))
    total_cp_add = pd.Series(index=[202212,202301,202302,202303,202304,202305,202306,202307,202308,202309,202310,202311,202312])
    total_cp = pd.concat([total_cp, total_cp_add], axis=0)
    total_cp = total_cp.fillna(method='ffill')
    # print(total_cp)
    p = MonthPubCalc(df, total_cp)
    print('发文数：', p.calc_monthlist_pubnum(202301,202312))
