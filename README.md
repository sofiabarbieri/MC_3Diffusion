# DiffCoeffIter
***
DiffCoeffIter is a MonteCarlo tool developed to compute the diffusion coefficient given th particle velocity is a 3D space.
The tool is needed to MCele_ProteinGradient as velocity calibation
## Requirements
***
* Python
* Matplotlib
* numpy
## System/Package versions tested
***
* OS: Ubuntu18 - Fedora33
* Python: 2.7.18
* Matplotlib: 2.2.5
* numpy: 1.16.6
* scipy: 1.2.3
***
The software may run with other versions. Python3 is NOT supported.
## How to run
***
```
 python main_iter_2.py -p 100000 
```
where p stands for number of particles 
## Expected output
***
The output is composed of two columns: the particle velocity and the particle diffusivity.
An example of output is provided in the repo.
 
