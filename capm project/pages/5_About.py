import streamlit as st

st.set_page_config(
    page_title="About This Project",
    page_icon="📝",
    layout="wide"
)

st.title("Project Documentation & Engineering Insights 📝")
st.write("---")

# Three-part tab design separates high-level context from intense math/engineering blocks
tab1, tab2, tab3 = st.tabs(["📌 Project Overview", "🧮 Quantitative Methodologies", "💻 System Architecture"])

with tab1:
    st.markdown("### 🎯 Why This Project Exists")
    st.write(
        "Standard financial web portals often segment raw market fundamentals away from predictive modeling "
        "and portfolio risk engineering frameworks. This platform was built to bridge that gap—providing retail "
        "investors and portfolio managers with an integrated environment to track asset health, quantify systematic "
        "risk exposure, and evaluate stochastic future price paths."
    )
    
    st.markdown("### 🔍 Key Objectives")
    st.markdown(
        "* **Automate Risk Quantifications:** Extract live market returns to calculate standalone and comparative equity parameters on the fly.\n"
        "* **Demystify Complex Models:** Translate rigorous econometric algorithms (like ARIMA) and probability workflows (like Monte Carlo) into actionable, visual chart telemetry.\n"
        "* **Demonstrate Production Coding Standards:** Prove how modular software engineering practices apply directly to rapid quantitative financial analysis."
    )

with tab2:
    st.markdown("### 📐 Deep-Dive Financial Mathematics")
    st.write(
        "To ensure the application functions as a robust quantitative tool rather than a generic visualization "
        "tracker, several foundational financial frameworks were engineered directly into the pipeline:"
    )
    
    # Mathematical Breakdown of CAPM
    st.markdown("#### 1. The Capital Asset Pricing Model (CAPM)")
    st.write(
        "Systematic risk represents the vulnerability of an asset to broader, unavoidable market movements. "
        "This platform calculates an asset's unique Beta ($\beta$) coefficient by processing a rolling covariance matrix "
        "of the selected equity's daily percentage returns scaled against the absolute variance of the S&P 500 market index:"
    )
    st.latex(r"\beta = \frac{Cov(R_a, R_m)}{Var(R_m)}")
    st.write(
        "Once derived, Beta is integrated into the core CAPM pricing equation to resolve the asset's localized baseline "
        "Expected Return ($E(R_a)$), assuming a standard annualized risk-free benchmark rate:"
    )
    st.latex(r"E(R_a) = R_f + \beta \cdot (E(R_m) - R_f)")
    
    st.write("---")
    
    # Algorithmic Breakdown of the Hybrid Ensemble
    st.markdown("#### 2. The Hybrid Ensemble Forecasting Engine")
    st.write(
        "Traditional regression models (like ARIMA) excel at picking up macro trajectories but struggle to capture real-world risk because "
        "their predictions mathematically flatten into a smooth mean over multi-week horizons. Conversely, standalone Monte Carlo "
        "simulations capture daily market randomness but can drift away from logical economic trends."
    )
    st.write(
        "**The Solution:** This application implements a custom **Ensemble Pipeline**. The engine first trains an "
        "ARIMA(2, d, 2) model to compute the structural baseline trend. It then generates an array of normal distribution "
        "stochastic random market shocks derived from the asset's historical daily volatility ($\sigma$) and drift ($\mu$):"
    )
    st.latex(r"\text{Shock Factor} = e^{\left(-\frac{1}{2}\sigma^2 + \sigma \cdot Z_t\right)}")
    st.write(
        "By mathematically multiplying the smooth ARIMA trend baseline by the stochastic simulation shock values at each step, "
        "the final **Hybrid Ensemble** visualizes a prediction path that preserves realistic market behavior while tracking a logical trend."
    )

with tab3:
    st.markdown("### 🏗️ Software Engineering Design Pattern")
    st.write(
        "This application is built entirely on **clean coding principles**. Instead of utilizing single script files where "
        "calculations and UI code are dangerously tangled together, this codebase enforces strict **Separation of Concerns**:"
    )
    
    st.markdown("#### 📁 Directory Layout Breakdown")
    st.code(
        """
CAPM PROJECT/
├── Trading_Guide_App.py     # Main application landing page file
├── pages/                   # Isolated interface components
│   ├── 1_CAPM_Beta.py       # Portfolio risk engine view
│   ├── 2_CAPM_Return.py     # Capital pricing evaluation view
│   ├── 3_Stock_Analysis.py  # Fundamental indicator tracking view
│   ├── 4_Stock_Prediction.py# Forecasting tab matrix view
│   ├── 5_About_This_Project.py # Core system architectural guidelines
│   └── utils/               # MODULAR UTILITY LOGIC ENGINE
│       ├── __init__.py      # Standard python package indicator
│       ├── model_train.py   # Algorithmic mathematical back-end calculations
│       └── plotly_figure.py # Central high-contrast canvas layout designs
        """,
        language="text"
    )
    
    st.markdown("#### 🔄 Data Pipeline Flow")
    st.markdown(
        "1. **Ingestion:** User inputs a stock ticker inside a page file. The system calls `yfinance` through an isolated cache pipeline.\n"
        "2. **Transformation:** The raw data matrices pass cleanly into `model_train.py` where pandas arrays extract mathematical statistics.\n"
        "3. **Visualization Canvas:** The derived frames are transferred directly to `plotly_figure.py`, which strips raw pandas indexes and configures high-contrast chart layouts.\n"
        "4. **Render:** The final figure objects are passed back up to the frontend views where Streamlit draws them effortlessly onto the screen."
    )

st.write("---")
st.caption("📝 Project System Documentation Module • Version 1.1.0 • Built with Streamlit & Python")