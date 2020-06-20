from compressibleflow import *

Gas.gas_list()
air = Air(500, 200)

m_dot = 3 #kg/s

area = air.critical_area(m_dot)

d = air.diameter(area)


Ma =3 

P_e = air.exit_pressure(Ma)
T_e = air.exit_temperature(Ma)
V_e = air.exit_speed(Ma)

A_e = air.exit_area(area, Ma)

D_e = air.diameter(A_e)