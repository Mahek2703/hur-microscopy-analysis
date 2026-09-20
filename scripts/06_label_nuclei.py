from tifffile import imread
import matplotlib.pyplot as plt

from skimage.filters import threshold_otsu
from skimage.morphology import remove_small_objects
from skimage.measure import label, regionprops

# Load DAPI image
image = imread("data/set1/control/control_1_dapi.tif")

# Use DAPI channel 2
dapi = image[:, :, 2]

# Create nuclei mask
threshold = threshold_otsu(dapi)
nuclei = dapi > threshold

# Remove very small objects
nuclei = remove_small_objects(nuclei, min_size=20)

# Label each nucleus
labeled_nuclei = label(nuclei)

# Find information about each nucleus
regions = regionprops(labeled_nuclei)

print("Number of detected nuclei:", len(regions))

# Display the labelled nuclei
plt.figure(figsize=(7, 7))
plt.imshow(dapi, cmap="gray")

for region in regions:
    y, x = region.centroid
    plt.text(x, y, str(region.label), color="red",
             fontsize=10, ha="center", va="center")

plt.title("Control 1 - Labelled Nuclei")
plt.axis("off")

plt.savefig(
    "figures/control_1_labelled_nuclei.png",
    dpi=150,
    bbox_inches="tight"
)

print("Labelled nuclei preview saved.")
