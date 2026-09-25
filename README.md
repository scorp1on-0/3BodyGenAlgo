# 3BodyGenAlgo
 A simple attempt to find a stable solution for the Three-Body Problem using a Genetic Algorithm.

## Reason
The objective of this program is to observe and study the scale of the effects of small changes in the initial conditions of a chaotic system. This way, the program attepmts to find a stable solution for the Three-Body Problem using a Genetic Algorithm approach.

## Current limitations
The formulas used to calculate the motion of the objects are Newtonian and do not take into account relativistic fenomena. Moreover, they are currently approximations made to fit the program. Furthermore, computational limitations also come into play when attempting to find a stable solution, as the program is not optimised.

## Usage
The program will run with a PyGame GUI, while displaying the three bodies, the current generation and the current iteration of the generation. Small lines representing velocity vectors are also visible on the objects. The program will start with a small amount of time for the first simulations, and will progressively increase with the generations. If no collisions occur in a simulation, the genome (initial conditions) is assumed to be of interest and is used and mutated in the next generation.

## Notes
The code is 100% human written.
