def alpha208(n = 5):
    if 'R' not in dv.fileds:
        R = GetResidual()
        dv.append_df(R,'R')
    return dv.add_formula('alpha208','Decay_linear(R,{})'.format(n),is_quarterly=False,overwrite=True)