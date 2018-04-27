#IC 0.037 IR 0.313
def alpha209(n = 5):
    if 'R' not in dv.fileds:
        R = GetResidual()
        dv.append_df(R,'R')
    return dv.add_formula('alpha209','Rank(R)',is_quarterly=False,overwrite=True)