import numpy as np

import suvat

def test_find_displacement():
    """
    This tests the `find_displacemet` function in turn for each SUVAT variable being unknown (each situation) to 
    ensure we get expected values.
    """
    displacement1 = suvat.find_displacement(u = None, v = 4, a = 5, t = 10)
    expected_displacement1 = -210
    assert displacement1 == expected_displacement1, "Did not get expected value for displacement"
    displacement2 = suvat.find_displacement(u = 4, v = None, a = 10, t = 5)
    expected_displacement2 = 145
    assert displacement2 == expected_displacement2, "Did not get expected value for displacement"
    displacement3 = suvat.find_displacement(u = 3, v = 8, a = None, t = 8)
    expected_displacement3 = 44
    assert displacement3 == expected_displacement3, "Did not get expected value for displacement"
    displacement4 = suvat.find_displacement(u = 4, v = 6, a = 5, t = None)
    expected_displacement4 = 2
    assert displacement4 == expected_displacement4, "Did not get expected value for displacement"

def test_find_initial_velocity():
    """
    This test the `find_initial_velocity` function in turn for each SUVAT variable being unknown (each situation) to
    ensure we get expected values
    """
    initial_velocity1 = suvat.find_initial_velocity(s = None, v = 25, a = 6, t = 4)
    expected_initial_velocity1 = 1
    assert initial_velocity1 == expected_initial_velocity1, "Did not get expected value for initial velocity"
    initial_velocity2 = suvat.find_initial_velocity(s = 5, v = None, a = 8, t = 5)
    expected_initial_velocity2 = -19
    assert initial_velocity2 == expected_initial_velocity2, "Did not get expected value for initial velocity"





