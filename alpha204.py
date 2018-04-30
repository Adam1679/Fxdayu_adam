def alpha204(n = 5,m = 10):
    '''
        若横截面交易量5分quantile在3以上，则取收盘价M天收益率的N天滞后，否则取M+5天收益率的N+5天滞后。
        '''
    return dv.add_formula('alpha204','If(Quantile(volume,5)>3,Delay(Return(close_adj,{}),{}),Delay(Return(close_adj,{}+5),{})+5)'.format(n,m,n,m),is_quarterly = False)

def run_formula(dv, param = None):
    defult_param = {'n':5,'m':10}
    if not param:
        param = defult_param
    
    n = param['n']
    m = param['m']

    return dv.add_formula('alpha204','If(Quantile(volume,5)>3,Delay(Return(close_adj,{}),{}),Delay(Return(close_adj,{}+5),{})+5)'.format(n,m,n,m),is_quarterly = False)

