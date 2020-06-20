from compressibleflow import *

P0 = 300
T0 = 500
air = Air(P0,T0)

area_star = 1
area_shock = 2
area_ratio = area_shock/area_star
Ma = air.ma_finder('downward',  area_ratio)
T1 = air.temperature(Ma, T0)
P1 = air.pressure(Ma, P0)

P2 = air.normalshock.P2(Ma)
Ma2 = air.normalshock.Ma2(Ma)
P02 = air.normalshock.P0_2(P0, Ma)
A2_star = air.normalshock.area_shock_star(area_star, Ma)

area_3 = 3
exit_ratio = area_3/A2_star
Ma3 = air.ma_finder('upward',  exit_ratio,True)
P3 = air.pressure(Ma3, P02)