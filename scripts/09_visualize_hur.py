from tifffile import imread
import matplotlib.pyplot as plt

from skimage.filters import threshold_otsu
from skimage.morphology import remove_small_objects
from skimage.measure import label, regionprops

# Load images
dapi_image = imread("data/set1/control/control_1_dapi.tif")
hur_image = imread("data/set1/control/control_1_hur.tif")

# Correct channels
dapi = dapi_image[:, :, 2]
hur = hur_image[:, :, 1]

# Detect nuclei
threshold = threshold_otsu(dapi)
nuclei = dapi > threshold
nuclei = remove_small_objects(nuclei, min_size=20)

# Label nuclei
labeled_nuclei = label(nuclei)

# Show HuR image
plt.figure(figsize=(7, 7))
plt.imshow(hur, cmap="gray")

# Add mean HuR value to each nucleus
for region in regionprops(labeled_nuclei):
    nucleus_mask = labeled_nuclei == region.label
    mean_hur = hur[nucleus_mask].mean()

    y, x = region.centroid

    plt.text(
        x, y,
        f"{region.label}: {mean_hur:.1f}",
        color="red",
        fontsize=8,
        ha="center"
    )

plt.title("Control 1 - HuR Intensity per Nucleus")
plt.axis("off")

plt.savefig(
    "figures/control_1_hur_measurements.png",
    dpi=150,
    bbox_inches="tight"
)

print("HuR measurement image saved.")
