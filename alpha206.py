def alpha206(n = 400):
    '''
        N*成交量比上前N天成交量的总和
        '''
    return dv.add_formula('alpha206','volume*{}/Ts_Sum(volume,{})'.format(n,n),is_quarterly=False,overwrite=True)

def run_formula(dv, param = None):
    defult_param = {'n':400}
    if not param:
        param = defult_param
    
    n = param['n']

    return dv.add_formula('alpha206','volume*{}/Ts_Sum(volume,{})'.format(n,n),is_quarterly=False,overwrite=True)
