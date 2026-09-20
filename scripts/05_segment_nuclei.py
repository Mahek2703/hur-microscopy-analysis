from tifffile import imread
import matplotlib.pyplot as plt

from skimage.filters import threshold_otsu
from skimage.morphology import remove_small_objects
from skimage.measure import label

# Load the DAPI image
image = imread("data/set1/control/control_1_dapi.tif")

# Use DAPI channel 2
dapi = image[:, :, 2]

# Automatically find a brightness threshold
threshold = threshold_otsu(dapi)

# Create a binary image
nuclei = dapi > threshold

# Remove very small bright objects
nuclei = remove_small_objects(nuclei, min_size=20)

# Give each nucleus a number
labeled_nuclei = label(nuclei)

# Count nuclei
number_of_nuclei = labeled_nuclei.max()

print("Otsu threshold:", threshold)
print("Number of detected nuclei:", number_of_nuclei)

# Save the binary mask
plt.imshow(nuclei, cmap="gray")
plt.title("Detected Nuclei - Control 1")
plt.axis("off")
plt.savefig(
    "figures/control_1_nuclei_mask.png",
    dpi=150,
    bbox_inches="tight"
)

print("Nuclei mask saved.")
