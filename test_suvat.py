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
    This tests the `find_initial_velocity` function in turn for each SUVAT variable being unknown (each situation) to
    ensure we get expected values
    """
    initial_velocity1 = suvat.find_initial_velocity(s = None, v = 25, a = 6, t = 4)
    expected_initial_velocity1 = 1
    assert initial_velocity1 == expected_initial_velocity1, "Did not get expected value for initial velocity"
    initial_velocity2 = suvat.find_initial_velocity(s = 5, v = None, a = 8, t = 5)
    expected_initial_velocity2 = -19
    assert initial_velocity2 == expected_initial_velocity2, "Did not get expected value for initial velocity"
    initial_velocity3 = suvat.find_initial_velocity(s = 5, v = 2, a = None, t = 10)
    expected_initial_velocity3 = -1
    assert initial_velocity3 == expected_initial_velocity3, "Did not get expected value for initial velocity"
    initial_velocity4 = suvat.find_initial_velocity(s = 8, v = 8, a = 3, t = None)
    expected_initial_velocity4 = 4
    assert initial_velocity4 == expected_initial_velocity4, "Did not get expected value for initial velocity"

def test_find_final_velocity():
    """
    This tests the `find_final_velocity` function in turn for each SUVAT variable being unknown (each situation) to
    ensure we get expected values
    """
    final_velocity1 = suvat.find_final_velocity(s = None, u = 2, a = 6, t = 11)
    expected_final_velocity1 = 68
    assert final_velocity1 == expected_final_velocity1, "Did not get expected value for final velocity"
    final_velocity2 = suvat.find_final_velocity(s = 4, u = None, a = 5, t = 10)
    expected_final_velocity2 = 25.4
    assert final_velocity2 == expected_final_velocity2, "Did not get expected value for final velocity"
    final_velocity3 = suvat.find_final_velocity(s = 10, u = 3, a = None, t = 10)
    expected_final_velocity3 = -1
    assert final_velocity3 == expected_final_velocity3, "Did not get expected value for final velocity"
    final_velocity4 = suvat.find_final_velocity(s = 28, u = 5, a = 9, t = None)
    expected_final_velocity4 = 23
    assert final_velocity4 == expected_final_velocity4, "Did not get expected value for final velocity"
    
def test_find_acceleration():
    """
    This tests the `find_acceleration` function in turn for each SUVAT variable being unknown (each situation) to
    ensure we get expected values
    """
    acceleration1 = suvat.find_acceleration(s = None, u = 3, v = 10, t = 7)
    expected_acceleration1 = 1
    assert acceleration1 == expected_acceleration1, "Did not get expected value for acceleration"
    acceleration2 = suvat.find_acceleration(s = 35, u = None, v = 9, t = 5)
    expected_acceleration2 = 0.8
    assert acceleration2 == expected_acceleration2, "Did not get expected value for acceleration"
    acceleration3 = suvat.find_acceleration(s = 14, u = 6, v = None, t = 1)
    expected_acceleration3 = 16
    assert acceleration3 == expected_acceleration3, "Did not get expected value for acceleration"
    acceleration4 = suvat.find_acceleration(s = 6, u = 2, v = 8, t = None)
    expected_acceleration4 = 5
    assert acceleration4 == expected_acceleration4, "Did not get expected value for acceleration"

def test_find_time():
    """
    This tests the `find_time` function in turn for each SUVAT variable being unknown (each situation) to ensure
    we get expected values
    """
    time1 = suvat.find_time(s = None, u = 5, v = 20, a = 3)
    expected_time1 = 5
    assert time1 == expected_time1, "Did not get expected value for time"
    time2 = suvat.find_time(s = -135, u = None, v = 7.5, a = 10)
    expected_time2 = [6]
    assert time2 == expected_time2, "Did not get expected value for time"
    time3 = suvat.find_time(s=204, u=4, v=None, a=10)
    expected_time3 = 6
    assert time3 == expected_time3, "Did not get expected value for time"
    time4 = suvat.find_time(s = 10, u = 5, v = 15, a = None)
    expected_time4 = 1
    assert time4 == expected_time4, "Did not get expected value for time"

test_find_displacement()
test_find_initial_velocity()
test_find_final_velocity()
test_find_displacement()
test_find_time()