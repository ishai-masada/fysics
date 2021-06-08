import math
import spicy.integrate as integrate
import spicy.special as special

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


    def __add__(self, b):
        if isinstance(b, Vector2):
            return Vector2(self.x + b.x, self.y + b.y)
        else:
            raise TypeError('do no go')


    def __truediv__(self, b):
        if isinstance(b, (float, int)):
            return Vector2(self.x/b, self.y/b)
        else:
            raise TypeError('do no go')
        

    def __mul__(self, b):
        if isinstance(b, (float, int)):
            return Vector2(self.x*b, self.y*b)
        else:
            raise TypeError('do no go')


    def length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


class Point:
    def __init__(self, position=None, velocity=None):
        self.position = position or Vector2()
        self.velocity = velocity or Vector2()


    def step(self, steps_per_sec, gravity=Vector2(0, -9.8)):
        self.position += self.velocity / steps_per_sec
        self.velocity += gravity
        if self.position.y <= 0:
            self.velocity.y = 0
            self.position.y = 0


class Ball:
    def __init__(self, radius, bounce, density, friction, position=None, velocity=None):
        self.position = position or Vector2()
        self.velocity = velocity or Vector2()
        self.radius = radius
        self.bounce = bounce
        self.density = density
        self.friction = friction
        
    def step(self, steps_per_sec, gravity=Vector2(0, -9.8)):
        self.position += self.velocity / steps_per_sec
        self.velocity += gravity
        if self.position.y - self.radius <= 0:
            self.velocity.y = 0
            self.position.y = self.radius
            
    def roll(self, x_velocity):
        if velocity.x != 0:
            pass

    @property
    def mass(self):
        return self.density / self.area
 
    @property
    def rotation(self):
        return atan(self.position.x / self.position.y)

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def inertia(self):
        return list(integrate.quad(lambda self.mass, self.radius: self.mass * self.radius**2, 0, math.inf))[0]
 
    @property
    def ang_mtm(self):
        return self.radius * self.mass * self.velocity.x

    @property
    def ang_speed(self):
        return self.ang_mtm / self.inertia


def simulate_bodies(bodies, duration, steps_per_sec=1, gravity=Vector2(0, -9.8)):
    time = 0
    while time < duration:
        time += 1 / steps_per_sec
        for body in bodies:
            body.step(steps_per_sec, gravity) 


def ball_throw(ang, speed):
    """ angle is in degrees and speed in meters/second"""
    
    ball_throw_dict = dict()
    # Convert angle to radians
    converted_ang = (ang * math.pi) / 180

    # Get the vertical speed of the ball
    v_speed = speed * math.sin(converted_ang)
    
    acceleration = 9.8
    
    # Calculate the time it takes for ball to land
    time = round(2 * v_speed/acceleration, 2)

    # Check to see if trig functuion made time negative
    if time < 0:
        time = -1 * time

    # Use the range equation to find the distance
    distance = round((speed**2 * math.sin(2*converted_ang))/ acceleration, 2)

    # Store time and distance into dictionary
    ball_throw_dict["distance"] = distance
    ball_throw_dict["time"] = time

    return fysics_dict


def simulated_ball_throw(ang, speed):
    acceleration = 9.8
    simulated_dict = dict()
    steps_per_sec = 500
    position = Vector2()
    converted_ang = (ang * math.pi) / 180
    v_speed = speed * math.sin(converted_ang)
    h_speed = speed * math.cos(converted_ang)
    velocity = Vector2(v_speed, h_speed)
    time = 0 
    
    while True:
        position += velocity / steps_per_sec
        velocity.y -= 9.8/steps_per_sec
        distance = abs(round(position.x, 1))
        
        
        # Calculate the time it takes for ball to land
        time += 1 / steps_per_sec 
        
        # Verify the velocity to find the maximum height
        if velocity.y >= 0:
            max_altitude = round(position.y, 2)
            
            # Store the maximum altitude into the dictionary
            simulated_dict["maximum height"] = max_altitude

        current_velocity = velocity.length()
        if current_velocity > simulated_dict.get('max velocity', 0):
            simulated_dict['max velocity'] = current_velocity


        # Store time and range into dictionary
        if position.y < 0:
            simulated_dict["distance"] = distance
            simulated_dict["time"] = time
            return simulated_dict
    
