from compressibleflow import Gas, RocketNozzle, Air

T0 = 500
P0 = 1000
gas = Air(T0,P0)

A_star = 0.002
A_exit = 0.008

#a
area_ratio = A_exit/A_star

Ma_e = Gas.ma_finder(gas, 'downward', area_ratio)
P_e = Gas.exit_pressure(gas, Ma_e)

m_throat = Gas.critical_m_dot(gas, 1,gas.diameter(A_star))

#b



#c

Ma_e_c = Gas.ma_finder(gas, 'upward', area_ratio)

P_e_c = Gas.exit_pressure(gas, Ma_e_c)













