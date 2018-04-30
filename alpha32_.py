
def run_formula(dv, param = None):
    '''
        最高价的横截面Rank和成交量的横截面Rank的N天相关系数的横截面Rank，然后在时间序列N天上求和。
    '''
    defult_param = {'n':20}
    if not param:
        param = defult_param
    
    n = param['n']

    return dv.add_formula('alpha32','-1*Ts_Sum(Rank(Corr(Rank(high_adj),Rank(volume),{})),{})'.format(n,n),is_quarterly=False,overwrite=True)
