#IC -0.062, IR -0.544
def alpha216(n = 20):
    if 'GetResidual2' not in dv.fileds:
        dv.append_df(GetResidual2(),'GetResidual2')
    return dv.add_formula('alpha216','StdDev(GetResidual2,{})'.format(n),is_quarterly=False,overwrite=True)


