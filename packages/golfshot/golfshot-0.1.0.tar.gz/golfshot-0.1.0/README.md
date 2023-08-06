# Summary
golfshot allows users to run a 2D simulation of a golf shot given the following parameters:
- launch_angle: angle between horizon and the golf ball path at impact (degrees)
- launch_velocity: golf ball velocity off the club face (meters per second)
- rotation_rate: golf ball back spin at impact (radians per second)


Assumptions:
- The air temperature is 15C or 59F
  - Thus, kinematic viscosity is 1.48*10**-5 m/s/s

- Also, air pressure is 1 atm (sea-level) and 0% humidity.
  - Thus, air density is 1.225 kg/(m^3)

- Drag and lift coefficient equations are from the publication "Aerodynamics of Golf Balls in Still Air"
  - Assumptions and error in coefficient equations can be found in the publication


1. Lyu, Kensrud, et al. Aerodynamics of Golf Balls in Still Air. 23 February 2018. 
https://www.researchgate.net/publication/323372659_Aerodynamics_of_Golf_Balls_in_Still_Air
    
# Getting Started

## Basic Example
```
from golfshot import GolfShot

sim = GolfShot(launch_velocity=75,launch_angle=10,rotation_rate=300)
state_history = sim.run_sim()

print(state_history)
```
## Plotting Example
```
import plotly.express as px
import pandas as pd
from golfshot import GolfShot

# coefficients for converting units of intial states
rpm_to_rad_per_s = 1/9.549297 # rotations per minute to radians per second coeff
miles_ph_to_mps = 1/2.23694 # miles per hour to meters per second coeff

launch_vel_mph = 135 # Typical for an amateur golfer (miles per hour)
launch_vel_mps = launch_vel_mph*miles_ph_to_mps # convert to meters per second

launch_angle_deg = 14 # Varies greatly for amateurs (degrees)

rotation_rate_rpm = 2700 # Typical for an amateur golfer (rotations per minute)
rotation_rate_rps = rotation_rate_rpm*rpm_to_rad_per_s # convert to radians per second

sim = GolfShot(launch_velocity=launch_vel_mps,
                launch_angle=launch_angle_deg,
                rotation_rate=rotation_rate_rps)
vals = sim.run_sim()

df = pd.DataFrame(dict(x=vals[0], y=vals[1])) # create data fram for plotting
fig = px.line(  df, x="x", y="y",
                labels={"x": "Distance (yards)", "y": "Height (yards)",},
                title=f'Golf Shot; launch velocity: {launch_vel_mph} (mph)') # plot
fig.show() # show figure in default browser
```
