#-0.053
def alpha195(n = 20):
    return dv.add_formula('alpha195','StdDev(volume/Ts_Mean(float_mv,{}),{})'.format(n,n),is_quarterly = False)