# SUVAT

Functionality to solve constant acceleration kinematic questions using SUVAT

## Tutorial

In this tutorial we will see how to use `suvat` to solve a kinematic problem of constant acceleration. For some more information on what SUVAT is used for and the derivation of their formulas we recommend: <https://studywell.com/kinematics/suvat-equations/#:~:text=The%20SUVAT%20Equations%20describe%20motion,U%202%20%2B%202%20A%20S>.

Consider the following problem:

A cyclist is travelling along a straight road. She accelerates at a constant rate from a velocity of $4 m/s$ to velocity of $7.5 m/s$ in $40 seconds$. Find:

1. The distance she travels in these 40 seconds
2. Her acceleration in these 40 seconds

First we import the relevant library:

```python
>>> import suvat
```

As we have the initial velocity, u, final velocity, v and time, t, we can find the displacement (in this case labelled distance as we don't need to account for positive and negative values), s, by using the `find_displacement` function. As we do not have a value for acceleration we will input "None" to account for the unknown:

```python
>>> distance = suvat.find_displacement(u=4,v=7.5,a=None,t=40)
```

We can then view the value of this distance, which solves part 1 of this problem:

```python
>>> distance
230
```

To solve part 2, we can use the same values found in the question to find the acceleration but use the `find_acceleration` function instead. Our only difference from before is we will have the displacement, s, set to None as we are only using the values found in the question.

Running the following will give us the acceleration:

```python
>>> acceleration = suvat.find_acceleration(s=None,u=4,v=7.5,t=40)
```

Once again we can now view the value of this acceleration, which solves part 2 of this problem:

```python
>>> acceleration
0.0875
```

## How to guides

In order to solve any SUVAT problem, we only need 3 values consisting of either the displacement, initial velocity, final velocity, acceleration or time, depending on what we are trying to calculate. 

We will always have 3 known values given in the question to input and one value we will store as None.

If at any point there are 4 known values, where a value has been calculated previously, we will continue to only input the 3 values given in the problem and input the calculated value as None as SUVAT can be misused and that can lead to giving the wrong answer if we were to put all 4 values in.

### How to compute the displacement
There are 4 different situations in which we might wish to find the displacement:

1. Given the **final velocity**, v, of the obejct in metres per second, **acceleration**, a, of the object in metres per second squared and the **time**, t, of travel in seconds, we can compute the displacement, s, in metres by doing:

```python
>>> import suvat
>>> suvat.find_displacement(u=None, v=7.5, a=10, t=6)
-135.0
```

2. Given the **initial velocity**, u, of the object in metres per second, **acceleration**, a, of the object in metres per second squared and the **time**, t, of travel in seconds, we can compute the displacement, s, in metres by doing:

```python
>>> import suvat
>>> suvat.find_displacement(u=4, v=None, a=10, t=6)
204.0
```

3. Given the **initial velocity**, u, of the object in metres per second, **final velocity**, v, of the object in metres per second and the **time**, t, of travel in seconds, we can compute the displacement, s, in metres by doing:

```python
>>> import suvat
>>> suvat.find_displacement(u=4, v=7.5, a=None, t=6)
34.5
```

4. Given the **initial velocity**, u, of the object in metres per second, **final velocity**, v, of the object in metres per second and the **acceleration**, a, of the object in metres per second squared, we can compute the displacement, s, in metres by doing:

```python
>>> import suvat
>>> suvat.find_displacement(u=4, v=7.5, a=10, t=None)
2.0125
```

### How to compute the initial velocity
There are 4 different situations in which we might wish to find the initial velocity:

1. Given the **final velocity**, v, of the obejct in metres per second, **acceleration**, a, of the object in metres per second squared and the **time**, t, of travel in seconds, we can compute the initial velocity, u, in metres per second by doing:

```python
>>> import suvat
>>> suvat.find_initial_velocity(s=None, v=7.5, a=10, t=6)
-52.5
```

2. Given the **displacement**, s, travelled in metres, **acceleration**, a, of the object in metres per second squared and the **time**, t, of travel in seconds, we can compute the initial velocity, u, in metres per second by doing:

```python
>>> import suvat
>>> suvat.find_initial_velocity(s=204, v=None, a=10, t=6)
4.0
```

3. Given the **displacement**, s, travelled in metres, **final velocity**, v, of the object in metres per second and the **time**, t, of travel in seconds, we can compute the initial velocity, u, in metres per second by doing:

```python
>>> import suvat
>>> suvat.find_initial_velocity(s=34.5, v=7.5, a=None, t=6)
4.0
```

4. Given the **displacement**, s, travelled in metres, **final velocity**, v, of the object in metres per second and the **acceleration**, a, of the object in metres per second squared, we can compute the initial velocity, u, in metres per second by doing:

```python
>>> import suvat
>>> suvat.find_initial_velocity(s=2.0125, v=7.5, a=10, t=None)
4.0
```

### How to compute the final velocity
There are 4 different situations in which we might wish to find the final velocity:

1. Given the **initial velocity**, u, of the object in metres per second, **acceleration**, a, of the object in metres per second squared and **time**, t, of travel in seconds, we can compute the final velocity, v, in metres per second by doing:

```python
>>> import suvat
>>> suvat.find_final_velocity(s=None, u=4, a=10, t=6)
64.0
```

2. Given the **displacement**, s, travelled in metres, **acceleration**, a, of the object in metres per second squared and **time**, t, of travel in seconds, we can compute the final velocity, v, in metres per second by doing:

```python
>>> import suvat
>>> suvat.find_final_velocity(s=-135, u=None, a=10, t=6)
7.5
```

3. Given the **displacement**, s, travelled in metres, **initial velocity**, u, of the object in metres per second and **time**, t, of travel in seconds, we can compute the final velocity, v, in metres per second by doing:

```python
>>> import suvat
>>> suvat.find_final_velocity(s=34.5, u=4, a=None, t=6)
7.5
```

4. Given the **displacement**, s, travelled in metres, **initial velocity**, u, of the object in metres per second and **acceleration**, a, of the object in metres per second squared, we can compute the final velocity, v, in metres per second by doing:

```python
>>> import suvat
>>> suvat.find_final_velocity(s=2.0125, u=4, a=10, t=None)
7.5
```

### How to compute the acceleration
There are 4 different situations in which we might wish to find the acceleration:

1. Given the **initial velocity**, u, of the object in metres per second, **final velocity**, v, of the object in metres per second and the **time**, t, of travel in seconds, we can compute the acceleration, a, in metres per second squared by doing:

```python
>>> import suvat
>>> suvat.find_acceleration(s=None, u=4, v=7.5, t=6)
0.5833333333333334
```

2. Given the **displacement**, s, travelled in metres, **final velocity**, v, of the object in metres per second and the **time**, t, of travel in seconds, we can compute the acceleration, a, in metres per second squared by doing:

```python
>>> import suvat
>>> suvat.find_acceleration(s=-135, u=None, v=7.5, t=6)
10.0
```

3. Given the **displacement**, s, travelled in metres, **initial velocity**, u, of the object in metres per second and the **time**, t, of travel in seconds, we can compute the acceleration, a, in metres per second squared by doing:

```python
>>> import suvat
>>> suvat.find_acceleration(s=204, u=4, v=None, t=6)
10.0
```

4. Given the **displacement**, s, travelled in metres, **initial velocity**, u, of the object in metres per second, and the **final velocity**, v, of the object in metres per second, we can compute the acceleration, a, in metres per second squared by doing:

```python
>>> import suvat
>>> suvat.find_acceleration(s=2.0125, u=4, v=7.5, t=None)
10.0
```

### How to compute the time
There are 4 different situations in which we might wish to find the acceleration:

1. Given the **initial velocity**, u, of the object in metres per second, **final velocity**, v, of the object in metres per second and the **acceleration**, a, of the object in metres per second squared, we can compute the time, t, in seconds by doing:

```python
>>> import suvat
>>> suvat.find_time(s=None, u=4, v=7.5, a=10)
0.35
```

2. Given the **displacement**, s, travelled in metres, **final velocity**, v, of the object in metres per second and the **acceleration**, a, of the object in metres per second squared, we can compute the time, t, in seconds by doing:

```python
>>> import suvat
>>> suvat.find_time(s=-135, u=None, v=7.5, a=10)
[6.0]
```

3. Given the **displacement**, s, travelled in metres, **initial velocity**, u, of the object in metres per second and the **acceleration**, a, of the object in metres per second squared, we can compute the time, t, in seconds by doing:

```python 
>>> import suvat
>>> suvat.find_time(s=204, u=4, v=None, a=10)
6.0
```

4. Given the **displacement**, s, travelled in metres, **initial velocity**, u, of the object in metres per second and the **final velocity**, v, of the object in metres per second, we can compute the time, t, in seconds by doing:

```python
>>> import suvat
>>> suvat.find_time(s=34.5, u=4, v=7.5, a=10)
6.0
```

## Explanation

### An overview of SUVAT
SUVAT stands for :  
  
$s$, displacement  
$u$, initial velocity  
$v$, final velocity  
$a$, acceleration  
$t$, time  

SUVAT equations are equations of motion and are used when the acceleration, a, is constant. The displacement, initial velocity, final velocity and acceleration variables are all vector quantities. This means that they have a magnitude and direction. Thus s, u, v or a can either be a positive or negative value as their sign will represent their direction of motion.

### Displacement, s
Displacement is a vector quantity that represents the change in position of the object.

It has the SI base unit of metres, $m$.

### Initial velocity, u
Initial velocity is a vector quantity that represents the velocity at which the motion starts. It is often found that in a problem the object might start from rest which refers to the initial velocity equalling $0 m/s$.

It has the SI base unit of metres per second, $m/s$.

### Final velocity, v
Final velocity is a vector quantity that represents the velocity at which the motion ends. It is often found that in a problem the object might come to a stop, which refers to the final velocity equalling $0 m/s$.

It has the SI base unit of metres per second, $m/s$.

### Acceleration, a
Acceleration is a vector quantity that represents the rate at which velocity changes with time. It is often found in questions that a ball might be dropping, or equivalent, and the acceleration needs to be treated as gravity. In this case the acceleration is often found to be $9.8 m/s^2$.

It has the SI base unit of metres per second squared, $m/s^2$.

### Time, t
The time we are referring to is the time of motion.

It has the SI base unit of seconds, $s$. (not to be confused with the symbol for displacement)

## Reference

### List of functionality
The following functions are written in `SUVAT`:

- `find_displacement`
- `find_initial_velocity`
- `find_final_velocity`
- `find_acceleration`
- `find_time`
  
### Bibliography
Some websites that give a good overview on the SUVAT equations and derivation:  
- <https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/mechanics/kinematics/equations-of-motion.html#:~:text=The%20equations%20of%20motion%2C%20also,%2D%20acceleration%20and%20t%20%2D%20time.>  
- <https://studywell.com/kinematics/suvat-equations/#:~:text=The%20SUVAT%20Equations%20describe%20motion,U%202%20%2B%202%20A%20S>

A text that includes some examples and information on SUVAT:  
>*Combo Book Formulae, Rearranging Equations and SUVAT: The Full Learning Pacakge for the Topic (Maths is Not A  Mystery). Panda Publications, 2023.*