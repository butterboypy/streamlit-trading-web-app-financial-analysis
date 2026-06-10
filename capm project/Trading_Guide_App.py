import streamlit as st

st.set_page_config(
    page_title="Trading App",
    page_icon="💸",
    layout="wide"
)

st.title("Trading Guide App 📊")
st.write("---")
st.header("Welcome to the Trading Guide App!")

# Maintain your local image banner asset pipeline
st.image("app.png")

st.write("---")
st.markdown("## 🛠️ Core Analytical Services & Architecture")
st.write("---")

# Section 1
st.markdown("### :one: Systemic Risk Profiling & CAPM Beta Engine")
st.write(
    "Quantify asset volatility relative to macro-market indices. This module calculates historical "
    "covariance metrics against the S&P 500 benchmark over custom multi-year windows to derive "
    "precise **Beta ($\beta$) coefficients** and map underlying equity risk profiles."
)

# Section 2
st.markdown("### :two: Multi-Asset Expected Return Optimization")
st.write(
    "Applied the mathematical foundation of the **Capital Asset Pricing Model (CAPM)** to evaluate "
    "portfolio risk-return trade-offs. This feature automates risk-premium evaluations to determine "
    "the baseline expected return requirements for individual equity tiers and diversified asset classes."
)

# Section 3
st.markdown("### :three: Real-Time Market Intelligence & Stock Analysis")
st.write(
    "Access institutional-grade market data streaming. Powered by live API connectivity, this interface "
    "delivers detailed financial disclosures, fundamental accounting metrics (EPS, P/E, Debt-to-Equity), "
    "and interactive technical analysis chart tracking featuring custom candle layouts and RSI oscillators."
)

# Section 4
st.markdown("### :four: Stochastic & Statistical Price Path Forecasting")
st.write(
    "Explore future asset valuation bounds through an advanced predictive suite. By incorporating an "
    "**Ensemble Hybrid Model**, the forecasting pipeline anchors long-term momentum to statistical time-series "
    "regression (ARIMA) while injecting realistic short-term daily volatility shocks via **Monte Carlo simulations**."
)

st.write("---")
st.caption("🚀 Designed by Krishnendu Das as an end-to-end Financial Analysis & Quantitative Data Project. Navigate using the sidebar to explore the individual analytical layers.")