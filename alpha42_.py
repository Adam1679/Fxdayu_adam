def run_formula(dv, param = None):
    '''
        最高价在N天的方差的横截面Rank乘以最高价和成交量的N天相关系数
        '''
    defult_param = {'n':8}
    if not param:
        param = defult_param
    
    n = param['n']

    return dv.add_formula('alpha42','Rank(StdDev(high,{}))*Correlation(high,volume,{})'.format(n,n),is_quarterly=False,overwrite=True)

