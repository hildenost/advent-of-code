# Configuration
FC := gfortran

utils: utils.f95
	$(FC) -c utils.f95

day1 : utils 01/calories.f95
	$(FC) 01/calories.f95 utils.o -o 01/day1 -std=f2008 -Wall

day2 : utils 02/rps.f95
	$(FC) 02/rps.f95 utils.o -o 02/day2 -std=f2008 -Wall

run1: day1
	01/day1

run2: day2
	02/day2



	
