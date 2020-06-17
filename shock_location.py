from compressibleflow import *

#Reservoir Characteristics
T0 = 500 #K
P0 = 1000 #kPa
P01 = P0 #kPa

#Building Air Object
gas = Air(T0,P0)

#Displaying gases in the library
gas.gas_list()

A_start=0.003 #m2
A1_star = 0.002 #m2
A_exit = 0.008 #m2

#Building Nozzle object by using air object
nozzle = RocketNozzle(gas)


P_c=300 #Ambient Pressure kPa

#Demonstration of Nozzle Geometry
nozzle.geometry(A_start, A1_star, A_exit)

#Displaying shock position in CD Nozzle
A_b=nozzle.shock(P_c, A1_star, A_exit,A_exit/2)

#Mach Number and Temperature Distribution Along CD Nozzle
gas.plot(A_start, A_exit,0.4,'T','Ma')
gas.plot(A_start, A_exit,0.4,'Ma','T')







