import math
import matplotlib.pyplot as plt
import numpy as np

# Existing complex number operations (copy from the provided code)
def addition(complexA, complexB):
    resultReal = round(complexA[0] + complexB[0], 4)
    resultImg = round(complexA[1] + complexB[1], 4)
    return [resultReal, resultImg]

def multiplication(complexA, complexB):
    resultReal = round((complexA[0]*complexB[0] - complexA[1]*complexB[1]), 4)
    resultImg = round((complexA[0]*complexB[1] + complexA[1]*complexB[0]), 4)
    return [resultReal, resultImg]

def module(complex):
    complex[0] = float(complex[0])
    complex[1] = float(complex[1])
    result = round((complex[0]**2 + complex[1]**2)**(1/2), 4)
    return result

# New functions for the double-slit simulation
def wave_function(x, k, x0):
    """Calculate the wave function for a single slit."""
    phase = k * (x - x0)
    return [math.cos(phase), math.sin(phase)]

def double_slit_intensity(x, wavelength, slit_distance, screen_distance):
    """Calculate the intensity at a point x on the screen."""
    k = 2 * math.pi / wavelength
    slit1 = wave_function(x, k, -slit_distance/2)
    slit2 = wave_function(x, k, slit_distance/2)
    total_wave = addition(slit1, slit2)
    intensity = module(total_wave)**2
    return intensity

def simulate_double_slit(wavelength, slit_distance, screen_distance, screen_width, num_points):
    """Simulate the double-slit experiment and return the intensity pattern."""
    x = np.linspace(-screen_width/2, screen_width/2, num_points)
    intensity = [double_slit_intensity(xi, wavelength, slit_distance, screen_distance) for xi in x]
    return x, intensity

# Simulation parameters
wavelength = 0.1  # wavelength of the particles
slit_distance = 0.5  # distance between the slits
screen_distance = 10.0  # distance to the screen
screen_width = 10.0  # width of the screen
num_points = 1000  # number of points to calculate

# Run the simulation
x, intensity = simulate_double_slit(wavelength, slit_distance, screen_distance, screen_width, num_points)

# Plot the results
plt.figure(figsize=(10, 6))
plt.plot(x, intensity)
plt.title("Double-slit Experiment Simulation")
plt.xlabel("Position on screen")
plt.ylabel("Intensity")
plt.grid(True)
plt.show()