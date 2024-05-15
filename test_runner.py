# import pytest

# def test_run():
#     assert run('doit.py', {"num_rows": 500, "num_cols": 20}) == None
#     assert run('x1.py', {"a": 5, "b": 0}) == None
#     assert 5 - 3 == 2

# if __name__ == "__main__":
#     pytest.main()

import runner

# def test_run():
#     r = runner.run('doit.py', {"num_rows": 500, "num_cols": 20})

#     print(r.describe())

def test_doit():
    r = runner.run('doit.py', {"num_rows": 500, "num_cols": 20})
    print(r.describe())
    assert r['Row Sum'].sum() == sum([r[f'Column{i}'].sum() for i in range(20)])