"""
Test function module
"""
import numpy as np
import pytest
from regmod.function import fun_dict


def ad_dfun(fun, x, eps=1e-16):
    return fun(x + eps*1j).imag/eps


@pytest.mark.parametrize("x", np.random.randn(3))
def test_identity(x):
    fun = fun_dict["identity"]
    assert np.isclose(fun.dfun(x), ad_dfun(fun.fun, x))
    assert np.isclose(fun.d2fun(x), ad_dfun(fun.dfun, x))


@pytest.mark.parametrize("x", np.random.randn(3))
def test_quad(x):
    fun = fun_dict["quad"]
    assert np.isclose(fun.dfun(x), ad_dfun(fun.fun, x))
    assert np.isclose(fun.d2fun(x), ad_dfun(fun.dfun, x))


@pytest.mark.parametrize("x", np.random.randn(3))
def test_exp(x):
    fun = fun_dict["exp"]
    assert np.isclose(fun.dfun(x), ad_dfun(fun.fun, x))
    assert np.isclose(fun.d2fun(x), ad_dfun(fun.dfun, x))


@pytest.mark.parametrize("x", np.random.randn(3))
def test_expit(x):
    fun = fun_dict["expit"]
    assert np.isclose(fun.dfun(x), ad_dfun(fun.fun, x))
    assert np.isclose(fun.d2fun(x), ad_dfun(fun.dfun, x))


@pytest.mark.parametrize("x", np.random.rand(3) + 0.1)
def test_log(x):
    fun = fun_dict["log"]
    assert np.isclose(fun.dfun(x), ad_dfun(fun.fun, x))
    assert np.isclose(fun.d2fun(x), ad_dfun(fun.dfun, x))


@pytest.mark.parametrize("x", 0.8*np.random.rand(3) + 0.1)
def test_logit(x):
    fun = fun_dict["logit"]
    assert np.isclose(fun.dfun(x), ad_dfun(fun.fun, x))
    assert np.isclose(fun.d2fun(x), ad_dfun(fun.dfun, x))
