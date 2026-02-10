import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Load input data
# -----------------------------
df = pd.read_csv("input_data.csv")

models = df["Model"]

criteria_cols = [
    "BLEU",
    "ROUGE_L",
    "BERTScore",
    "Perplexity",
    "InferenceTime_ms",
    "ModelSize_MB",
    "EaseOfFinetuning"
]

# Convert to matrix
A = df[criteria_cols].values.astype(float)

# -----------------------------
# Weights (sum = 1)
# -----------------------------
weights = np.array([0.25, 0.20, 0.20, 0.15, 0.10, 0.05, 0.05])

# Benefit(True) / Cost(False)
benefit_flags = np.array([True, True, True, False, False, False, True])

# -----------------------------
# TOPSIS Steps
# -----------------------------

# Step 1: Normalize
norm = np.sqrt((A ** 2).sum(axis=0))
R = A / norm

# Step 2: Weighted normalized matrix
W = R * weights

# Step 3: Ideal best & worst
ideal_best = np.where(benefit_flags, W.max(axis=0), W.min(axis=0))
ideal_worst = np.where(benefit_flags, W.min(axis=0), W.max(axis=0))

# Step 4: Distances
S_plus = np.sqrt(((W - ideal_best) ** 2).sum(axis=1))
S_minus = np.sqrt(((W - ideal_worst) ** 2).sum(axis=1))

# Step 5: TOPSIS score
topsis_score = S_minus / (S_plus + S_minus)

df["TOPSIS_Score"] = topsis_score
df["Rank"] = df["TOPSIS_Score"].rank(ascending=False).astype(int)

df = df.sort_values("Rank")

# -----------------------------
# Save results
# -----------------------------
df.to_csv("topsis_results.csv", index=False)
print(df[["Model", "TOPSIS_Score", "Rank"]])

# -----------------------------
# Plot
# -----------------------------
plt.figure(figsize=(9, 5))
plt.bar(df["Model"], df["TOPSIS_Score"])
plt.xlabel("Models")
plt.ylabel("TOPSIS Score")
plt.title("TOPSIS Ranking of Text Generation Models")
plt.ylim(0, 1)
plt.xticks(rotation=20)
plt.tight_layout()
plt.savefig("topsis_ranking.png")
plt.show()
