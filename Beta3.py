
def run_formula(dv, param = None):
    import pandas as pd
    defult_param = {'n':20}
    if not param:
        param = defult_param

    n = param['n']
    if 'hs300' not in dv.fields:
        index_data = dv.data_benchmark
        close = dv.get_ts('close')
        hs300 = pd.DataFrame(index=close.index,columns=close.columns)
        for col in hs300:
            hs300[col] = index_data
        dv.append_df(hs300,'hs300',overwrite=True)

    return dv.add_formula('Beta2','Covariance(Ts_Rank(close_adj,{}),Ts_Rank(hs300,{}),{})/Pow(StdDev(Ts_Rank(hs300,{}),{}),2)'.format(n,n,n,n,n),is_quarterly=False)
