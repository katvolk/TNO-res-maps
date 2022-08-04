# TNO-res-maps

This repository contains a representative subset of the mean motion resonance mapping 
simulation data (data directory) presented in [Volk & Malhotra (2022)](https://arxiv.org/abs/2208.02248) for 23 observed 
distant trasneptunian objects (TNOs). Python scripts are also included (plot-scripts 
directory) to reproduce or modify the resonance map plots (plots directory). 

If you use the data in this repository, cite Volk & Malhotra 2022 (NASA ADS link 
forthcoming)

Please see the paper for all the relevant details about how the simulation data was 
produced and how to interpret these Poincare maps.

### data file details

The files in the data directory contain time-histories of test particles
simulated in the vicinities of the indicated TNOs. (This information is also
available as a text file within the data directory.)

For each particle, the time-histories contain the state of the particle
at its perihelion passage (mean anomaly = 0) for 1000 perihelion passages.

The comma separated columns are as follows:
- stability, integer decoded as: 
  - 0 = no resonant libration lasting more than 750 cycles in N:5 or 
                  lower-order resonance
  - 1 = stable resonant libration lasting at least 1000 cycles
  - 2 = quasi-stable resonant libration lasting between 750-1000 cycles
- res-p, integer p for a p:q exterior resonance (e.g., p=3 for pluto), 0 for particles with stability=0
- res-q, integer q for a p:q exterior resonance (e.g., q=2 for pluto), 0 for particles with stability=0
- id, integer, test particle identifier (note, not necessarily unique in file)
- time, simulation time in years 
- a, test particle semimajor axis in au 
- psi, delta mean longitude between the particle and Neptune in radians 
- e, test particle eccentricity 
- inc, test particle inclination in radians

### plots directory

For each TNO, the test particle data in the data directory is plotted in individual PDFs.
Each test particle is plotted with a random different color (colors are repeated however).
The large black dots show the best-fit orbit of the TNO along with the 1 and 3 sigma 
uncertainties in the orbit's semimajor axis. See Volk & Malhotra (2022), especially Figure
2 for more details. These plots can be re-generated using the same simulation data with
updated orbit fits for these TNOs.

### plot-scripts directory

This directory contains Python scripts to plot Poincare maps near each of the indicated TNOs
using the files in the data directory. The resulting plots are in the plots directory.
(This information is also available as a text file within the plot-scripts directory.)

Each script has the observed best-fit semimajor axis (varaible abf), the 1-sigma uncertainty in 
semimajor axis (variable da) and psi value (variablle obspsi; the difference in mean longitude 
between Neptune and the object) at the epoch of the object's most recent (or near future) perihelion 
passage (variable tp). These match the values in Table 1 of Volk & Malhotra (2022).


You can update these variables with new orbit fits for the TNOs by editing the appropriate variables 
in each python script to see how improvements to the orbit affect a TNO's potential resonant status. 
