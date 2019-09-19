from cmath import *

# Центрирование вещественной величины
def centering(s):
    return (s - s.mean())


# Центрирование комплекснозначной величины
def complex_centering(s):
    return (centering(s.real) + 1j*centering(s.imag))


# Приведение вещественной величины к безразмерному виду
def dimensionless(s):
    if (s[s!=0].shape[0]==0):
        return s
    else: 
        return (s / s[s!=0].max())

    
# Приведение комплекснозначной величины к безразмерному виду
def complex_dimensionless(s):
    return (dimensionless(s.real) + 1j*dimensionless(s.imag))


# Препроцессинг
def preprocessing(s):
    s = complex_centering(s)
    s = complex_dimensionless(s)
    return s


# Нахождение комплексного коэффициента парной корреляции
def rc(y,x):
    yr, yi = y.real, y.imag
    xr, xi = x.real, x.imag
    
    rc_xy = (
        ((yr + 1j*yi)*(xr + 1j*xi)).sum()
        / 
        sqrt(((yr + 1j*yi)**2).sum() * ((xr + 1j*xi)**2).sum())
        )
    return rc_xy;




#
# OLD
#

# Расчет комплексного коэффициента пропорциональности (4.2.11)
def b(x,y):
    b_xy = (
        ((y.real + 1j*y.imag)*(x.real - 1j*x.imag)).sum()
    / 
        ((x.real + 1j*x.imag)*(x.real - 1j*x.imag)).sum()
    )
    return b_xy;


# Расчет выборочного значения коэффициента корреляции двух комплексных случайных величин (4.3.6)
def r(x,y):
    r_xy = ((
        ((y.real - y.real.mean())*(y.imag - y.imag.mean())).sum() + 
        ((x.real - x.real.mean())*(x.imag - x.imag.mean())).sum() + 
    1j*(((x.real - x.real.mean())*(y.imag - y.imag.mean())).sum() + 
        ((y.real - y.real.mean())*(x.imag - x.imag.mean())).sum())
    )  
    / 
    (
        (((x.real - x.real.mean())**2).sum() + ((x.imag - x.imag.mean())**2).sum()) * 
        (((y.real - y.real.mean())**2).sum() + ((y.imag - y.imag.mean())**2).sum())
    ))
    return r_xy;