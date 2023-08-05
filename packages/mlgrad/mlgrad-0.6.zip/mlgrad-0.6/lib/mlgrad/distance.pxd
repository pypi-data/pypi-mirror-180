# cython: language_level=3

cimport cython

cdef class Distance:    
    cdef double _evaluate(self, double *x, double *y, Py_ssize_t n) nogil
    cdef double evaluate(self, double[::1] x, double[::1] y) nogil
    cdef void gradient(self, double[::1] x, double[::1] y, double[::1]) nogil
    cdef set_param(self, name, val)

cdef class DistanceWithScale(Distance):
    cdef public double[:,::1] S
    cdef public double sigma
    
@cython.final
cdef class AbsoluteDistance(Distance):
    pass

@cython.final
cdef class EuclidDistance(Distance):
    pass

@cython.final
cdef class MahalanobisDistance(DistanceWithScale):
    pass

@cython.final
cdef class PowerDistance(Distance):
    cdef double p

