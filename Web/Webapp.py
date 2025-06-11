import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Heat exchanger function
def heat_exchanger(U, A_total, L, m_h, C_p_h, m_c, C_p_c, T_h_in, T_c_in, flow_type):
    A_per_length = A_total / L
    
    def model(T, z):
        T_h, T_c = T
        dT_hdz = - (U * A_per_length / (m_h * C_p_h)) * (T_h - T_c)
        dT_cdz = (U * A_per_length / (m_c * C_p_c)) * (T_h - T_c)
        if flow_type == 'Counter-current':
            return [dT_hdz, -dT_cdz]
        else:
            return [dT_hdz, dT_cdz]

    z = np.linspace(0, L, 100)
    T0 = [T_h_in, T_c_in]
    sol = odeint(model, T0, z)
    
    T_h = sol[:, 0]
    T_c = sol[:, 1]
    
    return z, T_h, T_c

# Streamlit UI
st.title("Heat Exchanger Simulation App 🔥")

flow_type = st.selectbox("Flow Type:", ['Co-current', 'Counter-current'])
U = st.slider("Overall Heat Transfer Coefficient (W/m²·K)", 100, 2000, 500)
A_total = st.slider("Total Heat Transfer Area (m²)", 10, 200, 50)
L = st.slider("Exchanger Length (m)", 1, 20, 10)

m_h = st.number_input("Hot Fluid Mass Flow Rate (kg/s)")
C_p_h = st.number_input("Hot Fluid Heat Capacity (J/kg·K)")
m_c = st.number_input("Cold Fluid Mass Flow Rate (kg/s)")
C_p_c = st.number_input("Cold Fluid Heat Capacity (J/kg·K)")

T_h_in = st.number_input("Hot Fluid Inlet Temp (°C)")
T_c_in = st.number_input("Cold Fluid Inlet Temp (°C)")

if st.button("Simulate"):
    z, T_h, T_c = heat_exchanger(U, A_total, L, m_h, C_p_h, m_c, C_p_c, T_h_in, T_c_in, flow_type)

    # Plotting
    st.subheader("Temperature Profiles")
    import matplotlib.pyplot as plt
    fig, ax = plt.subplots()
    ax.plot(z, T_h, 'r-', label='Hot Fluid')
    ax.plot(z, T_c, 'b-', label='Cold Fluid')
    ax.set_xlabel('Length (m)')
    ax.set_ylabel('Temperature (°C)')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
