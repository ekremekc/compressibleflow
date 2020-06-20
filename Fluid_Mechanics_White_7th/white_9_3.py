from compressibleflow import *


T1 = 320 #K
P1 = 170 #kPa
V1 = 240 #m/s

air = Air(T1,P1)

#d
Ma1 = air.mach_number(V1)

#a
P0 = air.stagnation_pressure(Ma1)
#b
T0 = air.stagnation_temp(Ma1)
#c
ro0 = P0/(T0*air.R)

Vmax = np.sqrt(air.cp*2*T0)

V_star = air.critical_speed_of_sound(Ma1)

V2 = 290
Ma2 = air.mach_number(V2)
T2 = air.temperature(Ma2, T0)
P0 = air.stagnation_pressure(Ma2)












