import numpy as np

from DualNumber import *

def cos(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which cos() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion cos() applied to x
    '''

    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
        return DualNumber(np.cos(x.real), -np.sin(x.real) * x.dual)
    else:
        return np.cos(x)

def sin(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which sin() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion sin() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
        return DualNumber(np.sin(x.real), np.cos(x.real) * x.dual)
    else:
        return np.sin(x)

def tan(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which tan() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion tan() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
        return DualNumber(np.tan(x.real), 1 / np.cos(x.real)**2 * x.dual)
    else:
        return np.tan(x)

def arccos(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which arccos() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion arccos() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
        return DualNumber(np.arccos(x.real), (-1/np.sqrt(1-x.real**2)) * x.dual)
    else:
        return np.arccos(x)


def arcsin(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which arcsin() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion arcsin() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
        return DualNumber(np.arcsin(x.real), (1/np.sqrt(1-x.real**2)) * x.dual)
    else:
        return np.arcsin(x)


def arctan(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which arctan() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion arctan() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
        return DualNumber(np.arctan(x.real), 1/(1+x.real**2) * x.dual)
    else:
        return np.arctan(x)

def cosh(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which cosh() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion cosh() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
        return DualNumber(np.cosh(x.real), np.sinh(x.real) * x.dual)
    else:
        return np.cosh(x)

def sinh(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which sinh() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion sinh() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
        return DualNumber(np.sinh(x.real), np.cosh(x.real) * x.dual)
    else:
        return np.sinh(x)

def tanh(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which tanh() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion tanh() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
        return DualNumber(np.tanh(x.real), (1 - np.tanh(x.real)**2) * x.dual)
    else:
        return np.tanh(x)

def arccosh(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which arccosh() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion arccosh() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
        return DualNumber(np.arccosh(x.real),  1 / np.sqrt(x.real ** 2 - 1) * x.dual)
    else:
        return np.arccosh(x)

def arcsinh(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which arcsinh() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion arcsinh() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")

    if isinstance(x, DualNumber):
        return DualNumber(np.arcsinh(x.real),  1 / np.sqrt(x.real ** 2 + 1) * x.dual)

    else:
        return np.arcsinh(x)

def arctanh(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which arctanh() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion arctanh() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")

    if isinstance(x, DualNumber):
        return DualNumber(np.arctanh(x.real),  1 / (1 - x.real**2) * x.dual)

    else:
        return np.arcsinh(x)

def sqrt(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which sqrt() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion sqrt() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")

    if isinstance(x, DualNumber):
        return DualNumber(np.sqrt(x.real), 0.5 / np.sqrt(x.real) * x.dual)

    else:
        return np.sqrt(x)

def exp(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which exp() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion exp() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")

    if isinstance(x, DualNumber):        
        return DualNumber(np.exp(x.real), np.exp(x.real) * x.dual)

    else:
        return np.exp(x)

def log(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which log() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion log() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
         return DualNumber(np.log(x.real), (1 / x.real) * x.dual)
    else:
        return np.log(x)

def log2(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which log2() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion log2() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
         return DualNumber(np.log(x.real) / np.log(2), (1 / x.real / np.log(2)) * x.dual)
    else:
        return np.log(x) / np.log(2)

def log10(x):
    '''
    Parameters
    ----------
    x : int / float / DualNumber object, required
        The object on which log10() is applied

    Raises
    ------
    TypeError
        If the type of input x is not supported

    Returns
    -------
        A new DualNumber with the elementary fucntion log10() applied to x
    '''
    if not isinstance(x, (int, float, DualNumber)):
        raise TypeError(f"Unsupported type `{type(x)}`")
    if isinstance(x, DualNumber):
         return DualNumber(np.log(x.real) / np.log(10), (1 / x.real / np.log(10)) * x.dual)
    else:
        return np.log(x) / np.log(10)

if __name__ == '__main__':

    z = DualNumber(2,1)

    f = cos(z)
    print('cos:\t ', f.real, f.dual)
    
    f = sin(z)
    print('sin:\t ',f.real, f.dual)

    f = tan(z)
    print('tan:\t ',f.real, f.dual)

    f = log(z)
    print('log:\t ',f.real, f.dual)

    f = cosh(z)
    print('cosh:\t ',f.real, f.dual)
    
    f = sinh(z)
    print('sinh\t ',f.real, f.dual)
    
    f = tanh(z)
    print('tanh\t ',f.real, f.dual)


    f = arccosh(z)
    print('arccosh:\t ',f.real, f.dual)
    
    
    z2 = DualNumber(0.5, 1)
    f = arccos(z2)
    print('arccos:\t ',f.real, f.dual)
    
    f = arcsin(z2)
    print('arcsin:\t ',f.real, f.dual)
    
    f = arctan(z2)
    print('arctan:\t ',f.real, f.dual)
    
    # With DualNumber(2, 1):
    # cos:	  0.5403023058681398 -0.8414709848078965
    # sin:	  0.8414709848078965 0.5403023058681398
    # tan:	  1.557407724654902 3.425518820814759
    # log:	  0.0 1.0
    # cosh:	  1.5430806348152437 1.1752011936438014
    # arccosh:	  0.0 inf
    # sinh: 3.6268604078470186 3.7621956910836314
    # tanh: 0.9640275800758169 0.07065082485316443
    
    # With DualNumber(0.5, 0.5)
    # arccos: 1.0471975511965976 -0.5773502691896258
    # arcsin: 0.5235987755982988 0.5773502691896258
    # arctan: 0.46364760900080615 0.4
