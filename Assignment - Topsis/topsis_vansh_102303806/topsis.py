import pandas as pd
import numpy as np
import sys
import os

def run_topsis(input_file, weights, impacts, output_file):
    # Check file exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError("Input file not found.")

    data = pd.read_csv(input_file)

    if data.shape[1] < 3:
        raise ValueError("Input file must contain at least 3 columns.")

    parameters = data.iloc[:, 1:]

    # Check numeric columns
    if not all(np.issubdtype(dtype, np.number) for dtype in parameters.dtypes):
        raise ValueError("All criteria columns must contain numeric values only.")

    if len(weights) != parameters.shape[1] or len(impacts) != parameters.shape[1]:
        raise ValueError("Number of weights and impacts must match number of criteria.")

    for i in impacts:
        if i not in ['+', '-']:
            raise ValueError("Impacts must be '+' or '-' only.")

    impacts = [1 if i == '+' else -1 for i in impacts]

    # Step 1: Normalize
    norm = parameters / np.sqrt((parameters ** 2).sum())

    # Step 2: Apply weights
    weighted = norm * weights

    # Step 3: Ideal best and worst
    ideal_best = [
        weighted.iloc[:, i].max() if impacts[i] == 1 else weighted.iloc[:, i].min()
        for i in range(len(impacts))
    ]
    ideal_worst = [
        weighted.iloc[:, i].min() if impacts[i] == 1 else weighted.iloc[:, i].max()
        for i in range(len(impacts))
    ]

    # Step 4: Distance
    d_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Score
    score = d_worst / (d_best + d_worst)

    # Step 6: Rank
    data["Topsis Score"] = score
    data["Rank"] = score.rank(ascending=False).astype(int)

    data.to_csv(output_file, index=False)
    print("TOPSIS analysis completed successfully.")


def main():
    args = sys.argv[1:]

    # Allow: topsis topsis.py input.csv weights impacts output.csv
    if len(args) == 5 and args[0].endswith(".py"):
        args = args[1:]

    if len(args) != 4:
        print("Usage:")
        print('topsis topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>')
        sys.exit(1)

    input_file = args[0]
    weights = list(map(float, args[1].split(",")))
    impacts = args[2].split(",")
    output_file = args[3]

    try:
        run_topsis(input_file, weights, impacts, output_file)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
