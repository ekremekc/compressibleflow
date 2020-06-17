from compressibleflow import *

T1 = 470
P1 = 500
v1 = 180
A1 = 0.05
air = Air(T1,P1)

M1 = air.mach_number(v1)
T0 = air.stagnation_temp(M1)
P0 = air.stagnation_pressure(M1)

r_start = air.diameter(A1)/2

A_star = air.throat_area(A1, air.mach_number(v1))
r_star = air.diameter(A_star)/2
m_star = air.m_dot(v1,air.diameter(A1))

area = 0.036

ratio = air.throat_area_ratio(area,A1, M1)

Ma_upward = air.ma_finder("upward", ratio,True,method="golden")
Ma_downward = air.ma_finder("downward", ratio, True)

T_upward = air.temperature(Ma_upward,T0)
T_downward = air.temperature(Ma_downward,T0)

P_upward = air.pressure(Ma_upward,P0)
P_downward = air.pressure(Ma_downward,P0)

exit_p = air.exit_pressure(M1)

air.plot(0.5*A1, A1,M1,'Ma','T')