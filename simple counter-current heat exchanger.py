import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# PARAMETERS
u  = float(input("Enter the overall heat transfer coefficient : "))

#  for heat transfer area per unit length
area = float(input("Enter total area :"))
l = float(input("Enter length of exchanger : "))

area_per_length = area/l

m_h = float(input("Enter mass flow rate for hot water : "))
C_p_h = float(input("Enter the specific heat for hot water :"))


m_c = float(input("Enter mass flow rate for cold water : "))
C_p_c = float(input("Enter the specific heat for cold water :"))



#Inlet Temperatures
T_hin = float(input("Enter inlet temp for hot water : "))
T_cin = float(input("Enter inlet temp for cold water : "))


def heat_exchanger(T, z):
    T_h , T_c = T
    dT_hdz = - (u * area_per_length / (m_h * C_p_h)) * (T_h - T_c)
    dT_cdz = (u * area_per_length / (m_c * C_p_c)) * (T_h - T_c)
    return [dT_hdz, -dT_cdz]


z = np.linspace(0, l, 100)


T0 = [T_hin,T_cin]


sol = odeint(heat_exchanger,T0,z)

T_h = sol[:,0]
T_c = sol[:,1]


plt.figure(figsize=(8, 5))
plt.plot(z, T_h, 'r-', linewidth=2, label='Hot Fluid')
plt.plot(z, T_c, 'b-', linewidth=2, label='Cold Fluid')
plt.xlabel('Length along Heat Exchanger (m)')
plt.ylabel('Temperature (°C)')
plt.title('Counter-Current Heat Exchanger Simulation')
plt.legend()
plt.grid(True)
plt.show()




#simple inputs
# Enter the overall heat transfer coefficient : 500
# Enter total area :50
# Enter length of exchanger : 10
# Enter mass flow rate for hot water : 1.5
# Enter the specific heat for hot water :4180
# Enter mass flow rate for cold water : 2.0
# Enter the specific heat for cold water :4180
# Enter inlet temp for hot water : 120
# Enter inlet temp for cold water : 30
