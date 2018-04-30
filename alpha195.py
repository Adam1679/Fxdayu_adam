def alpha195(n1 = 200,n2 = 20):
    '''
        交易量与流通市值N天平均的比值的方差
        '''
    return dv.add_formula('alpha195','StdDev(volume/Ts_Mean(float_mv,{}),{})'.format(n1,n2),is_quarterly = False)

def run_formula(dv, param = None):
    defult_param = {'n1':200,'n2':20}
    if not param:
        param = defult_param

    n1 = param['n1']
    n2 = param['n2']
    
    return dv.add_formula('alpha195','StdDev(volume/Ts_Mean(float_mv,{}),{})'.format(n1,n2),is_quarterly = False)

