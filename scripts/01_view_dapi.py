from tifffile import imread
import matplotlib.pyplot as plt

# Load the DAPI image
image = imread("data/set1/control/control_1_dapi.tif")

# Print basic information about the image
print("Image shape:", image.shape)
print("Data type:", image.dtype)
print("Minimum pixel value:", image.min())
print("Maximum pixel value:", image.max())

# Display the image
plt.imshow(image, cmap="gray")
plt.title("Control 1 - DAPI")
plt.axis("off")

# Save the image preview
plt.savefig("figures/control_1_dapi_preview.png", dpi=150, bbox_inches="tight")

print("Preview saved to figures/control_1_dapi_preview.png")
