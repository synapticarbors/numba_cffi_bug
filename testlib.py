from __future__ import print_function

import numpy as np
import numba as nb

from numba import cffi_support

import _rmath_ffi

cffi_support.register_module(_rmath_ffi)


pnorm = _rmath_ffi.lib.pnorm
qnorm = _rmath_ffi.lib.qnorm
runif = _rmath_ffi.lib.runif
set_seed = _rmath_ffi.lib.set_seed

set_seed(123, 456)

@nb.njit
def f():
    zlo = np.random.random()
    zhi = np.random.random()
    if zlo > 0.0:
        plo = pnorm(-zhi, 0.0, 1.0, 1, 0)
        phi = pnorm(-zlo, 0.0, 1.0, 1, 0)
    else:
        plo = pnorm(zlo, 0.0, 1.0, 1, 0)
        phi = pnorm(zhi, 0.0, 1.0, 1, 0)

    p = runif(plo, phi)
    z = qnorm(p, 0.0, 1.0, 1, 0)

    return p * z

@nb.njit
def _run():
    set_seed(123, 456)

    return f()


def run():
    print(_run())



if __name__ == '__main__':
    run()
