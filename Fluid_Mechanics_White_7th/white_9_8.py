from compressibleflow import *

T0 = 400
P0 = 120
gas = Air(T0,P0)

P_star = gas.critical_pressure()
area = 0.0006
nozzle = Nozzle(gas)

#a
Pb_a = 90
Ma_e = nozzle.exit_mach(Pb_a)
mdot_a = nozzle.massflowrate(Pb_a, area)
print(nozzle.ischoked(Pb_a))

#b
Pb_b = 45
Ma_e_b = nozzle.exit_mach(Pb_b)
mdot_b = nozzle.massflowrate(Pb_b, area)













