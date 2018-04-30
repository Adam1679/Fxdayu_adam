def alpha62_(n1 = 80,n2 = 8,n3 = 17):
    '''
    最低价和成交量N1天移动平均的N2天相关系数的横截面的Rank，再将Rank在N3天上线性衰减，最后再求一个横截面Rank
    '''
    return dv.add_formula('alpha62','-1*Rank(Decay_linear(Rank(Correlation(low_adj,Ts_Mean(volume,{}),{})),{}))'.format(n1,n2,n3),is_quarterly=False,overwrite=True)

def run_formula(dv, param = None):
    defult_param = {'n1':80,'n2':8,'n3':17}
    if not param:
        param = defult_param
    
    n1 = param['n1']
    n2 = param['n2']
    n3 = param['n3']

    return dv.add_formula('alpha62','-1*Rank(Decay_linear(Rank(Correlation(low_adj,Ts_Mean(volume,{}),{})),{}))'.format(n1,n2,n3),is_quarterly=False,overwrite=True)

