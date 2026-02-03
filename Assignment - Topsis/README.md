# TOPSIS Algorithm Implementation

## Program 1: Overview
TOPSIS (Technique for Order Preference by Similarity to Ideal Solution) is a multi-criteria decision-making (MCDM) technique used to rank alternatives based on their relative closeness to the ideal best and ideal worst solutions.

This project provides a complete **command-line based Python implementation** of the TOPSIS algorithm with proper validation and result generation.

---

### Features
- Accepts **custom weights** and **impacts** for each criterion
- Computes **TOPSIS Score** and **Rank**
- Works as a **command-line program**
- Generates results in a **CSV output file**
- Robust **error handling and input validation**
- Available as an **installable PyPI package**

---

## How TOPSIS Works (Brief)
1. Normalize the decision matrix  
2. Apply weights to normalized values  
3. Determine ideal best and ideal worst solutions  
4. Compute separation measures  
5. Calculate TOPSIS score  
6. Rank alternatives based on score  

---

## How to Use

### Prerequisites
- Python 3.7 or higher
- Required libraries:
  - `pandas`
  - `numpy`

Install dependencies (if running from source):
```bash
pip install pandas numpy
```

### Command-Line Usage
```bash
topsis <InputDataFile> <Weights> <Impacts> <ResultFileName>
```

### Parameters
1. **InputDataFile**: Path to the dataset file (CSV/XLSX). The first column lists alternatives, followed by numeric data for criteria.
2. **Weights**: Comma-separated values for criterion importance (e.g., `"1,2,3"`).
3. **Impacts**: Comma-separated values (`+` for maximize, `-` for minimize) indicating desired impact for each criterion (e.g., `"+,-,+"`).
4. **ResultFileName**: Name of the output file where results will be saved.

### Example Command
```bash
topsis sample_input.csv "1,1,1,1" "+,+,+,+" output.csv
```

---
## Program 2: PyPI Package
This implementation is available as a Python package on [`https://pypi.org/project/Topsis-Vansh-102303806/`](https://pypi.org/project/Topsis-Vansh-102203806/). You can easily install it via `pip`:


## Input File Format
The first column must contain alternative names.

All remaining columns must contain numeric criteria values.

The input file must have at least 3 columns.

Example Input (sample_input.csv)
Alternative	Cost	Quality	Delivery	Service
A1	250	7	4	8
A2	200	6	3	7


## Output
The output file includes:
- **Topsis Score**: Calculated score for each alternative.
- **Rank**: Rank based on the Topsis Score.

---

## Error Handling
The script validates:
- Correct number of parameters (inputFileName, Weights, Impacts, resultFileName).
- Show the appropriate message for wrong inputs.
- Handling of “File not Found” exception
- Input file must contain three or more columns.
- From 2nd to last columns must contain numeric values only (Handling of non-numeric values)
- Number of weights, number of impacts and number of columns (from 2nd to last columns) must
be same.
- Impacts must be either +ve or -ve.
- Impacts and weights must be separated by ‘,’ (comma).
