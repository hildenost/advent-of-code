# Configuration
FC := gfortran

utils: utils.f95
	$(FC) -c utils.f95

day2 : utils 02/rps.f95
	$(FC) 02/rps.f95 utils.o -o 02/day2 -std=f2008 -Wall

run2: day2
	02/day2



	
