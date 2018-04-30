def alpha194(n = 20):
    '''
        交易量与流通市值N天平均的比值
        '''
    return dv.add_formula('alpha194','volume/Ts_Mean(float_mv,{})'.format(n),is_quarterly = False)


def run_formula(dv, param = None):
    defult_param = {'n':20}
    if not param:
        param = defult_param

    n = param['n']
    
    return dv.add_formula('alpha194','volume/Ts_Mean(float_mv,{})'.format(n),is_quarterly = False)
