# Double-Slit Experiment Simulation

This Python script simulates the famous double-slit experiment, demonstrating the wave-particle duality of quantum mechanics. The simulation uses complex number operations to calculate and visualize the interference pattern created when particles pass through two slits.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Customization](#customization)
- [Theory](#theory)

## Requirements

- Python 3.6+
- NumPy
- Matplotlib

## Installation

1. Ensure you have Python 3.6 or higher installed on your system.
2. Install the required libraries:

   ```
   pip install numpy matplotlib
   ```

3. Download the `double_slit_simulation.py` file to your local machine.

## Usage

To run the simulation:

1. Open a terminal or command prompt.
2. Navigate to the directory containing `double_slit_simulation.py`.
3. Run the script:

   ```
   python double_slit_simulation.py
   ```

4. The script will generate a plot showing the interference pattern of the double-slit experiment.

## Code Structure

The simulation is composed of several key functions:

- `addition`, `multiplication`, `module`: Complex number operations.
- `wave_function`: Calculates the wave function for a single slit.
- `double_slit_intensity`: Computes the intensity at a point on the screen.
- `simulate_double_slit`: Generates the intensity pattern across the screen.

The main part of the script sets up simulation parameters and runs the simulation.

## Customization

You can customize the simulation by modifying the following parameters in the script:

```python
wavelength = 0.1        # wavelength of the particles
slit_distance = 0.5     # distance between the slits
screen_distance = 10.0  # distance to the screen
screen_width = 10.0     # width of the screen
num_points = 1000       # number of points to calculate
```

Adjust these values to see how they affect the interference pattern.

## Theory

The double-slit experiment is a fundamental demonstration of quantum mechanics. It shows that particles (like electrons or photons) can exhibit both particle and wave-like behavior.

In this simulation:

1. We represent the wave function of particles using complex numbers.
2. The wave functions from each slit are combined to create an interference pattern.
3. The intensity at each point on the screen is calculated as the square of the magnitude of the combined wave function.

The resulting plot shows alternating peaks and troughs, which represent the interference pattern observed in the actual experiment.