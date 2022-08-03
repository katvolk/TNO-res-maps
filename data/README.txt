The files in this directory contain time-histories of test particles
simulated in the vicinities of the indicated TNOs.

For each particle, the time-histories contain the state of the particle
at its perihelion passage (mean anomaly =0) for 1000 perihelion passages.

The comma separated columns are as follows:
	1) stability, integer decoded as: 
			0 = no resonant libration lasting more than 750 cycles in N:5 or 
				lower-order resonance
			1 = stable resonant libration lasting at least 1000 cycles
			2 = quasi-stable resonant libration lasting between 750-1000 cycles
	res-p, integer p for a p:q exterior resonance (e.g., p=3 for pluto)
	res-q, integer q for a p:q exterior resonance (e.g., q=2 for pluto)
	id, integer, test particle identifier (note, not necessarily unique in file)
	time, simulation time in years
	a, test particle semimajor axis in au
	psi, delta mean longitude between the particle and Neptune in radians
	e, test particle eccentricity
	inc, test particle inclination in radians
