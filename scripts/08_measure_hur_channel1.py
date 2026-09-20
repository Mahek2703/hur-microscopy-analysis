from tifffile import imread
import pandas as pd

from skimage.filters import threshold_otsu
from skimage.morphology import remove_small_objects
from skimage.measure import label, regionprops

# Load DAPI and HuR images
dapi_image = imread("data/set1/control/control_1_dapi.tif")
hur_image = imread("data/set1/control/control_1_hur.tif")

# Use the correct channels
dapi = dapi_image[:, :, 2]
hur = hur_image[:, :, 1]

# Detect nuclei from DAPI
threshold = threshold_otsu(dapi)
nuclei = dapi > threshold
nuclei = remove_small_objects(nuclei, min_size=20)

# Label each nucleus
labeled_nuclei = label(nuclei)

# Measure HuR intensity
results = []

for region in regionprops(labeled_nuclei):
    nucleus_mask = labeled_nuclei == region.label
    mean_hur = hur[nucleus_mask].mean()

    results.append({
        "nucleus": region.label,
        "area": region.area,
        "mean_hur": mean_hur
    })

# Create a table
results_df = pd.DataFrame(results)

print(results_df)

# Save the measurements
results_df.to_csv(
    "results/control_1_hur_channel1_measurements.csv",
    index=False
)

print("Results saved.")
