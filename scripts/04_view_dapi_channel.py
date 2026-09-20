from tifffile import imread
import matplotlib.pyplot as plt

image = imread("data/set1/control/control_1_dapi.tif")

# Select channel 2
dapi = image[:, :, 2]

print("DAPI shape:", dapi.shape)
print("DAPI minimum:", dapi.min())
print("DAPI maximum:", dapi.max())

plt.imshow(dapi, cmap="gray")
plt.title("Control 1 - DAPI Channel 2")
plt.axis("off")

plt.savefig(
    "figures/control_1_dapi_channel2.png",
    dpi=150,
    bbox_inches="tight"
)

print("DAPI channel preview saved.")
