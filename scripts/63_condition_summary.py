import pandas as pd

data = pd.read_csv(
    "results/all_sets_mean_hur.csv",
    index_col=0
)

summary = pd.DataFrame({
    "Mean": data.mean(),
    "SD": data.std()
})

print("\nCondition summary:")
print(summary)

summary.to_csv(
    "results/condition_summary_mean_sd.csv"
)

print("\nSummary saved.")
