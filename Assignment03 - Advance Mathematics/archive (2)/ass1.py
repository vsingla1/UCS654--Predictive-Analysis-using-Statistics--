import numpy as np
import pandas as pd

# -------------------------------
# 1. Load dataset
# -------------------------------
# Update path if needed
df = pd.read_csv("data.csv")

# Extract NO2 feature (drop missing values)
x = df["NO2"].dropna().values

# -------------------------------
# 2. Fixed roll-number parameters
# -------------------------------
Ar = 0.15
br = 0.6

# -------------------------------
# 3. Transformation (Step-1)
# -------------------------------
z = x + Ar * np.sin(br * x)

# -------------------------------
# 4. Parameter estimation (Step-2)
# -------------------------------

# Mean (mu)
mu = np.mean(z)

# Variance (MLE version, divide by n)
variance = np.mean((z - mu) ** 2)

# Lambda
lam = 1 / (2 * variance)

# Normalization constant c
c = np.sqrt(lam / np.pi)

# -------------------------------
# 5. Output results
# -------------------------------
print("Estimated parameters:")
print(f"mu (μ)     = {mu}")
print(f"lambda (λ) = {lam}")
print(f"c          = {c}")
