import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    "results/all_sets_mean_hur.csv",
    index_col=0
)

print("\nCombined data:")
print(data)

data.plot(
    kind="bar",
    figsize=(8, 5)
)

plt.ylabel("Mean nuclear HuR intensity")
plt.xlabel("Experimental set")
plt.title("Nuclear HuR intensity across six experimental sets")
plt.xticks(rotation=0)
plt.legend(title="Condition")

plt.tight_layout()

plt.savefig(
    "figures/all_sets_hur_comparison.png",
    dpi=150
)

print("\nPlot saved.")
