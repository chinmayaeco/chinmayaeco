import streamlit as st
import pandas as pd
import altair as alt
import numpy as np

st.set_page_config(page_title="Supply & Demand Simulation", layout="wide")

st.title("Law of Supply and Demand Simulation")

st.sidebar.header("Simulation Parameters")

# Demand parameters: P = a - b * Q
st.sidebar.subheader("Demand Curve")
demand_intercept = st.sidebar.slider("Demand Shift (Intercept, a)", min_value=50.0, max_value=200.0, value=100.0, step=5.0)
demand_slope = st.sidebar.slider("Demand Slope (b)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

# Supply parameters: P = c + d * Q
st.sidebar.subheader("Supply Curve")
supply_intercept = st.sidebar.slider("Supply Shift (Intercept, c)", min_value=0.0, max_value=100.0, value=20.0, step=5.0)
supply_slope = st.sidebar.slider("Supply Slope (d)", min_value=0.1, max_value=5.0, value=1.0, step=0.1)

st.markdown("""
This application simulates the basic economic principles of supply and demand. 
Use the sidebar to adjust the parameters of the Demand ($P = a - bQ$) and Supply ($P = c + dQ$) curves and instantly observe how shifts in the curves and changes in price elasticity affect the market equilibrium.
""")

if demand_intercept <= supply_intercept:
    st.error("Demand intercept must be greater than Supply intercept for a meaningful market equilibrium in this simple linear model.")
else:
    # Calculate Equilibrium
    # Q_eq = (a - c) / (b + d)
    q_eq = (demand_intercept - supply_intercept) / (demand_slope + supply_slope)
    p_eq = supply_intercept + supply_slope * q_eq

    col1, col2 = st.columns(2)
    col1.metric("Equilibrium Quantity (Q*)", f"{q_eq:.2f} units")
    col2.metric("Equilibrium Price (P*)", f"${p_eq:.2f}")

    # Generate Data for Plotting
    q_max = max(100, int(q_eq * 2.5))
    quantities = np.linspace(0, q_max, 200)
    
    demand_prices = demand_intercept - demand_slope * quantities
    supply_prices = supply_intercept + supply_slope * quantities

    # Filter out negative prices for demand curve
    valid_demand = demand_prices >= 0
    
    df_demand = pd.DataFrame({
        'Quantity': quantities[valid_demand],
        'Price': demand_prices[valid_demand],
        'Curve': 'Demand'
    })
    
    df_supply = pd.DataFrame({
        'Quantity': quantities,
        'Price': supply_prices,
        'Curve': 'Supply'
    })
    
    df = pd.concat([df_demand, df_supply])

    # Plot using Altair
    base = alt.Chart(df).encode(
        x=alt.X('Quantity:Q', title='Quantity (Q)'),
        y=alt.Y('Price:Q', title='Price (P)')
    )

    line_chart = base.mark_line(size=4).encode(
        color=alt.Color('Curve:N', scale=alt.Scale(domain=['Demand', 'Supply'], range=['#1f77b4', '#ff7f0e']))
    )

    # Equilibrium Point
    eq_point = pd.DataFrame({'Quantity': [q_eq], 'Price': [p_eq], 'Curve': ['Equilibrium']})
    point_chart = alt.Chart(eq_point).mark_circle(size=150, color='red').encode(
        x='Quantity:Q',
        y='Price:Q',
        tooltip=['Quantity', 'Price']
    )

    # Annotation for equilibrium
    text_chart = alt.Chart(eq_point).mark_text(
        align='left', baseline='middle', dx=10, fontSize=14, color='white'
    ).encode(
        x='Quantity:Q',
        y='Price:Q',
        text=alt.value(f"Eq: ({q_eq:.1f}, ${p_eq:.1f})")
    )

    final_chart = (line_chart + point_chart + text_chart).properties(
        width=700,
        height=500
    ).configure_axis(
        labelFontSize=12,
        titleFontSize=14
    ).configure_legend(
        titleFontSize=13,
        labelFontSize=12
    )

    st.altair_chart(final_chart, use_container_width=True)

st.markdown("---")
st.markdown("**Powered by Streamlit, Altair, and Pandas**")
