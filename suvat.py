import numpy as np

def find_displacement(u, v, a, t):
    """
    Defines the function to find the displacement (in metres) of the object. Including when different SUVAT 
    variables are unknown.
    """
    if u is None:
        """
        Returns the displacement (in metres) of the object when the initial velocity, u, is unknown
        by using the SUVAT equaton: 
        displacement = final velocity x time - 1/2 x acceleration x time squared

        It uses the final velocity (in metres per second), v, time (in seconds), t, and acceleration (in metres per 
        second squared), a, as inputted.
        """
        displacement = (float(v) * float(t)) - (0.5 * float(a) * float(t) ** 2)
        return displacement
    if v is None:
        """
        Returns the displacement (in metres) of the object when the final velocity, v, is unknown by using
        the SUVAT equation:
        displacement = initial velocity x time + 1/2 x acceleration x time squared

        It uses the initial velocity (in metres per second), u, time (in seconds), t, and acceleration (in metres 
        per second squared), a, as inputted.
        """
        displacement = (float(u) * float(t)) + (0.5 * float(a) * float(t) ** 2)
        return displacement
    if a is None:
        """
        Returns the displacement (in metres) of the object when the acceleration, a, is unknown by using the SUVAT
        equation:
        displacement = 1/2 x (initial velocity + final velocity) x time

        It uses the initial velocity (in metres per second), u, final velocity (in metres per second), v, and time
        (in seconds), t, as inputted.
        """
        displacement = 0.5 * (float(u) + float(v)) * float(t)
        return displacement
    if t is None:
        """
        Returns the displacement (in metres) of the object when the time, t, is unknown by rearranging the SUVAT 
        equation:
        final velocity squared = initial velocity squared + 2 x acceleration x displacement

        It uses the final velocity (in metres per second), v, initial velocity (in metres per second), u, and
        acceleration (in metres per second squared), a, as inputted.
        """
        displacement = (float(v) ** 2 - float(u) ** 2) / (2 * float(a))
        return displacement

def find_initial_velocity(s, v, a, t):
    """
    Defines the function to find the initial velocity (in metres per second) of the object. Including when different 
    SUVAT variables are unknown.
    """
    if s is None:
        """
        Returns the initial velocity (in metres per second) of the object when the displacement, s, is unknown by
        rearranging the SUVAT equation:
        final velocity = initial velocity + acceleration x time

        It uses the final velocity (in metres per second), v, acceleration (in metres per second squared), a, and
        the time (in seconds), s, as inputted.
        """
        initialvelocity = float(v) - (float(a) * float(t))
        return initialvelocity
    if v is None:
        """
        Returns the initial velocity (in metres per second) of the object when the final velocity, v, is unknown by
        rearranging the SUVAT equation:
        displacement = initial velocity x time + 1/2 x acceleration x time squared

        It uses the displacement (in metres), s, acceleration (in metres per second squared), a, and the time (in
        seconds), t, as inputted.
        """
        initialvelocity = (float(s) - (0.5 * float(a) * float(t) ** 2)) / float(t)
        return initialvelocity
    if a is None:
        """
        Returns the initial velocity (in metres per second) of the object when the acceleration, a, is unknown by
        rearranging the SUVAT equation:
        displacement = 1/2 x (initial velocity + final velocity) x time

        It uses the displacement (in metres), s, time (in seconds), t, and final velocity (in metres per second),
        v, as inputted.
        """
        initialvelocity = ((2 * float(s)) / float(t)) - float(v)
        return initialvelocity
    if t is None:
        """
        Returns the initial velocity (in metres per second) of the object when the time, t, is unknown by rearranging
        the SUVAT equation:
        final velocity squared = initial velocity squared + 2 x acceleration x displacement

        It uses the final velocity (in metres per second), v, the acceleration (in metres per second squared), a,
        and the displacement (in metres), s, as inputted.
        """
        initialvelocity = np.sqrt(float(v) ** 2 - (2 * float(a) * float(s)))
        return initialvelocity

def find_final_velocity(s, u, a, t):
    """
    Defines the function to find the final velocity (in metres per second) of the object. Including when different 
    SUVAT variables are unknown.
    """
    if s is None:
        """
        Returns the final velocity (in metres per second) of the object when the displacement, s, is unknown by 
        using the SUVAT equation:
        final velocity = initial velocity + acceleration x time

        It uses the initial velocity (in metres per second), u, the acceleration (in metres per second squared), a,
        and the time (in seconds), t, as inputted.
        """
        finalvelocity = float(u) + (float(a) * float(t))
        return finalvelocity
    if u is None:
        """
        Returns the final velocity (in metres per second) of the object when the initial velocity, u, is unknown by 
        rearranging the SUVAT equation:
        displacement = final velocity x time - 1/2 x acceleration x time squared

        It uses the displacement (in metres), s, the acceleration (in metres per second squared), a, and the time 
        (in seconds), t, as inputted.
        """
        finalvelocity = (float(s) + (0.5 * float(a) * float(t) ** 2)) / float(t)
        return finalvelocity
    if a is None:
        """
        Returns the final velocity (in metres per second) of the object when the acceleration, a, is unknown by 
        rearranging the SUVAT equation:
        displacement = 1/2 x (initial velocity + final velocity) x time

        It uses the displacement (in metres), s, the time (in seconds), t, and the initial velocity (in metres per
        second), u, as inputted. 
        """
        finalvelocity = ((2 * float(s)) / float(t)) - float(u)
        return finalvelocity
    if t is None:
        """
        Returns the final velocity (in metres per second) of the object when the time, t, is unknown by using the
        SUVAT equation:
        final velocity squared = initial velocity squared + 2 x acceleration x displacement

        It uses the initial velocity (in metres per second), u, acceleration (in metres per second squared), a, and
        the displacement (in metres), s, as inputted.
        """
        finalvelocity = np.sqrt(float(u) ** 2 + (2 * float(a) * float(s)))
        return finalvelocity
    
def find_acceleration(s, u, v, t):
    """
    Defines the function to find the acceleration (in metres per second squared) of the object. Including when 
    different SUVAT variables are unknown.
    """
    if s is None:
        """
        Returns the acceleration (in metres per second squared) of the object when the displacement, s, is unknown
        by rearranging the SUVAT equation:
        final velocity = intiial velocity + acceleration x time

        It uses the final velocity (in metres per second), v, initial velocity (in metres per second), u, and the
        time (in seconds), t, as inputted.
        """
        acceleration = (float(v) - float(u)) / float(t)
        return acceleration
    if u is None:
        """
        Returns the acceleration (in metres per second squared) of the object when the initial velocity, u, is
        unknown by rearranging the SUVAT equation:
        displacement = final velocity x time - 1/2 x acceleration x time squared

        It uses the final velocity (in metres per second), v, time (in seconds), t, and displacement (in metres),
        s, as inputted.
        """
        acceleration = (2 * ((float(v) * float(t)) - float(s))) / (float(t) ** 2)
        return acceleration
    if v is None:
        """
        Returns the acceleration (in metres per second squared) of the object when the final velocity, v, is
        unknown by rearranging the SUVAT equation:
        displacement = initial velocity x time + 1/2 x acceleration x time squared

        It uses the displacement (in metres), s, initial velocity (in metres per second), u, and time (in seconds),
        t, as inputted.
        """
        acceleration = (2 * (float(s) - (float(u) * float(t)))) / (float(t) ** 2)
        return acceleration
    if t is None:
        """
        Returns the acceleration (in metres per second squared) of the object when the time, t, is unknown by
        rearranging the SUVAT equation:
        final velocity squared = initial velocity squared + 2 x acceleration x displacement

        It uses the final velocity (in metres per second), v, initial velocity (in metres per second), u, and 
        displacement (in metres), s, as inputted.
        """
        acceleration = (float(v) ** 2 - float(u) ** 2) / (2 * float(s))
        return acceleration
    
def find_time(s, u, v, a):
    """
    Defines the function to find the time (in seconds) of the object. Including when different SUVAT variables 
    are unknown.
    """
    if s is None:
        """
        Returns the time (in seconds) of the object when the displacement, s, is unknown by rearranging the SUVAT
        equation:
        final velocity = intiial velocity + acceleration x time

        It uses the final velocity (in metres per second), v, initial velocity (in metres per second), u, and
        acceleration (in metres per second), a, as inputted.
        """
        time = (float(v) - float(u)) / float(a)
        return time
    if u is None:
        """
        Returns the time (in seconds) of the object when the initial velocity, u, is unknown by rearranging the
        SUVAT equations:
        final velocity = intiial velocity + acceleration x time
        and
        final velocity squared = initial velocity squared + 2 x acceleration x displacement

        It uses the final velocity (in metres per second), v, acceleration (in metres per second squared), a,
        and the displacement (in metres), s, as inputted.
        """
        time1 = (float(v) - np.sqrt(float(v) ** 2 - (2 * float(a) * float(s)))) / float(a)
        time2 = (float(v) + np.sqrt(float(v) ** 2 - (2 * float(a) * float(s)))) / float(a)

        times = [time1, time2]
        time = [num for num in times if num >= 0]
        return time
    if v is None:
        """
        Returns the time (in seconds) of the object when the final velocity, v, is unknown by rearranging the SUVAT
        equations:
        final velocity = intiial velocity + acceleration x time
        and
        final velocity squared = initial velocity squared + 2 x acceleration x displacement

        It uses the acceleration (in metres per second squared), a, displacement (in metres), s, and initial
        velocity (in metres per second), u, as inputted.
        """
        time = (np.sqrt(2 * float(a) * float(s) + float(u) ** 2) - float(u)) / float(a)
        return time
    if a is None:
        """
        Returns the time (in seconds) of the object when the acceleration, a, is unknown by rearranging the SUVAT
        equation:
        displacement = 1/2 x (initial velocity + final velocity) x time

        It uses the displacement (in metres), s, final velocity (in metres per second), v, and initial velocity (in
        metres per second), u, as inputted.
        """
        time = (2 * float(s)) / (float(v) + float(u))
        return time