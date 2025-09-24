import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# -----------------------------
# Sidebar Configuration
# -----------------------------
st.sidebar.header("Configuration")
n_points = st.sidebar.slider("Number of data points (n)", 50, 1000, 500, step=50)
a_true = st.sidebar.slider("Coefficient 'a' (y = ax + b + noise)", -5.0, 5.0, 2.0, step=0.1)
noise_var = st.sidebar.slider("Noise Variance (var)", 1, 200, 100, step=1)
b_true = 3.0  # 固定截距（可改成 slider）

# -----------------------------
# Data Generation
# -----------------------------
np.random.seed(42)
X = np.random.rand(n_points, 1) * 10  # 0-10
noise = np.random.normal(0, np.sqrt(noise_var), size=n_points)
y = a_true * X.flatten() + b_true + noise

# -----------------------------
# Modeling with Linear Regression
# -----------------------------
model = LinearRegression()
model.fit(X, y)
y_pred = model.predict(X)

coef_a = model.coef_[0]
intercept_b = model.intercept_

# -----------------------------
# Residuals & Outlier Detection
# -----------------------------
residuals = y - y_pred
df = pd.DataFrame({"x": X.flatten(), "y": y, "residuals": residuals})

# Top 5 outliers by absolute residuals
top_outliers = df.reindex(df["residuals"].abs().sort_values(ascending=False).index[:5])

# -----------------------------
# Visualization
# -----------------------------
fig, ax = plt.subplots(figsize=(10, 5))
ax.scatter(X, y, alpha=0.6, label="Generated data")
ax.plot(X, y_pred, color="red", linewidth=2, label="Linear Regression")

# 標記 outliers
for idx, row in top_outliers.iterrows():
    ax.scatter(row["x"], row["y"], color="purple", s=100, edgecolors="black", zorder=3)
    ax.text(row["x"], row["y"], f"Outlier {idx}", fontsize=9, color="purple")

ax.set_xlabel("X")
ax.set_ylabel("y")
ax.legend()

# -----------------------------
# Streamlit Layout
# -----------------------------
st.title("Interactive Linear Regression Visualizer")

st.pyplot(fig)

st.subheader("Model Coefficients")
st.write(f"**Coefficient (a):** {coef_a:.2f}")
st.write(f"**Intercept (b):** {intercept_b:.2f}")

st.subheader("Top 5 Outliers")
st.dataframe(top_outliers)
