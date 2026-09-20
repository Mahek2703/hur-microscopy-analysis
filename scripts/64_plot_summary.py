import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    "results/all_sets_mean_hur.csv",
    index_col=0
)

conditions = ["Control", "CMLD2", "PMA"]

means = data[conditions].mean()
stds = data[conditions].std()

plt.figure(figsize=(7, 5))

for i, condition in enumerate(conditions):
    values = data[condition]

    x = [i] * len(values)

    plt.scatter(
        x,
        values,
        s=60
    )

    plt.errorbar(
        i,
        means[condition],
        yerr=stds[condition],
        fmt="o",
        markersize=8,
        capsize=5
    )

plt.xticks(
    range(len(conditions)),
    conditions
)

plt.ylabel("Mean nuclear HuR intensity")
plt.xlabel("Condition")

plt.title(
    "Nuclear HuR intensity across six imaging fields"
)

plt.tight_layout()

plt.savefig(
    "figures/condition_mean_sd.png",
    dpi=150
)

print("\nPlot saved.")
