""" TASK 2: Pytest Markers Practice

Create 2 custom markers:
@pytest.mark.smoke
@pytest.mark.regression
Write:
2 test cases for smoke
2 test cases for regression
Each test should:
Contain a simple assertion 
Run tests using:
Only smoke tests
Only regression tests """

import pytest
# writing two test cases for smoke using pytest.mark.smoke
@pytest.mark.smoke
def test_smoke1():
    l=['apple','banana','cherry','mango','orange']
    assert 'apple' in l

@pytest.mark.smoke
def test_smoke2():
    l=['apple','banana','cherry','mango','orange']
    assert 'pineapple' not in l

# writing two test cases for regression using pytest.mark.regression
@pytest.mark.regression
def test_regression1():
    l=['apple','banana','cherry','mango','orange']
    assert 'apple' in l

@pytest.mark.regression
def test_regression2():
    l=['apple','banana','cherry','mango','orange']
    assert 'pineapple' not in l

# run the test cases - only smoke tests
# pytest -vs Test_Task-2.py -m "smoke"
# run the test cases - only regression tests
# pytest -vs Test_Task-2.py -m "regression"
