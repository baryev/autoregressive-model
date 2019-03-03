def r(x,y):
    r_xy = (
        ((y.real - y.real.mean())*(y.imag - y.imag.mean())).sum() + 
        ((x.real - x.real.mean())*(x.imag - x.imag.mean())).sum() + 
    1j*(((x.real - x.real.mean())*(y.imag - y.imag.mean())).sum() + 
        ((y.real - y.real.mean())*(x.imag - x.imag.mean())).sum())
    ) 
    / 
    (
        (((x.real - x.real.mean())**2).sum() + ((x.imag - x.imag.mean())**2).sum()) * 
        (((y.real - y.real.mean())**2).sum() + ((y.imag - y.imag.mean())**2).sum())
    )
    return r_xy;