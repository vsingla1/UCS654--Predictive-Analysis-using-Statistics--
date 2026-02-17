import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.combine import SMOTEENN
import os

def download_dataset():
    url = "https://github.com/AnjulaMehto/Sampling_Assignment/raw/main/Creditcard_data.csv"
    dataset_path = "Creditcard_data.csv"
    if not os.path.exists(dataset_path):
        df = pd.read_csv(url)
        df.to_csv(dataset_path, index=False)
    else:
        df = pd.read_csv(dataset_path)
    return df

def balance_dataset(df, technique="oversampling"):
    X = df.drop(columns=["Class"])
    y = df["Class"]

    if technique == "oversampling":
        sampler = RandomOverSampler(random_state=42)
    elif technique == "undersampling":
        sampler = RandomUnderSampler(random_state=42)
    elif technique == "smoteenn":
        sampler = SMOTEENN(random_state=42)
    else:
        raise ValueError("Unsupported balancing technique")

    X_resampled, y_resampled = sampler.fit_resample(X, y)
    return pd.DataFrame(X_resampled, columns=X.columns).assign(Class=y_resampled)

def calculate_sample_size(population_size, confidence_level=0.95, margin_of_error=0.05):
    Z = {0.90: 1.645, 0.95: 1.96, 0.99: 2.576}[confidence_level]
    p = 0.5  # Assume 50% population proportion for maximum variability
    n = (Z**2 * p * (1 - p)) / margin_of_error**2
    return int(min(n, population_size))

def apply_sampling_techniques(df, sample_size):
    techniques = {}
    # Simple Random Sampling
    techniques["Simple Random"] = df.sample(n=sample_size, random_state=42)

    # Systematic Sampling
    step = len(df) // sample_size
    techniques["Systematic"] = df.iloc[::step].head(sample_size)

    # Stratified Sampling
    techniques["Stratified"] = df.groupby("Class", group_keys=False).apply(
        lambda x: x.sample(min(len(x), sample_size // 2), random_state=42))

    # Cluster Sampling (use Time column to create clusters)
    df["Cluster"] = pd.qcut(df["Time"], q=sample_size, labels=False)
    cluster_sample = df.groupby("Cluster").sample(n=1, random_state=42)
    techniques["Cluster"] = cluster_sample.drop(columns=["Cluster"])

    # Oversampling (already balanced, can be added as an example)
    techniques["Oversampling"] = balance_dataset(df, technique="oversampling").sample(n=sample_size, random_state=42)

    return techniques


def train_models(samples):
    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),
        "Random Forest": RandomForestClassifier(),
        "SVM": SVC(),
        "Decision Tree": DecisionTreeClassifier(),
        "KNN": KNeighborsClassifier()
    }

    results_matrix = pd.DataFrame(
        columns=["Sampling Technique", "Model", "Accuracy"]
    )

    for technique_name, sample in samples.items():
        X = sample.drop(columns=["Class"])
        y = sample["Class"]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        for model_name, model in models.items():
            model.fit(X_train, y_train)
            y_pred = model.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            # Append results to the matrix
            results_matrix = results_matrix.append({
                "Sampling Technique": technique_name,
                "Model": model_name,
                "Accuracy": accuracy
            }, ignore_index=True)

    return results_matrix

def main():
    df = download_dataset()
    balanced_df = balance_dataset(df, technique="oversampling")
    sample_size = calculate_sample_size(len(balanced_df))

    print(f"Calculated Sample Size: {sample_size}")
    samples = apply_sampling_techniques(balanced_df, sample_size)
    results_matrix = train_models(samples)

    # Display the results in a matrix format
    pivot_table = results_matrix.pivot(
        index="Model", columns="Sampling Technique", values="Accuracy"
    )
    print("\nResults Matrix:")
    print(pivot_table.round(2))  # Round to 2 decimal places for clarity

if __name__ == "__main__":
    main()