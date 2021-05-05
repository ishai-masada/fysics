import math
fysics_dict = dict()

def ball_throw(ang, speed):
    # angle is in degrees and speed in meters/second
    
    # Convert angle to radians
    converted_ang = (ang * math.pi) / 180

    # Get the vertical speed of the ball
    v_speed = speed * math.sin(converted_ang)
    
    acceleration = 9.8
    
    # calculate the time it takes for ball to land
    time = round(2 * v_speed/acceleration, 2)

    # Check to see if trig functuion made time negative
    if time < 0:
        time = -1 * time

    # Use the range equation to find the distance
    distance = round((speed**2 * math.sin(2*converted_ang))/ acceleration, 2)

    # Put time and distance into dictionary
    fysics_dict["range in meters"] = distance
    fysics_dict["time in seconds"] = time

    return fysics_dict
