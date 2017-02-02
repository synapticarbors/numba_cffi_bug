import glob
import os

from cffi import FFI


include_dirs = [os.path.join('libraries', 'Rmath', 'src'),
                os.path.join('libraries', 'Rmath', 'include')]

rmath_src = glob.glob(os.path.join('libraries', 'Rmath', 'src', '*.c'))

# Take out dSFMT dependant files
rmath_src = [f for f in rmath_src if 'librandom.c' not in f]
rmath_src = [f for f in rmath_src if 'randmtzig.c' not in f]

extra_compile_args = ['-DMATHLIB_STANDALONE', '-std=c99']

ffi = FFI()
ffi.set_source('_rmath_ffi', '#include <Rmath.h>',
        include_dirs=include_dirs,
        sources=rmath_src,
        libraries=[],
        extra_compile_args=extra_compile_args)

ffi.cdef('''\
double pnorm(double, double, double, int, int);
double qnorm(double, double, double, int, int);
double runif(double, double);
void set_seed(unsigned int, unsigned int);
''')

if __name__ == '__main__':
    ffi.compile(verbose=True)
