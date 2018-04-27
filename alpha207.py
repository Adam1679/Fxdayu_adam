#IC 0.036 IR 0.306
def alpha207(n = 5):
    if 'R' not in dv.fileds:
        R = GetResidual()
        dv.append_df(R,'R')
    return dv.add_formula('alpha207','Ts_Mean(R,{})'.format(n),is_quarterly=False,overwrite=True)