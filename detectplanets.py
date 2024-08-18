import cv2
import numpy as np
import math


width, height = 800, 800
background_color = (0, 0, 0)
sun_color = (0, 255, 255)
planet_color = (255, 255, 255)
sun_radius = 40
planet_radius = 10


canvas = np.zeros((height, width, 3), dtype="uint8")
canvas[:] = background_color


sun_position = (width // 2, height // 2)


cv2.circle(canvas, sun_position, sun_radius, sun_color, -1)

planets = [
    {"distance": 100, "angle": 0, "speed": 0.01},
    {"distance": 150, "angle": 0, "speed": 0.008},
    {"distance": 200, "angle": 0, "speed": 0.006},
    {"distance": 250, "angle": 0, "speed": 0.004},
    {"distance": 300, "angle": 0, "speed": 0.002},
]


def calculate_position(distance, angle):
    x = int(sun_position[0] + distance * math.cos(angle))
    y = int(sun_position[1] + distance * math.sin(angle))
    return (x, y)


while True:
  
    canvas[:] = background_color

    
    cv2.circle(canvas, sun_position, sun_radius, sun_color, -1)

    
    for planet in planets:
        planet["angle"] += planet["speed"]  # Update the angle
        position = calculate_position(planet["distance"], planet["angle"])
        cv2.circle(canvas, position, planet_radius, planet_color, -1)

    
    cv2.imshow("Solar System Simulation", canvas)

 
    if cv2.waitKey(10) & 0xFF == 27:
        break

cv2.destroyAllWindows()
