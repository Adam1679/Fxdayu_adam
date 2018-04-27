def alpha197(n = 20,m = 5):
    return dv.add_formula('alpha197','Delay(volume/Ts_Mean(float_mv,{}),{})'.format(n,m),is_quarterly = False)