def alpha197(n = 20,m = 5):
    '''
        交易量与流通市值N天平均的比值滞后M期
        '''
    return dv.add_formula('alpha197','Delay(volume/Ts_Mean(float_mv,{}),{})'.format(n,m),is_quarterly = False)

def run_formula(dv, param = None):
    defult_param = {'n':20,'m':5}
    if not param:
        param = defult_param
    
    n = param['n']
    m = param['m']
    
    return dv.add_formula('alpha197','Delay(volume/Ts_Mean(float_mv,{}),{})'.format(n,m),is_quarterly = False)

