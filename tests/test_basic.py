import pytest
import basic

@pytest.mark.parametrize("x",
        [1, 2, 3, 4 ,5 ])
        
def test_square(x):
    basic.square(x) == x ** 2
