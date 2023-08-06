from typing import Union

import casadi as cs
import numpy as np


def array2cs(x: np.ndarray) -> Union[cs.SX, cs.MX]:
    """Converts numpy array `x` of scalar symbolic variable to a single symbolic
    instance. Opposite to `array2cs`. Note that all entries in `x` must have the same
    type, either SX or MX.

    Parameters
    ----------
    x : np.ndarray
        Array whose entries are either MX or SX. In case `x` is SX, MX or DM, it is
        returned immediately.

    Returns
    -------
    casadi.SX or MX
        A single SX or MX instance whose entries are `x`'s entries.

    Raises
    ------
    ValueError
        Raises if the array is empty (zero dimensions), or if it has more than 2 dims.
    """
    if isinstance(x, (cs.SX, cs.MX, cs.DM)):
        return x
    ndim = x.ndim
    if ndim == 0:
        raise ValueError("Cannot convert empty arrays.")
    elif ndim == 1:
        o = x[0]
        x = x.reshape(-1, 1)
    elif ndim == 2:
        o = x[0, 0]
    else:
        raise ValueError("Can only convert 1D and 2D arrays to CasADi SX or MX.")

    # infer type from first element
    sym_type = type(o)
    if sym_type is cs.SX:
        return cs.SX(x)
    shape = x.shape
    m = cs.MX(*shape)
    for i in np.ndindex(shape):
        m[i] = x[i]
    return m


def cs2array(x: Union[cs.MX, cs.SX]) -> np.ndarray:
    """Converts casadi symbolic variable `x` to a numpy array of scalars. Opposite to
    `array2cs`.

    Inspired by
    https://bitbucket.org/rawlings-group/mpc-tools-casadi/src/master/mpctools/tools.py

    Parameters
    ----------
    x : casadi.SX or MX
        A symbolic variable (with multiple entries).

    Returns
    -------
    np.ndarray
        The array containing the symbolic variable scalars.
    """
    if isinstance(x, np.ndarray):
        return x
    shape = x.shape
    y = np.empty(shape, dtype=object)
    for i in np.ndindex(shape):
        y[i] = x[i]
    return y
