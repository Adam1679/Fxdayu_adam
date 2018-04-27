#20:IC -0.012 IR -0.139;400:-0.046 IR -0.407
def alpha206(n = 400):
    return dv.add_formula('alpha206','volume*{}/Ts_Sum(volume,{})'.format(n,n),is_quarterly=False,overwrite=True)

