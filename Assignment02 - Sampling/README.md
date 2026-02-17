# Sampling Techniques and Model Accuracy Comparison

This project demonstrates the application of various sampling techniques on a dataset to evaluate their impact on the accuracy of machine learning models. It automates the process of sampling, training, and evaluating models while presenting the results in an easy-to-interpret matrix format.

---

## Project Workflow

1. **Dataset Download**: Automatically fetches the dataset from a provided URL.
2. **Data Balancing**: Uses oversampling, undersampling, or SMOTEENN techniques to handle class imbalances.
3. **Sampling Techniques**: Applies the following techniques:
   - Simple Random Sampling
   - Systematic Sampling
   - Stratified Sampling
   - Cluster Sampling
   - Oversampling
4. **Model Training**: Trains the following machine learning models:
   - Logistic Regression
   - Random Forest
   - Support Vector Machine (SVM)
   - Decision Tree
   - k-Nearest Neighbors (KNN)
5. **Accuracy Evaluation**: Compares the accuracy of models across different sampling techniques.
6. **Result Matrix**: Saves results in a pivot table format (`result-matrix.csv`).

---

## Results

The following table summarizes the accuracy achieved by each model with different sampling techniques:

| Model               | Cluster     | Oversampling | Simple Random | Stratified  | Systematic  |
| ------------------- | ----------- | ------------ | ------------- | ----------- | ----------- |
| Decision Tree       | 0.923076923 | 0.974025974  | 0.974025974   | 0.987012987 | 0.987012987 |
| KNN                 | 0.948717949 | 0.974025974  | 0.974025974   | 0.896103896 | 0.935064935 |
| Logistic Regression | 0.923076923 | 0.857142857  | 0.883116883   | 0.909090909 | 0.896103896 |
| Random Forest       | 0.948717949 | 1.000000000  | 1.000000000   | 0.987012987 | 1.000000000 |
| SVM                 | 0.948717949 | 0.688311688  | 0.675324675   | 0.740259740 | 0.805194805 |

### Analysis

- **Decision Tree and Systematic Sampling**: The Decision Tree model achieved the highest accuracy (0.987) using Systematic and Stratified Sampling.
- **Random Forest and Oversampling**: Random Forest consistently performed best with an accuracy of 1.000 when using Oversampling, Simple Random, and Systematic Sampling.
- **KNN and Cluster Sampling**: KNN performed well across all techniques but showed no significant advantage over others.
- **Logistic Regression**: Logistic Regression struggled with Oversampling but performed better with Stratified Sampling.
- **SVM**: SVM exhibited the lowest accuracy compared to other models, particularly with Simple Random and Oversampling techniques.

---

## Setup and Execution

1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/sampling-project.git
   cd sampling-project
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python main.py
   ```
4. Check the `result-matrix.csv` file for the accuracy matrix.

---

## Dependencies

- pandas
- numpy
- scikit-learn
- imbalanced-learn

Install all dependencies via:

```bash
pip install pandas numpy scikit-learn imbalanced-learn
```

---
