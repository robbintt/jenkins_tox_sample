
def func(x):
    return x+1

def test_answer():
    assert func(4) == 5

def test_bad_answer():
    assert func(3) != 5
