提供不同cohort留存率的预测、发文预测、90天、180天流量、收入预测等

使用方式如下：

    #发文预测
    df = pd.read_csv('D:/项目/X项目/X发文预估模型/留存模型/X引入留存(月).csv', encoding='utf-8')
    df['cp'] = df['cp_num'] / df['pr']
    total_cp = df.groupby('start_month')['cp'].max()
    df = df[(df.start_month <= 202209) & (df.lag_month <= 202209)]
    df['lag'] = df['lag_month'].apply(lambda x: int(str(x)[0:4]) * 12 + int(str(x)[4:])) - \
                df['start_month'].apply(lambda x: int(str(x)[0:4]) * 12 + int(str(x)[4:]))
    df1 = pd.pivot(df, index='lag', columns='start_month', values='pr')
    df2 = pd.pivot(df, index='lag', columns='start_month', values='cp_num')
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
    
    #流量预测
    data = pd.read_csv('发文90天内流量.csv', encoding='utf-8')
    his = data[data.month1 != 202207]
    pre = data[data.month1 == 202207]
    cl = IncomePredict(his, pre, month='month1', delta_days='delta_days', vv_income='vv', n=15, m=90)
    result = cl.calc_income_vv(method='frdist')
    print(result)
    print(pre.sum())