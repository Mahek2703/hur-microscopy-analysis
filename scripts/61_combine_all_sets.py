import pandas as pd

# Set 1
control_1 = pd.read_csv("results/control_1_hur_channel1_measurements.csv")
cmld2_1 = pd.read_csv("results/cmld2_1_hur_measurements.csv")
pma_1 = pd.read_csv("results/pma_1_hur_measurements.csv")

# Set 2
control_2 = pd.read_csv("results/control_2_hur_measurements.csv")
cmld2_2 = pd.read_csv("results/cmld2_2_hur_measurements.csv")
pma_2 = pd.read_csv("results/pma_2_hur_measurements.csv")

# Set 3
control_3 = pd.read_csv("results/control_3_hur_measurements.csv")
cmld2_3 = pd.read_csv("results/cmld2_3_hur_measurements.csv")
pma_3 = pd.read_csv("results/pma_3_hur_measurements.csv")

# Set 4
control_4 = pd.read_csv("results/control_4_hur_measurements.csv")
cmld2_4 = pd.read_csv("results/cmld2_4_hur_measurements.csv")
pma_4 = pd.read_csv("results/pma_4_hur_measurements.csv")

# Set 5
control_5 = pd.read_csv("results/control_5_hur_measurements.csv")
cmld2_5 = pd.read_csv("results/cmld2_5_hur_measurements.csv")
pma_5 = pd.read_csv("results/pma_5_hur_measurements.csv")

# Set 6
control_6 = pd.read_csv("results/control_6_hur_measurements.csv")
cmld2_6 = pd.read_csv("results/cmld2_6_hur_measurements.csv")
pma_6 = pd.read_csv("results/pma_6_hur_measurements.csv")

comparison = pd.DataFrame({
    "Control": [
        control_1["mean_hur"].mean(),
        control_2["mean_hur"].mean(),
        control_3["mean_hur"].mean(),
        control_4["mean_hur"].mean(),
        control_5["mean_hur"].mean(),
        control_6["mean_hur"].mean()
    ],
    "CMLD2": [
        cmld2_1["mean_hur"].mean(),
        cmld2_2["mean_hur"].mean(),
        cmld2_3["mean_hur"].mean(),
        cmld2_4["mean_hur"].mean(),
        cmld2_5["mean_hur"].mean(),
        cmld2_6["mean_hur"].mean()
    ],
    "PMA": [
        pma_1["mean_hur"].mean(),
        pma_2["mean_hur"].mean(),
        pma_3["mean_hur"].mean(),
        pma_4["mean_hur"].mean(),
        pma_5["mean_hur"].mean(),
        pma_6["mean_hur"].mean()
    ]
}, index=[
    "Set 1",
    "Set 2",
    "Set 3",
    "Set 4",
    "Set 5",
    "Set 6"
])

print("\nMean nuclear HuR intensity:")
print(comparison)

comparison.to_csv("results/all_sets_mean_hur.csv")

print("\nCombined results saved.")
