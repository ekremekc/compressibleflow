from compressibleflow import *
T1 = 289
air = Air(T1)

#### Option a

P2 = 1379

ratio =P2/air.P

alfa = air.speed_of_sound()

Ma1 = air.normalshock.Ma_beforeshock(ratio) 

V1 = Ma1*alfa

#### Option b

T2 = air.normalshock.T2(T1, Ma1)

V2 = air.normalshock.V2(T1, V1)

V = V1-V2