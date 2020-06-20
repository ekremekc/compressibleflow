from compressibleflow import *
P1 = 1700
rho1 = 18
gas_1 = Ar(P=P1)



T1 = P1/(gas_1.R*rho1)
gas_1 = Ar(T1,P1) 
h1 = gas_1.enthalpy()

T2 = 400
P2 = 248
gas_2 = Ar(T2,P2)

h2 = gas_2.enthalpy()
rho2 = gas_2.density()

delta_h = h2-h1
delta_s = relations.change_in_entropy(T2, T1, P2, P1, gas_1.cp, gas_1.R)





