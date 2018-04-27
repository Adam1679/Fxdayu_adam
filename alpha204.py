#IC 0.038 IR 0.484
def alpha204(n = 5,m = 10):
    return dv.add_formula('alpha204','If(Quantile(volume,5)>3,Delay(Return(close_adj,{}),{}),Delay(Return(close_adj,{}+5),{})+5)'.format(n,m,n,m),is_quarterly = False)

