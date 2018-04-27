#IC 0.037 IR 0.317
def alpha210(n = 20):
    if 'R' not in dv.fileds:
        R = GetResidual()
        dv.append_df(R,'R')
    return dv.add_formula('alpha210','Ts_Rank(R,{})'.format(n),is_quarterly=False,overwrite=True)