import pytest
import inspect
import package3.package4.mod5


def test_hello():
    assert package3.package4.mod5.hello_mod5()
