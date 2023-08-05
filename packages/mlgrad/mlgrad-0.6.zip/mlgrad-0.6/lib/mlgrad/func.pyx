# coding: utf-8

# The MIT License (MIT)
#
# Copyright © «2015–2022» <Shibzukhov Zaur, szport at gmail dot com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, expRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from libc.math cimport fabs, pow, sqrt, fmax, exp, log, atan
from libc.math cimport isnan, isinf
from libc.stdlib cimport strtod

from cython.parallel cimport parallel, prange

from openmp cimport omp_get_num_procs

cdef int num_procs = 2 #omp_get_num_procs()
# if num_procs >= 4:
#     num_procs /= 2
# else:
#     num_procs = 2

import numpy as np

cimport cython

cdef double c_nan = strtod("NaN", NULL)
cdef double c_inf = strtod("Inf", NULL)

cdef dict _func_table = {}
def register_func(cls, tag):
    _func_table[tag] = cls
    return cls

def func_from_dict(ob):
    f = _func_table[ob['name']]
    return f(*ob['args'])

cdef class Func(object):
    #
    cdef double _evaluate(self, const double x) nogil:
        return 0.
    #
    def __call__(self, x):
        cdef double v = x
        return self._evaluate(v)
    #
    def __getitem__(self, x):
        cdef double v = x
        return self._derivative(v)
    #
    cdef double _derivative(self, const double x) nogil:
        return 0.
    #
    cdef double _derivative2(self, const double x) nogil:
        return 0.
    #
    cdef double _derivative_div_x(self, const double x) nogil:
        return self._derivative(x) / x
    #
    def evaluate_array(self, double[::1] x):
        cdef double[::1] y = np.empty(len(x), 'd')
        self._evaluate_array(&x[0], &y[0], x.shape[0])
        return y.base
    #
    def derivative_array(self, double[::1] x):
        cdef double[::1] y = np.empty(len(x), 'd')
        self._derivative_array(&x[0], &y[0], x.shape[0])
        return y.base
    #
    def derivative_div_array(self, double[::1] x):
        cdef double[::1] y = np.empty(len(x), 'd')
        self._derivative_div_array(&x[0], &y[0], x.shape[0])
        return y.base
    #
    cdef void _evaluate_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        for i in range(n):
            y[i] = self._evaluate(x[i])
    #
    cdef void _derivative_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        for i in range(n):
            y[i] = self._derivative(x[i])
    #
    cdef void _derivative2_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        for i in range(n):
            y[i] = self._derivative2(x[i])
    #
    cdef void _derivative_div_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        for i in range(n):
            y[i] = self._derivative_div_x(x[i])
    #
    cdef double _value(self, const double x) nogil:
        return x
    #
    cdef void _value_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        for i in range(n):
            y[i] = self._value(x[i])
    #
    def value_array(self, double[::1] x):
        cdef double[::1] y = np.empty(len(x), 'd')
        self._value_array(&x[0], &y[0], x.shape[0])
        return y.base
    #

cdef class Comp(Func):
    #
    def __init__(self, Func f, Func g):
        self.f = f
        self.g = g
    #
    cdef double _evaluate(self, const double x) nogil:
        return self.f._evaluate(self.g._evaluate(x))
    #
    cdef double _derivative(self, const double x) nogil:
        return self.f._derivative(self.g._evaluate(x)) * self.g._derivative(x)
    #
    cdef double _derivative2(self, const double x) nogil:
        cdef double dg = self.g._derivative(x)
        cdef double y = self.g._evaluate(x)

        return self.f._derivative2(y) * dg * dg + \
               self.f._derivative(y) * self.g._derivative2(x)
    #
    cdef double _derivative_div_x(self, const double x) nogil:
        return self.f._derivative(self.g._evaluate(x)) * self.g._derivative_div_x(x)

    def to_dict(self):
        return { 'name':'comp',
                'args': (self.f.to_dict(), self.g.to_dict() )
               }

cdef class CompSqrt(Func):
    #
    def __init__(self, Func f):
        self.f = f
    #
    cdef double _evaluate(self, const double x) nogil:
        cdef double v = sqrt(x)
        return self.f._evaluate(v)
    #
    cdef double _derivative(self, const double x) nogil:
        cdef double v = sqrt(x)
        return 0.5 * self.f._derivative_div_x(v)
    #
    cdef double _derivative2(self, const double x) nogil:
        cdef double y = sqrt(x)

        return 0.25 * (self.f._derivative2(y) / x - self.f._derivative(y) / (x*y))
    #
    cdef double _derivative_div_x(self, const double x) nogil:
        cdef double v = sqrt(x)
        return 0.5 * self.f._derivative_div_x(v) / x

    def to_dict(self):
        return { 'name':'compsqrt',
                'args': (self.f.to_dict(), self.g.to_dict() )
               }

cdef class ZeroOnPositive(Func):
    #
    def __init__(self, Func f):
        self.f = f
    #
    cdef double _evaluate(self, const double x) nogil:
        if x > 0:
            return 0
        else:
            return self.f._evaluate(x)
    #
    cdef double _derivative(self, const double x) nogil:
        if x > 0:
            return 0
        else:
            return self.f._derivative(x)
    #
    cdef double _derivative2(self, const double x) nogil:
        if x > 0:
            return 0
        else:
            return self.f._derivative2(x)
    #
    cdef double _derivative_div_x(self, const double x) nogil:
        if x > 0:
            return 0
        else:
            return self.f._derivative_div_x(x)

cdef class PlusId(Func):
    #
    cdef double _evaluate(self, const double x) nogil:
        if x <= 0:
            return 0
        else:
            return x
    #
    cdef double _derivative(self, const double x) nogil:
        if x <= 0:
            return 0
        else:
            return 1.
    #
    cdef double _derivative2(self, const double x) nogil:
        return 0
    #
    cdef double _derivative_div_x(self, const double x) nogil:
        if x <= 0:
            return 0
        else:
            return 1./x

cdef class FuncExp(Func):
    #
    def __init__ (self, Func f):
        self.f = f
    #
    cdef double _evaluate(self, const double x) nogil:
        return self.f._evaluate(exp(x))
    #
    cdef double _derivative(self, const double x) nogil:
        cdef double y = exp(x)
        return self.f._derivative(y) * y
    #
    cdef double _derivative2(self, const double x) nogil:
        cdef double y = exp(x)
        return (self.f._derivative(y) + self.f._derivative2(y) * y) * y

cdef class Id(Func):
    #
    cdef double _evaluate(self, const double x) nogil:
        return x
    #
    cdef double _derivative(self, const double x) nogil:
        return 1
    #
    cdef double _derivative2(self, const double x) nogil:
        return 0
    #
    def _repr_latex_(self):
        return '$\mathrm{id}(x)=x$'

def quantile_func(alpha, func):
    if type(func) is Sqrt:
        return Quantile_Sqrt(alpha, func.eps)
    else:
        return QuantileFunc(alpha, func)

cdef class QuantileFunc(Func):
    #
    def __init__(self, alpha, Func func):
        self.alpha = alpha
        self.f = func
    #
    cdef double _evaluate(self, const double x) nogil:
        if x > 0:
            return self.alpha * self.f._evaluate(x)
        elif x < 0:
            return (1-self.alpha) * self.f._evaluate(x)
        else:
            return 0.5 * self.f._evaluate(0)
    #
    cdef double _derivative(self, const double x) nogil:
        if x > 0:
            return self.alpha * self.f._derivative(x)
        elif x < 0:
            return (1-self.alpha) * self.f._derivative(x)
        else:
            return 0.5 * self.f._derivative(0)
    #
    cdef double _derivative2(self, const double x) nogil:
        if x > 0:
            return self.alpha * self.f._derivative2(x)
        elif x < 0:
            return (1-self.alpha) * self.f._derivative2(x)
        else:
            return 0.5 * self.f._derivative2(0)
    #
    cdef double _derivative_div_x(self, const double x) nogil:
        if x > 0:
            return self.alpha * self.f._derivative_div_x(x)
        elif x < 0:
            return (1-self.alpha) * self.f._derivative_div_x(x)
        else:
            return 0.5 * self.f._derivative_div_x(0)
    #
    def _repr_latex_(self):
        return '$\mathrm{id}(x)=x$'

    def to_dict(self):
        return { 'name':'quantile_func',
                'args': (self.alpha, self.f.to_dict() )
               }


cdef class Neg(Func):
    #
    cdef double _evaluate(self, const double x) nogil:
        return -x
    #
    cdef double _derivative(self, const double x) nogil:
        return -1
    #
    cdef double _derivative2(self, const double x) nogil:
        return 0
    #
    def _repr_latex_(self):
        return '$\mathrm{id}(x)=-x$'

cdef class ModSigmoidal(Func):
    #
    def __init__(self, a=1):
        self.label = u'σ'
        self.a = a
    #
    cdef double _evaluate(self, const double x) nogil:
        return x / (self.a + fabs(x))
    #
    cdef double _derivative(self, const double x) nogil:
        cdef double v = (self.a + fabs(x))
        return self.a / (v*v)
    #
    cdef double _derivative2(self, const double x) nogil:
        cdef double v = (self.a + fabs(x))
        if x > 0:
            return -2.0 * self.a / v*v*v
        elif x < 0:
            return 2.0 * self.a / v*v*v
        else:
            return 0
    #
    def _repr_latex_(self):
        return '$%s(x, a)=\dfrac{x}{a+|x|}$' % self.label

cdef class Sigmoidal(Func):
    #
    def __init__(self, p=1):
        self.label = u'σ'
        self.p = p
    #
    @cython.cdivision(True)
    cdef double _evaluate(self, const double x) nogil:
        cdef double p2 = 2 * self.p
        return (1.0 - exp(-p2 * x)) / (1.0 + exp(-p2 * x))
    #
    @cython.cdivision(True)
    cdef double _derivative(self, const double x) nogil:
        cdef double p2 = 2 * self.p
        cdef double v = exp(-p2 * x)
        return 2 * p2 * v / ((1 + v) * (1 + v))
    #
    @cython.cdivision(True)
    cdef double _derivative2(self, const double x) nogil:
        cdef double p = self.p
        cdef double p2 = 2 * self.p
        cdef double v = (1.0 - exp(-p2 * x)) / (1.0 + exp(-p2 * x))
        return 2 * p * p * (v*v - 1) * v
    #
    def _repr_latex_(self):
        return '$%s(x, p)=\dfrac{1}{1+e^{-px}}$' % self.label

    def to_dict(self):
        return { 'name':'sigmoidal',
                 'args': (self.p,) }

cdef class Arctang(Func):
    #
    def __init__(self, a=1):
        self.label = u'σ'
        self.a = a
    #
    @cython.cdivision(True)
    cdef double _evaluate(self, const double x) nogil:
        return atan(x/self.a)
    #
    @cython.cdivision(True)
    cdef double _derivative(self, const double x) nogil:
        cdef double v = x/self.a
        return 1 / (self.a * (1 + v*v))
    #
    @cython.cdivision(True)
    cdef double _derivative2(self, const double x) nogil:
        cdef double v = x /self.a
        cdef double a2 = self.a * self.a
        cdef double u = 1 + v*v
        return -2*v / (a2 * u*u)
    #
    def _repr_latex_(self):
        return '$%s(x, p)=\dfrac{1}{1+e^{-px}}$' % self.label

    def to_dict(self):
        return { 'name':'arctg',
                 'args': (self.a,) }

cdef class SoftPlus(Func):
    #
    def __init__(self, a=1):
        self.label = u'softplus'
        self.a = a
        if a == 1:
            self.log_a = 0
        else:
            self.log_a = log(a)
    #
    cdef double _evaluate(self, const double x) nogil:
        return log(self.a + exp(x)) - self.log_a
    #
    @cython.cdivision(True)
    cdef double _derivative(self, const double x) nogil:
        cdef double v = exp(x)
        return v / (self.a + v)
    #
    @cython.cdivision(True)
    cdef double _derivative2(self, const double x) nogil:
        cdef double v1 = exp(x)
        cdef double v2 = self.a + v1
        return self.a * v1 / v2*v2
    #
    def _repr_latex_(self):
        return '$%s(x, a)=\ln(a+e^x)$' % self.label

    def to_dict(self):
        return { 'name':'softplus',
                 'args': (self.a,) }

cdef class Threshold(Func):
    #
    def __init__(self, theta=0):
        self.label = u'H'
        self.theta = theta
    #
    cdef double _evaluate(self, const double x) nogil:
        if x >= self.theta:
            return 1
        else:
            return 0
    #
    cdef double _derivative(self, const double x) nogil:
        if x == self.theta:
            return c_inf
        else:
            return 0
    #
    cdef double _derivative2(self, const double x) nogil:
        return c_nan
    #
    def _repr_latex_(self):
        return '$%s(x, \theta)=\cases{1&x\geq\theta\\0&x<0}$' % self.label

    def to_dict(self):
        return { 'name':'threshold',
                 'args': (self.theta,) }

cdef class Sign(Func):
    #
    def __init__(self, theta=0):
        self.label = u'sign'
        self.theta = theta
    #
    cdef double _evaluate(self, const double x) nogil:
        if x > self.theta:
            return 1
        elif x < self.theta:
            return -1
        else:
            return 0
    #
    cdef double _derivative(self, const double x) nogil:
        if x == self.theta:
            return c_inf
        else:
            return 0
    #
    cdef double _derivative2(self, const double x) nogil:
        return c_nan
    #
    def _repr_latex_(self):
        return '$%s(x, \theta)=\cases{1&x\geq\theta\\0&x<0}$' % self.label

    def to_dict(self):
        return { 'name':'sign',
                 'args': (self.theta,) }

cdef class Quantile(Func):
    #
    def __init__(self, alpha=0.5):
        self.alpha = alpha
    #
    cdef double _evaluate(self, const double x) nogil:
        if x < 0:
            return (self.alpha - 1) * x
        elif x > 0:
            return self.alpha * x
        else:
            return 0
    #
    cdef double _derivative(self, const double x) nogil:
        if x < 0:
            return self.alpha - 1.0
        elif x > 0:
            return self.alpha
        else:
            return 0
    #
    cdef double _derivative2(self, const double x) nogil:
        if x == 0:
            return c_inf
        else:
            return 0
    #
    def _repr_latex_(self):
        return r"$ρ(x)=(\alpha - [x < 0])x$"

    def to_dict(self):
        return { 'name':'quantile',
                 'args': (self.alpha,) }

# cdef class Expectile(Func):
#     #
#     def __init__(self, alpha=0.5):
#         self.alpha = alpha
#     #
#     cdef double _evaluate(self, const double x) nogil:
#         if x < 0:
#             return 0.5 * (1. - self.alpha) * x * x
#         elif x > 0:
#             return 0.5 * self.alpha * x * x
#         else:
#             return 0
#     #
#     cdef double _derivative(self, const double x) nogil:
#         if x < 0:
#             return (1.0 - self.alpha) * x
#         elif x > 0:
#             return self.alpha * x
#         else:
#             return 0
#     #
#     cdef double _derivative2(self, const double x) nogil:
#         if x < 0:
#             return (1.0 - self.alpha)
#         elif x > 0:
#             return self.alpha
#         else:
#             return 0.5
#     #
#     cdef double _derivative_div_x(self, const double x) nogil:
#         if x < 0:
#             return (1.0 - self.alpha)
#         elif x > 0:
#             return self.alpha
#         else:
#             return 0.5
#     #
#     def _repr_latex_(self):
#         return r"$ρ(x)=(\alpha - [x < 0])x|x|$"

#     def to_dict(self):
#         return { 'name':'expectile',
#                  'args': (self.alpha,) }

cdef class Power(Func):
    #
    def __init__(self, p=2.0, alpha=0):
        self.p = p
        self.alpha = alpha
        self.alpha_p = pow(self.alpha, self.p)
    #
    cdef double _evaluate(self, const double x) nogil:
        return pow(fabs(x) + self.alpha, self.p) / self.p
    #
    cdef double _derivative(self, const double x) nogil:
        cdef double val
        val = pow(fabs(x) + self.alpha, self.p-1)
        if x < 0:
            val = -val
        return val
    #
    cdef double _derivative2(self, const double x) nogil:
        return (self.p-1) * pow(fabs(x) + self.alpha, self.p-2)
    #
    cdef double _derivative_div_x(self, const double x) nogil:
        return pow(fabs(x) + self.alpha, self.p-2)
    #
    def _repr_latex_(self):
        return r"$ρ(x)=\frac{1}{p}(|x|+\alpha)^p$"

    def to_dict(self):
        return { 'name':'power',
                 'args': (self.p, self.alpha,) }

cdef class Square(Func):
    #
    cdef double _evaluate(self, const double x) nogil:
        return 0.5 * x * x
    #
    cdef double _derivative(self, const double x) nogil:
        return x
    #
    cdef double _derivative_div_x(self, const double x) nogil:
        return 1
    #
    cdef double _derivative2(self, const double x) nogil:
        return 1
    #
    def _repr_latex_(self):
        return r"$ρ(x)=0.5x^2$"

    def to_dict(self):
        return { 'name':'square',
                 'args': () }

cdef class SquareSigned(Func):
    #
    cdef double _evaluate(self, const double x) nogil:
        cdef double val = 0.5 * x * x
        if x >= 0:
            return val
        else:
            return -val
    #
    cdef double _derivative(self, const double x) nogil:
        return fabs(x)
    #
    cdef double _derivative2(self, const double x) nogil:
        if x > 0:
            return 1.0
        elif x < 0:
            return -1.0
        else:
            return 0.
    #
    def _repr_latex_(self):
        return r"$ρ(x)=0.5x^2$"

cdef class Absolute(Func):
    #
    cdef double _evaluate(self, const double x) nogil:
        return fabs(x)
    #
    cdef double _derivative(self, const double x) nogil:
        if x > 0:
            return 1
        elif x < 0:
            return -1
        else:
            0
    #
    cdef double _derivative2(self, const double x) nogil:
        if x == 0:
            return c_inf
        else:
            return 0
    #
    def _repr_latex_(self):
        return r"$ρ(x)=|x|$"

    def to_dict(self):
        return { 'name':'absolute',
                 'args': () }

cdef class Quantile_AlphaLog(Func):
    #
    def __init__(self, alpha=1.0, q=0.5):
        assert alpha > 0
        self.alpha = alpha
        self.q = q
        if alpha == 0:
            self.alpha2 = 0.
        else:
            self.alpha2 = self.alpha*log(self.alpha)
    #
    cdef double _evaluate(self, const double x) nogil:
        cdef double val
        if x < 0:
            val = -x - self.alpha*log(self.alpha - x) + self.alpha2
            return (1.0-self.q) * val
        elif x > 0:
            val = x - self.alpha*log(self.alpha + x) + self.alpha2
            return self.q * val
        else:
            return 0
    #
    @cython.cdivision(True)
    cdef double _derivative(self, const double x) nogil:
        cdef double val
        if x < 0:
            val = x / (self.alpha - x)
            return (1-self.q) * val
        elif x > 0:
            val = x / (self.alpha + x)
            return self.q * val
        else:
            return self.q - 0.5
    #
    @cython.cdivision(True)
    cdef double _derivative2(self, const double x) nogil:
        cdef double v
        if x < 0:
            v = self.alpha - x
            return (1-self.q)*self.alpha / (v*v)
        elif x > 0:
            v = self.alpha + x
            return self.q*self.alpha / (v*v)
        else:
            return 0.5 / self.alpha
    #
    @cython.cdivision(True)
    cdef double _derivative_div_x(self, const double x) nogil:
        cdef double val
        if x < 0:
            val = 1 / (self.alpha - x)
            return (1-self.q) * val
        elif x > 0:
            val = 1 / (self.alpha + x)
            return self.q * val
        else:
            return (self.q - 0.5) / self.alpha
    #
    def _repr_latex_(self):
        return r"$ρ_q(x)=\mathrm{sign}_q(x)(|x| - \alpha\ln(\alpha+|x|)+\alpha\ln\alpha)$"

    def to_dict(self):
        return { 'name':'quantile_alpha_log',
                 'args': (self.alpha, self.q) }

cdef class Logistic(Func):

    def __init__(self, p=1.0):
        assert p > 0
        self.p = p

    @cython.cdivision(True)
    cdef double _evaluate(self, const double x) nogil:
        return log(1.0 + exp(fabs(x) / self.p)) - log(2)

    @cython.cdivision(True)
    cdef double _derivative(self, const double x) nogil:
        cdef double v = exp(fabs(x) / self.p)
        if x > 0:
            return v / (1.0 + v) / self.p
        elif x < 0:
            return -v / (1.0 + v) / self.p
        else:
            return 0

    @cython.cdivision(True)
    cdef double _derivative2(self, const double x) nogil:
        cdef double v = exp(fabs(x) / self.p)
        if x > 0:
            return 1 / ((1 + v) * (1+v)) / self.p
        elif x < 0:
            return -1 / ((1 + v) * (1+v)) / self.p
        else:
            return 0

    def _repr_latex_(self):
        return r"$\ell(y,\tilde y)=\log(1+e^{|y-\tilde y|/p})$"

    def to_dict(self):
        return { 'name':'logistic',
                 'args': (self.p,) }

cdef class Hinge(Func):
    #
    def __init__(self, C=1.0):
        self.C = C
    #
    cdef double _evaluate(self, const double x) nogil:
        if x >= self.C:
            return 0
        else:
            return self.C - x
    #
    cdef double _derivative(self, const double x) nogil:
        if x >= self.C:
            return 0
        else:
            return -1
    #
    cdef double _derivative_div_x(self, const double x) nogil:
        if x >= self.C:
            return 0
        else:
            return -1 / (self.C - x)
    #
    cdef double _derivative2(self, const double x) nogil:
        if x >= self.C:
            return -c_inf
        else:
            return 0
    #
    cdef double _value(self, const double x) nogil:
        return self.C - x
    #
    def _repr_latex_(self):
        return r"$ρ(x)=(c-x)_{+}$"

    def to_dict(self):
        return { 'name':'hinge',
                 'args': (self.C,) }

cdef class HSquare(Func):
    #
    def __init__(self, C=1.0):
        self.C = C
    #
    cdef double _evaluate(self, const double x) nogil:
        cdef double v = self.C - x
        if v < 0:
            v = 0
        return 0.5 * v * v
    #
    cdef double _derivative(self, const double x) nogil:
        cdef double v = self.C - x
        if v < 0:
            v = 0
        return -v
    #
    cdef double _derivative_div_x(self, const double x) nogil:
        cdef double v = self.C - x
        if v < 0:
            return 0
        else:
            return -1
    #
    cdef double _derivative2(self, const double x) nogil:
        cdef double v = self.C - x
        if v < 0:
            return 0
        else:
            return 1
    #
    cdef double _value(self, const double x) nogil:
        return self.C - x
    #
    def _repr_latex_(self):
        return r"$ρ(x)=(c-x)^2$"

    def to_dict(self):
        return { 'name':'hinge',
                 'args': (self.C,) }

cdef class HingeSqrt(Func):
    #
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.alpha2 = alpha*alpha
    #
    cdef double _evaluate(self, const double x) nogil:
        return -x + sqrt(self.alpha2 + x*x)
    #
    @cython.cdivision(True)
    cdef double _derivative(self, const double x) nogil:
        return -1 + x/sqrt(self.alpha2 + x*x)
    #
    @cython.cdivision(True)
    cdef double _derivative2(self, const double x) nogil:
        return self.alpha2/sqrt(self.alpha2 + x*x)
    #
    def _repr_latex_(self):
        return r"$ρ(x)=-x + \sqrt{c^2+x^2}$"

    def to_dict(self):
        return { 'name':'hinge_sqrt',
                 'args': (self.alpha,) }

cdef class HingeSqrtPlus(Func):
    #
    def __init__(self, alpha=1.0):
        self.alpha = alpha
        self.alpha2 = alpha*alpha
    #
    cdef double _evaluate(self, const double x) nogil:
        return x + sqrt(self.alpha2 + x*x)
    #
    @cython.cdivision(True)
    cdef double _derivative(self, const double x) nogil:
        return 1 + x/sqrt(self.alpha2 + x*x)
    #
    @cython.cdivision(True)
    cdef double _derivative2(self, const double x) nogil:
        return self.alpha2/sqrt(self.alpha2 + x*x)
    #
    def _repr_latex_(self):
        return r"$ρ(x)=-x + \sqrt{c^2+x^2}$"

    def to_dict(self):
        return { 'name':'hinge_sqrt',
                 'args': (self.alpha,) }

cdef class Huber(Func):

    def __init__(self, C=1.345):
        self.C = C

    @cython.cdivision(True)
    cdef double _evaluate(self, const double x) nogil:
        cdef double x_abs = fabs(x)

        if x_abs > self.C:
            return x_abs - 0.5 * self.C
        else:
            return 0.5 * x*x / self.C

    @cython.cdivision(True)
    cdef double _derivative(self, const double x) nogil:
        cdef double x_abs = fabs(x)

        if x > self.C:
            return 1.
        elif x < -self.C:
            return -1.
        else:
            return x / self.C
    #
    @cython.cdivision(True)
    cdef double _derivative_div_x(self, const double x) nogil:
        cdef double x_abs = fabs(x)

        if x_abs > self.C:
            return 1. / x_abs
        else:
            return 1. / self.C

    def _repr_latex_(self):
        return r"""$\displaystyle
            \rho(x)=\cases{
                0.5x^2/C, & |x|<C\\
                |x|-0.5C, & |x| \geq C
            }
        $"""

    def to_dict(self):
        return { 'name':'huber',
                 'args': (self.C,) }

cdef class TM(Func):
    #
    def __init__(self, a=1):
        self.a = a
    #
    cdef double _evaluate(self, const double x) nogil:
        if x <= 0:
            return x*x/2
        else:
            return self.a * x
    #
    cdef double _derivative(self, const double x) nogil:
        if x <= 0:
            return x
        else:
            return self.a
    #
    cdef double _derivative2(self, const double x) nogil:
        if x <= 0:
            return 1
        else:
            return 0
    #
    cdef double _derivative_div_x(self, const double x) nogil:
        if x <= 0:
            return 1
        else:
            return self.a / x
    #
    def _repr_latex_(self):
        return r"""$\displaystyle
            \rho(x)=\cases{
                frac{1}{2}x^2, & x<0\\
                ax, & x\geq 0
            }
        $"""

cdef class LogSquare(Func):

    def __init__(self, a=1.0):
        self.a = a
        self.a2 = a * a

    cdef double _evaluate(self, const double x) nogil:
        return log(self.a2 + x*x)

    @cython.cdivision(True)
    cdef double _derivative(self, const double x) nogil:
        return 2 * x / (self.a2 + x*x)

    @cython.cdivision(True)
    cdef double _derivative2(self, const double x) nogil:
        cdef double x2 = x*x
        cdef double xa = self.a + x2
        return 2 * (self.a2 - x2) / xa * xa

    def _repr_latex_(self):
        return r'$\ln(a^2 + x^2)$'

    def to_dict(self):
        return { 'name':'log_square',
                 'args': (self.a,) }

cdef class Tukey(Func):

    def __init__(self, C=4.685):
        self.C = C
        self.C2 = C * C / 6.

    cdef double _evaluate(self, const double x) nogil:
        cdef double v = x/self.C
        cdef double v2 = v*v
        cdef double v3 = 1 - v2

        if v <= self.C:
            return self.C2 * (1 - v3*v3*v3)
        else:
            return self.C2

    cdef double _derivative(self, const double x) nogil:
        cdef double v = x/self.C
        cdef double v3 = 1 - v*v

        if v <= self.C:
            return x * v3*v3
        else:
            return 0

    cdef double _derivative2(self, const double x) nogil:
        cdef double v = x/self.C
        cdef double v3 = 1 - v*v

        if v <= self.C:
            return v3*v3 - 4*v3*v*v
        else:
            return 0

    def _repr_latex_(self):
        return r"""$\displaystyle
            \pho(x)=\cases{
                (C^2/6) (1-[1-(x/C)^2]^3), & |x|\leq C\\
                C^2/6, & |x| > C
            }
        $"""

    def to_dict(self):
        return { 'name':'tukey',
                 'args': (self.C,) }

cdef class SoftAbs(Func):
    #
    def __init__(self, eps=1.0):
        self.eps = eps
    #
    @cython.cdivision(True)
    cdef double _evaluate(self, const double x) nogil:
        return x * x / (self.eps + fabs(x))
    #
    @cython.cdivision(True)
    cdef double _derivative(self, const double x) nogil:
        cdef double v = self.eps + fabs(x)
        return x * (self.eps + v) / (v * v)
    #
    @cython.cdivision(True)
    cdef double _derivative2(self, const double x) nogil:
        cdef double eps = self.eps
        cdef double v = eps + fabs(x)
        return 2 * eps * eps / (v * v * v)
    #
    @cython.cdivision(True)
    cdef double _derivative_div_x(self, const double x) nogil:
        cdef double v = self.eps + fabs(x)
        return (self.eps + v) / (v * v)
    #
    def _repr_latex_(self):
        return r"$p(x)=\frac{x^2}{\varepsilon+|x|}$"

    def to_dict(self):
        return { 'name':'softabs',
                 'args': (self.eps,) }


cdef class Sqrt(Func):
    #
    def __init__(self, eps=1.0):
        self.eps = eps
        self.eps2 = eps*eps
    #
    @cython.cdivision(True)
    @cython.final
    cdef double _evaluate(self, const double x) nogil:
        return sqrt(self.eps2 + x*x) - self.eps
    #
    @cython.cdivision(True)
    @cython.final
    cdef void _evaluate_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        cdef double v, eps = self.eps, eps2 = self.eps2

        for i in prange(n, nogil=True, schedule='static', num_threads=num_procs):
            v = x[i]
            y[i] = sqrt(eps2 + v*v) - eps
    #
    @cython.cdivision(True)
    @cython.final
    cdef double _derivative(self, const double x) nogil:
        cdef double v = self.eps2 + x*x
        return x / sqrt(v)
    #
    @cython.cdivision(True)
    @cython.final
    cdef void _derivative_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        cdef double v, eps = self.eps, eps2 = self.eps2

        for i in prange(n, nogil=True, schedule='static', num_threads=num_procs):
            v = x[i]
            y[i] = v / sqrt(eps2 + v*v)
    #
    @cython.cdivision(True)
    @cython.final
    cdef double _derivative2(self, const double x) nogil:
        cdef double v = self.eps2 + x*x
        return self.eps2 / (v * sqrt(v))
    #
    @cython.cdivision(True)
    @cython.final
    cdef void _derivative2_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        cdef double v, v2, eps = self.eps, eps2 = self.eps2

        for i in prange(n, nogil=True, schedule='static', num_threads=num_procs):
            v = x[i]
            v2 = eps2 + v*v
            y[i] = eps2 / (v2 * sqrt(v2))
    #
    @cython.cdivision(True)
    @cython.final
    cdef double _derivative_div_x(self, const double x) nogil:
        return 1. / sqrt(self.eps2 + x*x)
    #
    @cython.cdivision(True)
    @cython.final
    cdef void _derivative_div_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        cdef double v, v2, eps = self.eps, eps2 = self.eps2

        for i in prange(n, nogil=True, schedule='static', num_threads=num_procs):
            v = x[i]
            y[i] = 1. / sqrt(eps2 + v*v)
    #
    def _repr_latex_(self):
        return r"$p(x)=\sqrt{\varepsilon^2+x^2}$"

    def to_dict(self):
        return { 'name':'sqrt',
                 'args': (self.eps) }

cdef class Quantile_Sqrt(Func):
    #
    def __init__(self, alpha=0.5, eps=1.0):
        self.alpha = alpha
        self.eps = eps
        self.eps2 = eps*eps
    #
    cdef double _evaluate(self, const double x) nogil:
        cdef double v = self.eps2 + x*x
        if x >= 0:
            return (sqrt(v) - self.eps) * self.alpha
        else:
            return (sqrt(v) - self.eps) * (1-self.alpha)
    #
    @cython.cdivision(True)
    cdef double _derivative(self, const double x) nogil:
        cdef double v = self.eps2 + x*x
        if x >= 0:
            return self.alpha * x / sqrt(v)
        else:
            return (1.-self.alpha) * x / sqrt(v)
    #
    @cython.cdivision(True)
    cdef double _derivative2(self, const double x) nogil:
        cdef double v = self.eps2 + x*x
        if x >= 0:
            return self.alpha * self.eps2 / (v * sqrt(v))
        else:
            return (1.-self.alpha) * self.eps2 / (v * sqrt(v))
    #
    @cython.cdivision(True)
    cdef double _derivative_div_x(self, const double x) nogil:
        cdef double v = self.eps2 + x*x
        if x >= 0:
            return self.alpha / sqrt(v)
        else:
            return (1.-self.alpha) / sqrt(v)
    #
    @cython.cdivision(True)
    cdef void _evaluate_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        cdef double u, v
        for i in range(n):
            v = x[i]
            u = self.eps2 + v*v
            if v >= 0:
                y[i] = (sqrt(u) - self.eps) * self.alpha
            else:
                y[i] = (sqrt(u) - self.eps) * (1-self.alpha)
    #
    @cython.cdivision(True)
    cdef void _derivative_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        cdef double u, v
        for i in range(n):
            v = x[i]
            u = self.eps2 + v*v
            if v >= 0:
                y[i] = self.alpha * v / sqrt(u)
            else:
                y[i] = (1.-self.alpha) * v / sqrt(u)
    #
    @cython.cdivision(True)
    cdef void _derivative2_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        cdef double u, v
        for i in range(n):
            v = x[i]
            u = self.eps2 + v*v
            if v >= 0:
                y[i] = self.alpha * self.eps2 / (u * sqrt(u))
            else:
                y[i] = (1.-self.alpha) * self.eps2 / (u * sqrt(u))
    #
    @cython.cdivision(True)
    cdef void _derivative_div_array(self, const double *x, double *y, const Py_ssize_t n) nogil:
        cdef Py_ssize_t i
        cdef double u, v
        for i in range(n):
            v = x[i]
            u = self.eps2 + v*v
            if v >= 0:
                y[i] = self.alpha / sqrt(u)
            else:
                y[i] = (1.-self.alpha) / sqrt(u)
    #
    def _repr_latex_(self):
        return r"$p(x)=(\sqrt{\varepsilon^2+x^2}-\varepsilon)_\alpha$"

    def to_dict(self):
        return { 'name':'quantile_sqrt',
                 'args': (self.alpha, self.eps) }


cdef class Expectile(Func):
    #
    def __init__(self, alpha=1.0):
        self.alpha = alpha
    #
    cdef double _evaluate(self, const double x) nogil:
        return exp(x/self.alpha)
    #
    cdef double _derivative(self, const double x) nogil:
        return exp(x/self.alpha)/self.alpha
    #
    cdef double _derivative2(self, const double x) nogil:
        return exp(x/self.alpha)/self.alpha/self.alpha
    #
    def _repr_latex_(self):
        return r"$\rho(x)=\exp{x/\alpha}$"

    def to_dict(self):
        return { 'name':'exp',
                 'args': (self.alpha,) }

cdef class Log(Func):
    #
    def __init__(self, alpha=1.0):
        self.alpha = alpha
    #
    cdef double _evaluate(self, const double x) nogil:
        return log(self.alpha+x)
    #
    cdef double _derivative(self, const double x) nogil:
        return 1 / (self.alpha+x)
    #
    cdef double _derivative2(self, const double x) nogil:
        cdef double x2 = self.alpha+x
        return -1 / (x2*x2)
    #
    def _repr_latex_(self):
        return r"$\rho(x)=\ln{\alpha+x}$"

    def to_dict(self):
        return { 'name':'log',
                 'args': (self.alpha,) }

cdef class ParameterizedFunc:
    #
    def __call__(self, x, u):
        return self._evaluate(x, u)
    #
    cdef double _evaluate(self, const double x, const double u) nogil:
        return 0
    #
    cdef double _derivative(self, const double x, const double u) nogil:
        return 0
    #
    cdef double derivative_u(self, const double x, const double u) nogil:
        return 0

cdef class WinsorizedFunc(ParameterizedFunc):
    #
    cdef double _evaluate(self, const double x, const double u) nogil:
        if x > u:
            return u
        elif x < -u:
            return -u
        else:
            return x
    #
    cdef double _derivative(self, const double x, const double u) nogil:
        if x > u or x < -u:
            return 0
        else:
            return 1
    #
    cdef double derivative_u(self, const double x, const double u) nogil:
        if x > u or x < -u:
            return 1
        else:
            return 0

    def to_dict(self):
        return { 'name':'winsorized',
                 'args': () }


cdef class SoftMinFunc(ParameterizedFunc):
    #
    def __init__(self, a = 1):
        self.a = a
    #
    @cython.cdivision(True)
    cdef double _evaluate(self, const double x, const double u) nogil:
        if u < x:
            return u - log(1. + exp(-self.a*(x-u))) / self.a
        else:
            return x - log(1. + exp(-self.a*(u-x))) / self.a
    #
    @cython.cdivision(True)
    cdef double _derivative(self, const double x, const double u) nogil:
        return 1. / (1. + exp(-self.a*(u-x)))
    #
    @cython.cdivision(True)
    cdef double derivative_u(self, const double x, const double u) nogil:
        return 1. / (1. + exp(-self.a*(x-u)))

    def to_dict(self):
        return { 'name':'softmin',
                 'args': (self.a,) }

cdef class  WinsorizedSmoothFunc(ParameterizedFunc):
    #
    def __init__(self, Func f):
        self.f = f
    #
    cdef double _evaluate(self, const double x, const double u) nogil:
        return 0.5 * (x + u - self.f._evaluate(x - u))
    #
    cdef double _derivative(self, const double x, const double u) nogil:
        return 0.5 * (1. - self.f._derivative(x - u))
    #
    cdef double derivative_u(self, const double x, const double u) nogil:
        return 0.5 * (1. + self.f._derivative(x - u))

    def to_dict(self):
        return { 'name':'winsorized_soft',
                 'args': (self.f.to_dict(),) }

cdef class KMinSquare(Func):
    #
    def __init__(self, c):
        self.c = np.asarray(c, 'd')
        self.n_dim = c.shape[0]
        self.j_min = 0
    #
    cdef double _evaluate(self, const double x) nogil:
        cdef int j, j_min, n_dim = self.n_dim
        cdef double d, d_min

        d_min = self.c[0]
        j_min = 0
        j = 1
        while j < n_dim:
            d = self.c[j]
            if fabs(x - d) < d_min:
                j_min = j
                d_min = d
            j += 1
        self.j_min = j_min
        return 0.5 * (x - d_min) * (x - d_min)
    #
    cdef double _derivative(self, const double x) nogil:
        return x - self.c[self.j_min]
    #
    cdef double _derivative2(self, const double x) nogil:
        return 1
    #
    def _repr_latex_(self):
        return r"$\rho(x)=\min_{j=1,\dots,q} (x-c_j)^2/2$"

    def to_dict(self):
        return { 'name':'kmin_square',
                 'args': (self.c.tolist(),) }


register_func(Comp, 'comp')
register_func(QuantileFunc, 'quantile_func')
register_func(Sigmoidal, 'sigmoidal')
register_func(KMinSquare, 'kmin_square')
register_func(WinsorizedSmoothFunc, 'winsorized_smooth')
register_func(SoftMinFunc, 'softmin')
register_func(WinsorizedFunc, 'winsorized')
register_func(Log, 'log')
register_func(Exp, 'exp')
register_func(Quantile_Sqrt, 'quantile_sqrt')
register_func(Sqrt, 'sqrt')
register_func(SoftAbs, 'softabs')
register_func(Tukey, 'tukey')
register_func(LogSquare, 'log_square')
register_func(Huber, 'huber')
register_func(HingeSqrt, 'hinge_sqrt')
register_func(Hinge, 'hinge')
register_func(Logistic, 'logistic')
register_func(Quantile_AlphaLog, 'quantile_alpha_log')
register_func(Absolute, 'absolute')
register_func(Square, 'square')
register_func(Power, 'power')
register_func(Expectile, 'expectile')
register_func(Quantile, 'quantile')
register_func(Sign, 'sign')
register_func(Threshold, 'threshold')
register_func(SoftPlus, 'softplus')
register_func(Arctang, 'arctg')
