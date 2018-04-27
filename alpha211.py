#IC -0.062 IR -0.634
def alpha211(n = 20):
    if 'R' not in dv.fileds:
        R = GetResidual()
        dv.append_df(R,'R')
    return dv.add_formula('alpha211','StdDev(R,{})'.format(n),is_quarterly=False,overwrite=True)