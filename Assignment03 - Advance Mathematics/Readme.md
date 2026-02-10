# **Title: Learn Probability Density Functions using Roll-Number-Parameterized Non-Linear Model**

## *1. Methodology*
- Load India Air Quality dataset.
- Select NO₂ feature and remove missing values.
- Transform data using: z = x + aᵣ sin(bᵣ x).
- Learn Gaussian PDF parameters using MLE.

## *2. Description*
- Learn a probability density function from air quality data.
- NO₂ concentration is used as the input feature.
- A roll-number-based non-linear transformation is applied.

## *3. Input*
- India Air Quality Dataset (Kaggle).
- NO₂ concentration values.
- University Roll Number.

## *4 .Output*
- Estimated PDF parameters:
  - μ (mean)
  - λ (precision parameter)
  - c (normalization constant)